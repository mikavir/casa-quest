import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, g)
from functools import wraps
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from pymongo import MongoClient
from gridfs import GridFS
from werkzeug.security import generate_password_hash, check_password_hash
import cloudinary
import cloudinary.uploader
import cloudinary.api

if os.path.exists("env.py"):
    import env


app = Flask(__name__)


# Configurations for MONGO DB
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# Configurations for Cloudinary API
cloudinary.config(
    cloud_name = os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key = os.environ.get('CLOUDINARY_API_KEY'),
    api_secret = os.environ.get('CLOUDINARY_API_SECRET')
)

"""
https://flask.palletsprojects.com/en/2.3.x/patterns/viewdecorators/
"""
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user") is None:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/", methods=["GET"])
def index():
    """
    Function to render to homepage if not logged in
    """
    return render_template("index.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Renders template for 'registration'

    Adds new user to MongoDB collect 'Users' then redirects to profile

    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "name": request.form.get("name").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("registration.html")


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    """

    Renders template for 'login'.

    Finds user details in MongoDB collection users and redirect to user profile. Adds session for users.

    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


#LOGOUT
@app.route("/logout")
@login_required
def logout():
    """
    Removes user session. 

    Redirects to login page

    """
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# USERS PROFILE/DASHBOARD
@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    """

    Renders template profile.html when user is in session

    Returns houses by the user.

    """
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
        
    houses = mongo.db.houses.find({"username": username})

    return render_template("profile.html", username=username, houses=houses)


# HOUSE
@app.route("/house/<house_id>", methods=["GET", "POST"])
@login_required
def view_house(house_id):
    """

    Renders template house

    Returns house information, house viewing, house personal checks of the house Object ID

    """
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
        
    house = mongo.db.houses.find_one({"_id": ObjectId(house_id)})

    if house is None:
        return redirect(url_for("profile", username=username))
    if username != house["username"]:
        return redirect(url_for("profile", username=username))
    
    # return redirect(url_for("view_house", house_id=house_id))

    # user is correct house owner and has acces to house info
    house_info = mongo.db.houseInformation.find_one({"_id": ObjectId(house_id)})

    house_check = mongo.db.houseChecks.find_one({"_id": ObjectId(house_id)})

    house_viewing = mongo.db.houseViewing.find_one({"_id": ObjectId(house_id)})

    traffic = ["Heavy Traffic", "Moderate Traffic", "No Traffic"]

    property_facing = ["South Facing", "North Facing", "West Facing", "East Facing"]

    noise = ["Quiet", "Some Noise", "Very Noisy"]

    storage_space = ["Minimal", "Moderate", "Abundant"]

    roof_condition = [
            ('Excellent', 'Newly installed or recently replaced, no visible damage or wear'),
            ('Good', 'Well-maintained, minor wear and tear, no significant issues'),
            ('Fair', 'Some signs of aging or minor damage, may require maintenance or repairs.'),
            ('Poor', 'Significant damage or deterioration, leaks, structural issues')
            ]



    return render_template(
        "house.html", username=username, house=house, house_info=house_info,
        house_check=house_check, house_viewing=house_viewing, traffic=traffic,
        property_facing=property_facing, noise=noise, storage_space=storage_space, roof_condition=roof_condition
    )


# ADD NEW HOUSE ENTRY
@app.route("/new_house",methods=["GET", "POST"])
@login_required
def new_house():
    """
    Renders template add new house.
     
    Adds house information to MongDB collection 'house' with cloudinary url. Redirects back to Profile/dashboard

    """
    if request.method == "POST":
        address = request.form.get("address")
        agency = request.form.get("agency")
        property_type = request.form.get("property_type")
        chainfree = "yes" if request.form.get("chain_free") else "no"
        bedrooms = request.form.get("no_bedrooms")
        bathrooms = request.form.get("no_bathrooms")
        price = request.form.get("house_price")
        date_viewing = request.form.get("date_viewing")
        image = request.files["image-url"]

        # Upload to cloudinary
        image_upload = cloudinary.uploader.upload(image)
     

        house_entry = {
            "username": session["user"],
            "address": address,
            "price": price,
            "agency": agency,
            "bathrooms": bathrooms,
            "bedrooms": bedrooms,
            "chainFree": chainfree,
            "propertyType": property_type, 
            "date_viewing": date_viewing,
            "image_url": image_upload["secure_url"]
        }

        mongo.db.houses.insert_one(house_entry)
        flash("house added!")
        return redirect(url_for(
                            "profile", username=session["user"]))
    else:
        types = ["Detached", "Semi-Detached", "Terraced"]
        return render_template("new_house.html", types=types)


# EDITS NEW HOUSE ENTRY
@app.route("/edit_new_house/<house_id>",methods=["GET", "POST"])
@login_required
def edit_new_house(house_id):
    """

    Renders edit new house template.

    Update house information to MongoDB collection 'house'. Redirects back to profile.

    """
    if request.method == "POST":
        
        address = request.form.get("address")
        agency = request.form.get("agency")
        property_type = request.form.get("property_type")
        chainfree = "yes" if request.form.get("chain_free") else "no"
        bedrooms = request.form.get("no_bedrooms")
        bathrooms = request.form.get("no_bathrooms")
        price = request.form.get("house_price")
        date_viewing = request.form.get("date_viewing")
        
        edit_house_entry = {
            "username": session["user"],
            "address": address,
            "price": price,
            "agency": agency,
            "bathrooms": bathrooms,
            "bedrooms": bedrooms,
            "chainFree": chainfree,
            "propertyType": property_type, 
            "date_viewing": date_viewing,
            
        }
        
        image = request.files["image-url"]
        if image.filename != '':
            image_upload = cloudinary.uploader.upload(image)
            edit_house_entry["image_url"] = image_upload["secure_url"]

        # Check if the id exist:
        house = mongo.db.houses.find_one({"_id": ObjectId(house_id)})

        if house is None:
            error_message = "Unable to edit a house that does not"
            return render_template("404.html", error_message=error_message)
     
        mongo.db.houses.update_one({"_id": ObjectId(house_id)}, {"$set": edit_house_entry})
        flash("House Successfully Updated")
        return redirect(url_for(
                            "profile", username=session["user"]))
    else:
        house = mongo.db.houses.find_one({"_id": ObjectId(house_id)})
        types = ["Detached", "Semi-Detached", "Terraced"]
        return render_template("edit_new_house.html", types=types, house=house)


# ADD HOUSE INFORMATION FROM MODAL
@app.route("/house/<house_id>#addInfoModal", methods=["GET", "POST"])
@login_required
def add_house_info(house_id):
    """
    Renders template hoouse. 

    Add house information to MongoDB collection 'houseInformation' and adds the same '_id' of house.

    """
    if request.method == "POST":
        house = mongo.db.houses.find_one({"_id": ObjectId(house_id)})
        epc = request.form.get("add_epc")
        tax_band = request.form.get("add_tax_band")
        flood_risk = request.form.get("add_flood_risk")
        internet_speed = request.form.get("add_internet_speed")
        dedicated_parking = "yes" if request.form.get("add_dedicated_parking") else "no"

        house_info = {
            "_id": ObjectId(house_id),
            "epc": epc,
            "taxBand": tax_band,
            "floodRisk": flood_risk,
            "internetSpeed": internet_speed,
            "dedicatedParking": dedicated_parking
        }

        house_data = mongo.db.houseInformation.find_one({"_id": ObjectId(house_id)})

        if house_data is None:
            mongo.db.houseInformation.insert_one(house_info)
            flash("House info added")
            return redirect(url_for("view_house", house_id=house_id))
        else: 
            error_message = "House Information already exists"
            return render_template("500.html", error_message=error_message)
    else:
       return redirect(url_for("view_house", house_id=house_id))



# EDIT HOUSE INFORMATION MODAL
@app.route("/house/<house_id>#editInfoModal", methods=["GET", "POST"])
@login_required
def edit_house_info(house_id):
    """
    Renders template house. 

    Edits house information to MongoDB collection 'houseInformation' and adds the same '_id' of house.
    
    """
    if request.method == "POST":
        house = mongo.db.houses.find_one({"_id": ObjectId(house_id)})
        epc = request.form.get("epc")
        tax_band = request.form.get("tax_band")
        flood_risk = request.form.get("flood_risk")
        internet_speed = request.form.get("internet_speed")
        dedicated_parking = "yes" if request.form.get("dedicated_parking") else "no"

        edit_house_info = {
            "_id": ObjectId(house_id),
            "epc": epc,
            "taxBand": tax_band,
            "floodRisk": flood_risk,
            "internetSpeed": internet_speed,
            "dedicatedParking": dedicated_parking
        }

        house_data = mongo.db.houseInformation.find_one({"_id": ObjectId(house_id)})

       
        if house_data is None:
            error_message = "Unable to edit a house that does not exist"
            return render_template("404.html", error_message=error_message)
        else:        
            mongo.db.houseInformation.update_one({"_id": ObjectId(house_id)}, {"$set": edit_house_info})
            flash("House info edited")
            return redirect(url_for("view_house", house_id=house_id))
    else:
        return redirect(url_for("view_house", house_id=house_id))



# ADD HOUSE VIEWING INFORMATION FROM MODAL
@app.route("/house/<house_id>#addHouseViewingModal", methods=["GET", "POST"])
@login_required
def add_house_viewing(house_id):
    """
    Renders template house. 

    Add house viewing information to MongoDB collection 'houseViewing' and adds the same '_id' of house.

    """
    if request.method == "POST":
        house = mongo.db.houses.find_one({"_id": ObjectId(house_id)})
        sellers_situation = request.form.get("add_sellers-sitaution")
        neighbours = request.form.get("add_neighbours")
        facilities = request.form.get("add_facilities")
        traffic = request.form.get("add_traffic")
        other_offers = "yes" if request.form.get("add_offers") else "no"
        double_glazed_windows = "yes" if request.form.get("add_windows") else "no"

        house_viewing_info = {
            "_id": ObjectId(house_id),
            "sellersSituation": sellers_situation,
            "neighbours": neighbours,
            "traffic": traffic,
            "otherOffers": other_offers,
            "facilities": facilities,
            "windows": double_glazed_windows
        }
      
        house_data = mongo.db.houseViewing.find_one({"_id": ObjectId(house_id)})

        if house_data is None:
            mongo.db.houseViewing.insert_one(house_viewing_info)
            flash("House viewing info added")
            return redirect(url_for("view_house", house_id=house_id))
        else: 
            error_message = "House viewing information already exists"
            return render_template("500.html", error_message=error_message)

    else:
        return redirect(url_for("view_house", house_id=house_id))



# EDIT HOUSE VIEWING INFORMATION FROM MODAL
@app.route("/house/<house_id>#editHouseViewingModal", methods=["GET", "POST"])
@login_required
def edit_house_viewing(house_id):
    """
    Renders template house. 

    Edit house viewing information to MongoDB collection 'houseViewing' and adds the same '_id' of house.

    """
    if request.method == "POST":
        house = mongo.db.houses.find_one({"_id": ObjectId(house_id)})
        sellers_situation = request.form.get("sellers-sitaution")
        neighbours = request.form.get("neighbours")
        facilities = request.form.get("facilities")
        traffic = request.form.get("traffic")
        other_offers = "yes" if request.form.get("offers") else "no"
        double_glazed_windows = "yes" if request.form.get("windows") else "no"

        edit_house_viewing_info = {
            "_id": ObjectId(house_id),
            "sellersSituation": sellers_situation,
            "neighbours": neighbours,
            "traffic": traffic,
            "otherOffers": other_offers,
            "facilities": facilities,
            "windows": double_glazed_windows
        }
      
        # Check to ensure that there is a house entry in the database
        house_data = mongo.db.houseViewing.find_one({"_id": ObjectId(house_id)})

        if house_data is None:
            error_message = "Unable to edit a house that does not exist"
            return render_template("404.html", error_message=error_message)
        else:
            # else: Allow to update database
            mongo.db.houseViewing.update_one({"_id": ObjectId(house_id)}, {"$set": edit_house_viewing_info})
            flash("House viewing info edited")
            return redirect(url_for("view_house", house_id=house_id))
    else:
        return redirect(url_for("view_house", house_id=house_id))


# Add HOUSE PERSONAL CHECK FROM MODAL
@app.route("/house/<house_id>#addHouseCheckModal", methods=["GET", "POST"])
@login_required
def add_house_check(house_id):
    """
    Renders template house. 

    Add house checks to MongoDB collection 'houseChecks and adds the same '_id' of house.

    """
    if request.method == "POST":
        house = mongo.db.houses.find_one({"_id": ObjectId(house_id)})
        property_facing = request.form.get("add_property_facing")
        noise_level = request.form.get("add_noise_level")
        boiler_noise = request.form.get("add_boiler_noise")
        storage_space = request.form.get("add_storage_space")
        attic_access = "yes" if request.form.get("add_attic") else "no"
        electric_ports = "yes" if request.form.get("add_electric_ports") else "no"
        mould = "yes" if request.form.get("add_mould") else "no"
        damp = "yes" if request.form.get("add_damp") else "no"
        crack = "yes" if request.form.get("add_crack") else "no"
        roof_condition = request.form.get("add_roof_condition")

        add_house_check_info = {
            "_id": ObjectId(house_id),
            "propertyFacing": property_facing,
            "noisePollution": noise_level,
            "boilerNoise": boiler_noise,
            "storageSpace": storage_space,
            "atticAccess": attic_access,
            "electricPorts": electric_ports,
            "mould": mould,
            "damp": damp,
            "crack": crack,
            "roofCondition": roof_condition
        }

        # Check to ensure that there is a house entry in the database
        house_data = mongo.db.houseChecks.find_one({"_id": ObjectId(house_id)})

        if house_data is None:
            mongo.db.houseChecks.insert_one(add_house_check_info)
            flash("Personal House Checks Added")
            return redirect(url_for("view_house", house_id=house_id))
        else:
            error_message = "House Check Information already exists"
            return render_template("500.html", error_message=error_message)
    else:
        return redirect(url_for("view_house", house_id=house_id))


# EDIT HOUSE PERSONAL CHECK FROM MODAL
@app.route("/house/<house_id>#editHouseCheckModal", methods=["GET", "POST"])
@login_required
def edit_house_check(house_id):
    """
    Renders template house. 

    Edit house checks to MongoDB collection 'houseChecks and adds the same '_id' of house.

    """
    if request.method == "POST":
        house = mongo.db.houses.find_one({"_id": ObjectId(house_id)})
        property_facing = request.form.get("property_facing")
        noise_level = request.form.get("noise_level")
        boiler_noise = request.form.get("boiler_noise")
        storage_space = request.form.get("storage_space")
        attic_access = "yes" if request.form.get("attic") else "no"
        electric_ports = "yes" if request.form.get("electric_ports") else "no"
        mould = "yes" if request.form.get("mould") else "no"
        damp = "yes" if request.form.get("damp") else "no"
        crack = "yes" if request.form.get("crack") else "no"
        roof_condition = request.form.get("roof_condition")

        edit_house_check_info = {
            "_id": ObjectId(house_id),
            "propertyFacing": property_facing,
            "noisePollution": noise_level,
            "boilerNoise": boiler_noise,
            "storageSpace": storage_space,
            "atticAccess": attic_access,
            "electricPorts": electric_ports,
            "mould": mould,
            "damp": damp,
            "crack": crack,
            "roofCondition": roof_condition
        }

        house_data = mongo.db.houseChecks.find_one({"_id": ObjectId(house_id)})

        if house_data is None:
            error_message = "Unable to edit a house that does not exist"
            return render_template("404.html", error_message=error_message)
        else:
            mongo.db.houseChecks.update_one({"_id": ObjectId(house_id)}, {"$set": edit_house_check_info})
            flash("House checks info edited")
            return redirect(url_for("view_house", house_id=house_id))
    else:
        return redirect(url_for("view_house", house_id=house_id))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)