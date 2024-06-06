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
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET')
)


def login_required(f):
    """
    Function to ensure that user is logged in

    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        """
        https://flask.palletsprojects.com/en/2.3.x/patterns/viewdecorators/
        """
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


@app.route("/500", methods=["GET"])
def text500():
    """
    Function to render to 500.html for testing purposes
    """
    return render_template("500.html")


@app.route("/contact", methods=["GET"])
def contact():
    """
    Render's contact page template
    """
    email_api = os.environ.get("EMAIL_API")
    return render_template("contact.html", email_api=email_api)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Renders template for 'registration'

    Adds new user to MongoDB collect 'Users' then redirects to profile

    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username")})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # Grab variables from form:
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        #  Registration form validation
        if [name, username, password, confirm_password] is None:
            flash("Registration failed: Please complete the required fields")
            return redirect(url_for("register"))
        if len(username) < 5 or len(username) > 30:
            flash("Registration failed: Please complete the required fields")
            return redirect(url_for("register"))
        # https://www.w3schools.com/python/ref_string_isalnum.asp
        if not password.isalnum() and len(password) < 8:
            flash("Registration failed: Please complete the required fields")
            return redirect(url_for("register"))
        if password != confirm_password:
            flash("Registration failed: Please complete the required fields")
            return redirect(url_for("register"))
        else:
            register = {
                "name": name,
                "username": username,
                "password": generate_password_hash(password)
            }
            mongo.db.users.insert_one(register)

            # put the new user into 'session' cookie
            session["user"] = request.form.get("username")
            flash("Registration Successful!")
            return redirect(url_for("profile", username=session["user"]))

    return render_template("registration.html")


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    """

    Renders template for 'login'.

    Finds user details in MongoDB collection users and
    redirect to user profile. Adds session for users.

    """
    if request.method == "POST":
        # Validate that username and password is not an empty string:
        username = request.form.get("username")
        password = request.form.get("password")
        if username is None:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
        if password is None:
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": username}
        )

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(existing_user["password"], password):
                session["user"] = username
                flash("Welcome, {}".format(username))
                return redirect(url_for(
                    "profile", username=session["user"]
                ))
                # invalid password match
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# LOGOUT
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
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if username == "systemadmin":
        houses = mongo.db.houses.find()
    # grab the session user's username from db
    else:
        houses = mongo.db.houses.find({"username": username})

    return render_template("profile.html", username=username, houses=houses)


# HOUSE
@app.route("/house/<house_id>", methods=["GET", "POST"])
@login_required
def view_house(house_id):
    """

    Renders template house

    Returns house information, house viewing,
    house personal checks of the house Object ID.

    """
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    house = mongo.db.houses.find_one({"_id": ObjectId(house_id)})

    if house is None:
        return redirect(url_for("profile", username=username))
    if username != house["username"] and username != "systemadmin":
        return redirect(url_for("profile", username=username))

    # return redirect(url_for("view_house", house_id=house_id))

    # user is correct house owner and has acces to house info
    house_info = mongo.db.houseInformation.find_one(
        {"_id": ObjectId(house_id)}
    )

    house_check = mongo.db.houseChecks.find_one(
        {"_id": ObjectId(house_id)}
    )

    house_viewing = mongo.db.houseViewing.find_one(
        {"_id": ObjectId(house_id)}
    )

    ammount = ["Heavy", "Moderate", "No"]

    property_facing = [
        "South", "North", "West", "East"
        ]

    storage_space = ["Minimal", "Moderate", "Abundant"]

    roof_condition = [
        ('Excellent', 'Newly installed or recently replaced, no visible damage or wear'),  # noqa
        ('Good', 'Well-maintained, minor wear and tear, no significant issues'),  # noqa
        ('Fair', 'Some signs of aging or minor damage, may require maintenance or repairs.'),  # noqa
        ('Poor', 'Significant damage or deterioration, leaks, structural issues')  # noqa
    ]

    characters = ["A", "B", "C", "D", "E", "F", "G"]

    return render_template(
        "house.html", username=username, house=house, house_info=house_info,
        house_check=house_check, house_viewing=house_viewing, ammount=ammount,
        property_facing=property_facing, storage_space=storage_space,
        roof_condition=roof_condition, characters=characters
    )


# ADD NEW HOUSE ENTRY
@app.route("/new_house", methods=["GET", "POST"])
@login_required
def new_house():
    """
    Renders template add new house.

    Adds house information to MongDB collection 'house' with cloudinary url.
    Redirects back to Profile/dashboard

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
        }

        # Google maps API:
        maps_api = os.environ.get('MAPS_API')

        # Seperate address in order to put replace characters
        address_list = address.split(" ")

        # Add characters
        parameters = "+".join(address_list)

        # Google maps embed:
        embed_url = f"https://www.google.com/maps/embed/v1/place?key={maps_api}&q={parameters}"  # noqa

        # Add embedded url to the insert
        house_entry["mapsUrl"] = embed_url

        # Upload to cloudinary
        # Check the size of image file nefore uploading
        #  Move the file pointer to the end of the image_file
        # https://stackoverflow.com/questions/67937305/how-to-get-the-size-of-a-multipart-form-data-binary-file
        image = request.files["image-url"]

        image.seek(0, os.SEEK_END)

        # Get the current position of the pointer,
        # which is the size of the file
        image_size = image.tell()

        # Move the file pointer back to the beginning of the file
        image.seek(0, os.SEEK_SET)

        # Convert file size to MB
        image_size_mb = image_size / (1024 * 1024)

        # if image name is not an emoty string and less than 10mb,
        # to upload to cloudinary
        if image.filename != '' and image_size_mb < 10:
            image_upload = cloudinary.uploader.upload(image)
            house_entry["image_url"] = image_upload["secure_url"]
        else:
            flash("Image unable to be uploaded")
            temp_image_url = "https://res.cloudinary.com/dpqnw6tkn/image/upload/v1715774209/vnxhz63wmo25sthxvsst.jpg"  # noqa
            house_entry["image_url"] = temp_image_url

        mongo.db.houses.insert_one(house_entry)
        flash("house added!")
        return redirect(url_for(
                            "profile", username=session["user"]))
    else:
        maps_api = os.environ.get('MAPS_API')
        types = ["Detached", "Semi-Detached", "Terraced"]
        return render_template(
            "new_house.html", types=types, maps_api=maps_api
            )


