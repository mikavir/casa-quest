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

if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
client = pymongo.MongoClient(os.environ.get("MONGO_URI"))
db = client["casa_quest"]
fs = GridFS(db)


"""
https://flask.palletsprojects.com/en/2.3.x/patterns/viewdecorators/
"""
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        username = session["user"]
        if username is None:
            return redirect("/login")
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


@app.route("/login", methods=["GET", "POST"])
def login():
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


@app.route("/logout")
@login_required
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
        
    houses = mongo.db.houses.find()

    if session["user"]:
        return render_template("profile.html", username=username, houses=houses)

    return redirect(url_for("login"))


@app.route("/new_house",methods=["GET", "POST"])
@login_required
def new_house():
    if request.method == "POST":
        address = request.form.get("address")
        agency = request.form.get("agency")
        property_type = request.form.get("property_type")
        chainfree = "yes" if request.form.get("chain_free") else "no"
        bedrooms = request.form.get("no_bedrooms")
        bathrooms = request.form.get("no_bathrooms")
        price = request.form.get("house_price")
        date_viewing = request.form.get("date_viewing")

        #   # Check if the file is present in the request
        # if 'image-file' in request.files:
        #     image_file = request.files['image-file']
        #     # if image_file.filename != '':
        #         # A file has been uploaded so add to database
        #     image_id = fs.put(image_file)
        #     # else:
        #     #     # No file uploaded
        #     #     with open("static/images/house-placeholder.jpg") as image_placeholder:
        #     #         image_id = fs.put(image_placeholder)
        #     #         print("No file uploaded")
        # else:
        #     print("No file field in the request")
        

        house_entry = {
            "username": session["user"],
            "address": address,
            "price": price,
            "agency": agency,
            "bathrooms": bathrooms,
            "bedrooms": bedrooms,
            "chainFree": chainfree,
            "propertyType": property_type, 
            "date_viewing": date_viewing
        }

        # # if image_id is not None:
        # house_entry["image"] = image_id
        
        db.houses.insert_one(house_entry)
        flash("house added!")
        return redirect(url_for(
                            "profile", username=session["user"]))
    else:
        types = ["Detached", "Semi-Detached", "Terraced"]
        return render_template("new_house.html", types=types)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)