# EDITS NEW HOUSE ENTRY
@app.route("/edit_new_house/<house_id>", methods=["GET", "POST"])
@login_required
def edit_new_house(house_id):
    """

    Renders edit new house template.

    Update house information to MongoDB collection 'house'.
    Redirects back to profile.

    """
    house = mongo.db.houses.find_one({"_id": ObjectId(house_id)})
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
            "username": house["username"],
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
            image.seek(0, os.SEEK_END)

            # https://stackoverflow.com/questions/67937305/how-to-get-the-size-of-a-multipart-form-data-binary-file
            # Get the current position of the pointer,
            # which is the size of the file
            image_size = image.tell()

            # Move the file pointer back to the
            # beginning of the file
            image.seek(0, os.SEEK_SET)

            # Convert file size to MB
            image_size_mb = image_size / (1024 * 1024)
            if image_size_mb < 10:
                image_upload = cloudinary.uploader.upload(image)
                edit_house_entry["image_url"] = image_upload["secure_url"]
            else:
                flash("Unable to upload image")

        # Check if the id exist:
        house = mongo.db.houses.find_one({"_id": ObjectId(house_id)})

        if house is None:
            error_message = "Unable to edit a house that does not"
            return render_template("404.html", error_message=error_message)

        mongo.db.houses.update_one(
            {"_id": ObjectId(house_id)}, {"$set": edit_house_entry}
            )
        flash("House Successfully Updated")
        return redirect(url_for(
                            "profile", username=session["user"]))

    maps_api = os.environ.get('MAPS_API')
    types = ["Detached", "Semi-Detached", "Terraced"]
    return render_template(
        "edit_new_house.html", types=types, house=house, maps_api=maps_api
        )


# ADD HOUSE INFORMATION FROM MODAL
@app.route("/house/<house_id>#addInfoModal", methods=["GET", "POST"])
@login_required
def add_house_info(house_id):
    """
    Renders template house.

    Add house information to MongoDB collection
    'houseInformation' and adds the same '_id' of house.

    """
    if request.method == "POST":
        epc = request.form.get("add_epc")
        tax_band = request.form.get("add_tax_band")
        flood_risk = request.form.get("add_flood_risk")
        internet_speed = request.form.get("add_internet_speed")
        dedicated_parking = "yes" if request.form.get("add_dedicated_parking") else "no"  # noqa

        house_info = {
            "_id": ObjectId(house_id),
            "epc": epc,
            "taxBand": tax_band,
            "floodRisk": flood_risk,
            "internetSpeed": internet_speed,
            "dedicatedParking": dedicated_parking
        }

        house_data = mongo.db.houseInformation.find_one(
            {"_id": ObjectId(house_id)}
            )

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

    Edits house information to MongoDB collection
    'houseInformation' and adds the same '_id' of house.

    """
    if request.method == "POST":
        epc = request.form.get("epc")
        tax_band = request.form.get("tax_band")
        flood_risk = request.form.get("flood_risk")
        internet_speed = request.form.get("internet_speed")
        dedicated_parking = "yes" if request.form.get("dedicated_parking") else "no"  # noqa

        edit_house_info = {
            "_id": ObjectId(house_id),
            "epc": epc,
            "taxBand": tax_band,
            "floodRisk": flood_risk,
            "internetSpeed": internet_speed,
            "dedicatedParking": dedicated_parking
        }

        house_data = mongo.db.houseInformation.find_one(
            {"_id": ObjectId(house_id)}
            )

        if house_data is None:
            error_message = "Unable to edit a house that does not exist"
            return render_template("404.html", error_message=error_message)
        mongo.db.houseInformation.update_one(
            {"_id": ObjectId(house_id)}, {"$set": edit_house_info}
            )
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

    Add house viewing information to MongoDB collection
    'houseViewing' and adds the same '_id' of house.

    """
    if request.method == "POST":
        sellers_situation = request.form.get("add_sellers_sitaution")
        neighbours = request.form.get("add_neighbours")
        facilities = request.form.get("add_facilities")
        traffic = request.form.get("add_traffic")
        other_offers = "yes" if request.form.get("add_offers") else "no"
        double_glazed_windows = "yes" if request.form.get("add_windows") else "no"  # noqa

        house_viewing_info = {
            "_id": ObjectId(house_id),
            "sellersSituation": sellers_situation,
            "neighbours": neighbours,
            "traffic": traffic,
            "otherOffers": other_offers,
            "facilities": facilities,
            "windows": double_glazed_windows
        }
        house_data = mongo.db.houseViewing.find_one(
            {"_id": ObjectId(house_id)}
            )

        if house_data is None:
            mongo.db.houseViewing.insert_one(house_viewing_info)
            flash("House viewing info added")
            return redirect(url_for("view_house", house_id=house_id))
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

    Edit house viewing information to MongoDB collection 'houseViewing'
    and adds the same '_id' of house.

    """
    if request.method == "POST":
        sellers_situation = request.form.get("sellers_sitaution")
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
        house_data = mongo.db.houseViewing.find_one(
            {"_id": ObjectId(house_id)}
            )

        if house_data is None:
            error_message = "Unable to edit a house that does not exist"
            return render_template("404.html", error_message=error_message)
        # else: Allow to update database
        mongo.db.houseViewing.update_one(
            {"_id": ObjectId(house_id)}, {"$set": edit_house_viewing_info}
            )
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

    Add house checks to MongoDB collection
    'houseChecks and adds the same '_id' of house.

    """
    if request.method == "POST":
        property_facing = request.form.get("add_property_facing")
        noise_level = request.form.get("add_noise_level")
        boiler_noise = request.form.get("add_boiler_noise")
        storage_space = request.form.get("add_storage_space")
        attic_access = "yes" if request.form.get("add_attic") else "no"
        electric_ports = "yes" if request.form.get("add_electric_ports") else "no"  # noqa
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

    Edit house checks to MongoDB collection
    'houseChecks and adds the same '_id' of house.

    """
    if request.method == "POST":
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

        house_data = mongo.db.houseChecks.find_one(
            {"_id": ObjectId(house_id)}
            )

        if house_data is None:
            error_message = "Unable to edit a house that does not exist"
            return render_template("404.html", error_message=error_message)
        mongo.db.houseChecks.update_one(
            {"_id": ObjectId(house_id)}, {"$set": edit_house_check_info}
            )
        flash("House checks info edited")
        return redirect(url_for("view_house", house_id=house_id))
    return redirect(url_for("view_house", house_id=house_id))


# Delete house
@app.route(
    "/profile/<username>#deleteModal<house_id>", methods=["GET", "POST"]
)
@login_required
def delete_house(username, house_id):
    """
    Deletes any house entry with the same id from the
    database and redirects back to the profile

    """
    if request.method == "POST":
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        house = mongo.db.houses.find_one({"_id": ObjectId(house_id)})

        if house is None:
            return redirect(url_for("profile", username=username))
        if username != house["username"] and username != "systemadmin":
            return redirect(url_for("profile", username=username))

        house_info = mongo.db.houseInformation.find_one(
            {"_id": ObjectId(house_id)}
            )

        house_check = mongo.db.houseChecks.find_one(
            {"_id": ObjectId(house_id)}
            )

        house_viewing = mongo.db.houseViewing.find_one(
            {"_id": ObjectId(house_id)}
            )

        if house_info is not None:
            mongo.db.houseInformation.delete_one(
                {"_id": ObjectId(house_id)}
                )

        if house_check is not None:
            mongo.db.houseChecks.delete_one(
                {"_id": ObjectId(house_id)}
                )

        if house_viewing is not None:
            mongo.db.houseViewing.delete_one(
                {"_id": ObjectId(house_id)}
            )

        if house is not None:
            mongo.db.houses.delete_one(
                {"_id": ObjectId(house_id)}
                )
            flash("House Deleted")
        return redirect(url_for("profile", username=username))
    return redirect(url_for("profile", username=username))


@app.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    """
    Renders 'change_password.html' when request method is get.

    When request method is POST, current password from user and
    their chosen new password is acquired and checked with their
    current password with werkzeug.security check_password_hash
    If succesful, a new hash is generated and database is updated.

    Inspired from my project Health Diary Keeper
    (https://github.com/mikavir/health-diary-keeper/blob/main/app.py)

    """
    if request.method == "POST":
        # Find username
        username = mongo.db.users.find_one(
            {"username": session["user"]})

        # Acquire form fields
        current_password = request.form.get("current_password")
        new_password = request.form.get("new_password")
        confirm_password = request.form.get("confirm_new_password")

        # Validate that input is not empty
        if current_password and new_password and confirm_password is None:
            flash("Please complete the required fields")
            return redirect(url_for('change_password'))

        # Check to see if new_password and confirm_password is same
        if new_password == confirm_password:

            # Use check_password_hash to ensure that
            # the current password is the same as database
            if check_password_hash(username["password"], current_password):

                # Generate a new password hash:
                new_hash_password = generate_password_hash(new_password)

                # New entry to the database
                new_password_entry = {"password": new_hash_password}

                # Update database and return
                mongo.db.users.update_one(
                    {"username": session["user"]}, {"$set": new_password_entry}
                    )
                flash("Password succesfully changed!")
                return redirect(url_for('change_password'))

        flash("Changing password failed!")
        return render_template("change_password.html")

    return render_template("change_password.html")


@app.route("/favourites/<username>/<house_id>", methods=["GET", "POST"])
@login_required
def add_to_favourites(username, house_id):
    """

    Renders template of 'favourites.html'

    When request is POST. It updates database that house is 'is_favourite' and
    returns to favourites.html

    """
    if request.method == "POST":
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        # Update is favourite in the house
        update_favourite = {"is_favourite": "yes"}
        mongo.db.houses.update_one(
            {"_id": ObjectId(house_id)}, {"$set": update_favourite}
            )
        flash("House added to favourites")
        houses = mongo.db.houses.find({"username": username})

        return render_template(
            "favourites.html", username=username, houses=houses
            )
    houses = mongo.db.houses.find({"username": username})
    return render_template("favourites.html", username=username, houses=houses)


@app.route("/favourites/<username>/remove/<house_id>", methods=["GET", "POST"])
@login_required
def remove_from_favourites(username, house_id):
    """

    Renders template of 'profile'

    When request is POST. It updates database that house is 'is_favourite' and
    returns back to profile.

    """
    if request.method == "POST":
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        # Update is favourite in the house
        update_favourite = {"is_favourite": "no"}
        mongo.db.houses.update_one(
            {"_id": ObjectId(house_id)}, {"$set": update_favourite}
            )
        flash("Removed from favourites")
        return redirect(url_for("profile", username=session["user"]))
    return redirect(url_for("profile", username=session["user"]))


@app.route("/favourites/<username>", methods=["GET"])
@login_required
def favourites(username):
    """
    Renders the favourites.html template

    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    houses = mongo.db.houses.find({"username": username})

    return render_template(
        "favourites.html", username=username, houses=houses
        )


#  ----------------ADMIN FUNCTIONALILITIES

@app.route("/manage_users/<username>", methods=["GET"])
@login_required
def manage_users(username):
    """
    Renders the manage_users.html only if username is equals to
    "systemadmin"

    returns a 403 page if not system admin
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if username == "systemadmin":
        users = mongo.db.users.find()
        return render_template("manage_users.html", users=users)
    return render_template('403.html'), 403


@app.route(
    "/manage_users/<username>#deleteModal<user_name>", methods=["GET", "POST"]
)
@login_required
def delete_user(username, user_name):
    """

    Admin function: (delete users)
    1) Using the username, it checks if it is truly the admin account
    2) Using the user_name it finds all the houses of under the user_name
    3) As find(), returns a curser, we make a list
    using a for loop of the houses
    4) Using .get(), we acquire the house_id of the houses.
    (https://www.codecademy.com/learn/dscp-python-fundamentals/modules/
    dscp-python-dictionaries/cheatsheet)
    5) With the house_id, we check if the id exist in the other collections and
    it deletes it.
    6) once all the houses have been deleted, the user is safely deleted.

    Returns a 403 if user is not 'systemadmin'

    """
    if request.method == "POST":
        # Find username and make sure username is "systemadmin"
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

        # find the houses by made by the user:
        if username == "systemadmin":
            user = mongo.db.users.find_one(
                {"username": user_name}
                )

            # As find users a pointer,
            # we need to convert it to a list by appneding
            houses = mongo.db.houses.find(
                {"username": user_name}
                )
            # user_houses list
            user_houses = []

            for house in houses:
                user_houses.append(house)

            for house in user_houses:
                # Find the data per house
                one_house = mongo.db.houses.find_one(house)

                # extract the id:
                house_id = one_house.get("_id")

                # Check the other database:

                house_info = mongo.db.houseInformation.find_one(
                    {"_id": ObjectId(house_id)}
                    )

                house_check = mongo.db.houseChecks.find_one(
                    {"_id": ObjectId(house_id)}
                    )

                house_viewing = mongo.db.houseViewing.find_one(
                    {"_id": ObjectId(house_id)}
                    )

                # delete any house_info if it exist
                if house_info is not None:
                    mongo.db.houseInformation.delete_one(
                        {"_id": ObjectId(house_id)}
                        )

                # delete any house_check if it exist
                if house_check is not None:
                    mongo.db.houseChecks.delete_one(
                        {"_id": ObjectId(house_id)}
                        )

                # delete any house_check if it exist
                if house_viewing is not None:
                    mongo.db.houseViewing.delete_one(
                        {"_id": ObjectId(house_id)}
                        )

                # delete any house if it exist
                if house is not None:
                    mongo.db.houses.delete_one(
                        {"_id": ObjectId(house_id)}
                        )

            # Delete user once all the houses have been deleted
            # Additional defensive programming to make sure admin account is
            # not deleted.
            if user and user_name != "systemadmin":
                mongo.db.users.delete_one(
                    {"username": user_name}
                    )
                return redirect(url_for(
                    "manage_users",  username=session["user"]
                    ))
                flash("user deleted!")
            return redirect(url_for(
                "manage_users",  username=session["user"])
                )

        return render_template('403.html'), 403

    return redirect(url_for("manage_users",  username=session["user"]))


#  ----------------Error Handling pages

@app.errorhandler(404)
def page_not_found(e):
    """
    https://flask-docs-ja.readthedocs.io/en/latest/patterns/errorpages/

    Renders to 404 page.
    """
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server(e):
    """
    https://flask-docs-ja.readthedocs.io/en/latest/patterns/errorpages/

    Renders to 500 page.
    """
    # note that we set the 500 status explicitly
    return render_template('500.html'), 500


@app.errorhandler(403)
def page_forbidden(e):
    """
    https://flask-docs-ja.readthedocs.io/en/latest/patterns/errorpages/

    Renders to 403 page.
    """
    # note that we set the 403 status explicitly
    return render_template('403.html'), 403


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG", False))
