# [CASA QUEST](https://casa-quest-853d4c81f9b1.herokuapp.com)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/mikavir/casa-quest)](https://github.com/mikavir/casa-quest/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/mikavir/casa-quest)](https://github.com/mikavir/casa-quest/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/mikavir/casa-quest)](https://github.com/mikavir/casa-quest)

![screenshot](documentation/mokup-casa-quest.png)

source: [amiresponsive](https://ui.dev/amiresponsive?url=https://casa-quest-853d4c81f9b1.herokuapp.com)

**Casa Quest: Your Ultimate House-Hunting Adventure Begins Here!**

Introducing a responsive web app for house-hunters to efficiently organize and track properties. Users can create personalized accounts, curate dashboards with viewed and upcoming houses, and utilize built-in tools for comparing properties, streamlining the house-hunting process.

## UX



### Colour Scheme

Initially, these colors were selected to complement our logo. The shades of green and their corresponding hues were chosen for their association with tranquility and harmony. This makes them ideal for a website dedicated to house hunters searching for their perfect, peaceful home.

- Primary Color: rgb(250, 236, 217) - Hex: #FAECD9
- Secondary Color: rgb(88, 126, 123) - Hex: #587E7B
- Tertiary Color: rgb(253, 253, 253) - Hex: #FDFDFD
- Accent Color: rgb(23, 53, 59) - Hex: #17353B


I used [coolors.co](https://coolors.co/faecd9-587e7b-fdfdfd-17353b) to generate my colour palette.

![screenshot](documentation/casa-quest-colour-scheme.png)

As I developed my project, I discovered additional colors from the Materialize library that complemented my existing color scheme.

- #004d40 teal darken-4
- #00796b teal darken-2
- #ffe0b2 orange lighten-4

In total, these were the colours that made the website.

[coolors.co](https://coolors.co/fdfdfd-faecd9-ffe0b2-587e7b-00796b-004d40-17353b)
![screenshot](documentation/casa-quest-full-colours.png)

This was the colour taken from materialize web for cancel buttons: 

-#b71c1c red darken-4

![screenshot](documentation/casa-quest-colour-red.png)
[coolors.co](https://coolors.co/b71c1c)

### Typography

After researching other home buying websites and gathering ideas, I found significant inspiration in the design of the [Mr and Mrs Clarke](https://www.mrandmrsclarke.com/) website. The fonts used in the website have been inspired the fonts that they have used.


- [Domine](https://fonts.google.com/specimen/Domine) was used for the primary headers and titles.

- [Questrial](https://fonts.google.com/specimen/Questrial) was used for all other secondary text.

- [Material Icons](https://fonts.google.com/icons?icon.set=Material+Icons) was used for icons from Materialize web.

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## User Stories

### New Site Users

- As a new site user, I would like to see a clear logo, so that I can remember the brand.
- As a new site user, I would like to see a clear message of the web app, so that I can understand the web applicatioon well.
- As a new site user, I would like to see navigation bar, so that I can easily navigate around the site.
- As a new site user, I would like to see a contact page, so that I can get in touch with the administrators of the application if I need help.
- As a new site user, I would like to see social media icons so that I can reach out at the other sources.

### Returning Site Users

- As a returning site user, I would like to be able to register, so that I can have a personal account.
- As a returning site user, I would like to be able to log in once registered, so that I can keep a track of properties visited.
- As a returning site user, I would like to be able to make new entries of properties, so that I can keep a log of my properties.
- As a returning site user, I would like to edit the information, so that I can have a more accurate information on the property.
- As a returning site user, I would like to delete the entry, so that I can eliminate properties that I'm not interested.
- As a returning site user, I would like to see a community of homebuyers, so that I can learn more about buying houses.
- As a returning site user, I would like to be able to make a post in the community of homebuyers, so that I can share my experience.
- As a returning site user, I would like to be able to make a comment in a post in the community of homebuyers, so that I can share my experience.
- As a returning site user, I would like to be able to change my password, so that I can keep my account secure.
### Site Admin

- As a site administrator, I would like to keep connected with my users , so that they can report any user experience.
- As a site administrator, I should be able to delete posts that is against the rules, so that I can ensure that the community is safe.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

### Mobile Wireframes

<details>
<summary> Click here to see the Mobile Wireframes </summary>

Landing Page
  - ![screenshot](documentation/wireframes/landing-mobile.png)

Profile
  - ![screenshot](documentation/wireframes/profile-mobile.png)

House Post
  - ![screenshot](documentation/wireframes/mobile-contact.png)

Login
  - ![screenshot](documentation/wireframes/login-mobile.png)

Register
  - ![screenshot](documentation/wireframes/register-mobile.png)

Contact
  - ![screenshot](documentation/wireframes/contact-mobile.png)

Blog
  - ![screenshot](documentation/wireframes/blog-mobile.png)
</details>

### Tablet Wireframes

<details>
<summary> Click here to see the Tablet Wireframes </summary>

Landing Page
  - ![screenshot](documentation/wireframes/landing-tablet.png)

Profile
  - ![screenshot](documentation/wireframes/profile-tablet.png)

House Post
  - ![screenshot](documentation/wireframes/mobile-tablet.png)

Login
  - ![screenshot](documentation/wireframes/login-tablet.png)

Register
  - ![screenshot](documentation/wireframes/register-tablet.png)

Contact
  - ![screenshot](documentation/wireframes/contact-tablet.png)

Blog
  - ![screenshot](documentation/wireframes/blog-tablet.png)

</details>

### Desktop Wireframes

<details>
<summary> Click here to see the Desktop Wireframes </summary>

Landing Page
  - ![screenshot](documentation/wireframes/landing-desktop.png)

Profile
  - ![screenshot](documentation/wireframes/profile-desktop.png)

House Post
  - ![screenshot](documentation/wireframes/mobile-desktop.png)

Login
  - ![screenshot](documentation/wireframes/login-desktop.png)

Register
  - ![screenshot](documentation/wireframes/register-desktop.png)

Contact
  - ![screenshot](documentation/wireframes/contact-desktop.png)

Blog
  - ![screenshot](documentation/wireframes/blog-desktop.png)


</details>

## Features

### Existing Features

- **Landing Page**

    - The landing page creates the first impression of the website, conveying the core message and purpose of the web application. It establishes the theme for the entire site and strengthens the brand image. Featuring a hero image of a family, it suggests the idea of families finding a home together, enhancing the emotional connection with visitors.

![screenshot](documentation/feature/casa-quest-feature-landing.png)

- **Call out message and button**

    - Having a callout button simplifies navigation by prompting users to take action. For example, the 'Start Your Casa Quest Now' button encourages users to create an account.

![screenshot](documentation/feature/casa-quest-feature-callout.png)

- **Dashboard**

    - Having a dashboard of houses with key information provides centralized access to property details. Users can view all relevant information about various properties in one place, eliminating the need to switch between different pages or apps. This setup allows for quick and easy comparison of multiple properties based on criteria such as price, location, number of bedrooms, and features

![screenshot](documentation/feature/casa-quest-feature-dashboard.png)
- **Favourite**

    - Users can mark properties as favorites, which then appear on a dedicated favorites page for easy access and review. This feature allows users to keep all their preferred properties in one place, simplifying the management and review process. By maintaining a favorites list, users can quickly compare their top choices without needing to search for them again

![screenshot](documentation/feature/casa-quest-feature-favourite.png)

- **Manage Account**

    - A centralized place to manage account settings reduces complexity, making it easy for users to update their password or logout.

![screenshot](documentation/feature/casa-quest-feature-manage-account.png)

### Future Features

- YOUR-TITLE-FOR-FUTURE-FEATURE-#1
    - Any additional notes about this feature.
- YOUR-TITLE-FOR-FUTURE-FEATURE-#2
    - Any additional notes about this feature.
- YOUR-TITLE-FOR-FUTURE-FEATURE-#3
    - Any additional notes about this feature.

## Tools & Technologies Used
- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.
- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) used for user interaction on the site.
- [![jQuery](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) used for user interaction on the site.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![Materialize](https://img.shields.io/badge/Materialize-grey?logo=materialdesign&logoColor=F5A5A8)](https://materializecss.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [![Flask](https://img.shields.io/badge/Flask-grey?logo=flask&logoColor=000000)](https://flask.palletsprojects.com) used as the Python framework for the site.
- [![MongoDB](https://img.shields.io/badge/MongoDB-grey?logo=mongodb&logoColor=47A248)](https://www.mongodb.com) used as the non-relational database management with Flask.
- [![Cloudinary](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) used for online static file storage.
- [![Balsamiq](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) used for creating wireframes.
- [![Canva](https://img.shields.io/badge/Canva-grey?logo=canva&logoColor=00C4CC)](https://www.canva.com/p/canvawireframes) used for creating logo.
- [![Google Maps API](https://img.shields.io/badge/Google_Maps_API-grey?logo=googlemaps&logoColor=4285F4)](https://developers.google.com/maps) used as an interactive map on my site.
- [![Font Awesome](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) used for the icons.
- [![Google Fonts](https://img.shields.io/badge/Google_Fonts-grey?logo=goole&logoColor=528DD7)](https://fonts.google.com/icons) used for the icons and fonts

- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to make the writing content.
- [![Email JS](https://img.shields.io/badge/EmailJs-grey?logo=javascript&logoColor=75A99C)](https://www.emailjs.com/) used to send automatic replies to user after contacting.
## User Pathway
Using Lucidchart, I have illustrated the user pathways as shown below.
![screenshot](documentation/database/user-flow-pathway.png)
## Database Design

The data used for Casa Quest was inspired by a list of questions my partner and I compiled while viewing houses. Initially, we organized these questions into a comprehensive table shown below. 
The idea emerged to transform the table into a more digital, user-friendly format with organized data.

![screenshot](documentation/database/table-questions.png)

Using [Lucid Chart](www.lucidchart.com), I have made an entity relationship diagram to show a physical data model.
![erd](documentation/database/erd.png)

My project uses a non-relational database with MongoDB, and therefore the database architecture
doesn't have actual relationships like a relational database would.

My database is called **casa_quest**.

It contains 7 collections:

- **users**
- **house**
- **houseInformation**
- **houseChecks**
- **houseViewing**
- **blogPost**
- **blogComment**

During the course of developing my project, I realized that the Minimum Viable Product (MVP) should focus on organizing house information rather than creating blog posts. This insight led me to eliminate the blog post feature and concentrate on achieving the core MVP. Below is the updated ERD of my project.

![screenshot](documentation/database/updated_erd.png)

With this, the mongo database have been updated to 5 collections:

![screenshot](documentation/database/mongo-collections.png)



## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://casa-quest-853d4c81f9b1.herokuapp.com).

### MongoDB Non-Relational Database

This project uses [MongoDB](https://www.mongodb.com) for the Non-Relational Database.

To obtain your own MongoDB Database URI, sign-up on their site, then follow these steps:

- The name of the database on MongoDB should be called **insert-your-database-name-here**.
- The collection(s) needed for this database should be **insert-your-collection-names-here**.
- Click on the **Cluster** name created for the project.
- Click on the **Connect** button.
- Click **Connect Your Application**.
- Copy the connection string, and replace `password` with your own password (also remove the angle-brackets).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `DATABASE_URL` | user's own value |
| `IP` | 0.0.0.0 |
| `MONGO_DBNAME` | user's own value |
| `MONGO_URI` | user's own value |
| `PORT` | 5000 |
| `SECRET_KEY` | user's own value |

Heroku needs three additional files in order to deploy properly.

- requirements.txt
- Procfile
- runtime.txt

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: python app.py > Procfile`
- *replace **app.py** with the name of your primary Flask app name; the one at the root-level*

The **runtime.txt** file needs to know which Python version you're using:
1. type: `python3 --version` in the terminal.
2. in the **runtime.txt** file, add your Python version:
	- `python-3.9.18`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Obtaining EmailJS API 

1. Sign up for a [EmailJS](https://www.emailjs.com/docs/) account in the EmailJS website.
2. Create an email service in your EmailJS dashboard.
3. Install EmailJS Library. You can do this by including the EmailJS script in your HTML file or by installing it via npm if you're using a package manager like npm or yarn.

```
npm install --save @emailjs/browser
```

or

```
$ yarn add @emailjs/browser
```

4. In your EmailJS dashboard, navigate to the "API Keys" section and copy your API key.
5. Add this code snippet before your closing tags. Making sure you have added your public key.

```js
<script type="text/javascript"
        src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js">
</script>
<script type="text/javascript">
  (function(){
      emailjs.init({
        publicKey: "YOUR_PUBLIC_KEY",
      });
  })();
</script>
```

6.  Create an email template in your EmailJS dashboard. This template will define the content and structure of the emails you'll send.
7. Write JavaScript function to send email using EmailJS. Below is a basic syntax for the code: 

```
emailjs.send(serviceID, templateID, templateParams, options);
```

8. Call your function whenever you want to send an email.

### Obtaining EmbedMaps API 

1. Create a Google Cloud Platform account at [Google Cloud](https://cloud.google.com/?hl=en)
2. Set up a new project in the Google Cloud Console.
3. Enable the required Google Maps APIs from the “API & Services” dashboard.
4. Create API credentials and generate an API key and enable 'Embed Maps API'
5. Optionally restrict the API key for security under “Application restrictions” and “API restrictions.”
6. Set up billing in the Google Cloud Console.
7. Set up your API Key in your env.py
```python

os.eviron.get("MAPS_API", "user's own value")

```
8. Integrate it into your Flask app:
```python

parameters = address

maps_api = os.environ.get('MAPS_API')

embed_url = f"https://www.google.com/maps/embed/v1/place?key={maps_api}&q={parameters}"

```
9. If deployed to Heroku, Add the API key to the config vars

### Obtaining Cloudinary API
1. Sign Up at Cloudinary and verify your email.
2. Log In to your Cloudinary account.
3. Find Your API Credentials in the dashboard (Cloud name, API Key, and API Secret).
4. Install the Cloudinary Python SDK
```sh
pip3 install cloudinary
```
5. Add your Cloudinary API key to your env.py
```python
import os 

os.environ.setdefault("CLOUDINARY_CLOUD_NAME", "user's own value")
os.environ.setdefault("CLOUDINARY_API_KEY", "user's own value")
os.environ.setdefault("CLOUDINARY_API_SECRET", "user's own value")


```

6. Configure Cloudinary in your Python application:
```python
import os
import cloudinary 

cloudinary.config(
    cloud_name = os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key = os.environ.get('CLOUDINARY_API_KEY'),
    api_secret = os.environ.get('CLOUDINARY_API_SECRET')
)
```
7. Integrate it with your flask app
```python
file = request.files["file"]

# Upload to cloudinary
file_upload = cloudinary.uploader.upload(file)

```

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps, plus a few extras.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("MONGO_DBNAME", "user's own value")
os.environ.setdefault("MONGO_URI", "user's own value")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DB_URL", "user's own value")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "True")
```


#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/mikavir/casa-quest) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git shell or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/mikavir/casa-quest.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/mikavir/casa-quest)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/mikavir/casa-quest)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to discuss any differences between the local version you've developed, and the live deployment site on Heroku.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## Credits

### Content

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [StackOverflow](https://stackoverflow.com/questions/67937305/how-to-get-the-size-of-a-multipart-form-data-binary-file) | app.py: `add_new_house()` and `edit_new_house()` | "How to find the size of an image upload" |
| [StackOver Flow](https://stackoverflow.com/questions/42294/how-do-you-get-the-footer-to-stay-at-the-bottom-of-a-web-page) | entire site | How to bring the footer at the bottom of the HTML |
| [Mr and Mrs Clarke](https://www.mrandmrsclarke.com/) | entire site | Inspiration on the design |
| [study.com](https://study.com/learn/lesson/python-not-equal-conditional-operators.html#:~:text=Python%20Not%20Equal%20Operator,the%20return%20value%20is%20true.) | app.py | Conditional operations |
| [Code Academy](https://www.codecademy.com/learn/dscp-python-fundamentals/modules/dscp-python-dictionaries/cheatsheet) | app.py: `delete_user(username, user_name)` | To access the house_id key in the dictionary |
| [Geek for geeks](https://www.geeksforgeeks.org/how-to-search-for-an-object-by-its-objectid-in-the-mongo-console/) | app.py | How to searh for object id in mongo |
| [w3 schools](https://www.w3schools.com/python/ref_list_append.asp) | app.py | How to append to make a list |
| [Flasks docs](https://flask-docs-ja.readthedocs.io/en/latest/patterns/errorpages/) | app.py | Making routes for error pages |
| [Google Cloud](https://developers.google.com/maps/documentation/embed/get-started) | app.py | Documentation on Embed maps API |
| [Flask](https://flask.palletsprojects.com/en/2.3.x/tutorial/templates/) | All templates | Adding titles using jinja syntax on templates |
| [W3 Schools](https://www.w3schools.com/tags/att_input_pattern.asp) | Registration page, login page and change password page | Adding pattern requirements on passwords |
| [StackOverflow](https://stackoverflow.com/questions/3974985/update-mongodb-field-using-value-of-another-field) | app.py | Updating mongodb using field of another field|
| [Tedboy](https://tedboy.github.io/flask/generated/werkzeug.check_password_hash.html) | app.py | Documentation on check_password_hash|
| [StackOverflow](https://stackoverflow.com/questions/28968660/how-to-convert-a-pymongo-cursor-cursor-into-a-dict) | app.py | How to convert a mongodb curser to a list of dictionary|
| [w3 schools](https://www.w3schools.com/tags/ref_urlencode.ASP) | entire site | used to debug url and the routes|
of dictionary|
| [Migelgrinberg](https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask) | app.py | Handling File Uploads With Flask|
| [StackOverflow](https://stackoverflow.com/questions/572768/styling-an-input-type-file-button) | styles.css | Styling an input type file button|
| [Youtube](https://www.youtube.com/watch?v=J39KJ5jzH3E) | app.py | How to add google autocomplete |
| [shecodes.io](https://www.shecodes.io/athena/264269-how-to-order-a-list-vertically-using-css#:~:text=list%20and%20set%20the%20display,items%20vertically%20in%20a%20column.&text=This%20will%20order%20the%20list%20items%20vertically%20instead%20of%20horizontally.) | styles.css | How to order a list vertically |
| [Great Wall of Gratitude](https://github.com/VCGithubCode/Gratidudes) | styles.css | How to create a toggle animation of hamburger to x sign. |
| [mikavir](https://github.com/mikavir/rx-decoder) | contact page, email.js | Setting up the emailjs and contact page |
### Media

| Source | Location | Type | Notes |
| --- | --- | --- | --- |
| [FreePik](https://www.freepik.com/free-photo/back-view-family-hugging-admiring-their-home_22426721.htm#query=house&position=49&from_view=keyword&track=sph&uuid=6f9398b1-ef01-41fa-912d-7c88cb9c1d84") | Landing Page |Image | Hero image background- Image by zinkevych |
| [FreePik](https://www.freepik.com/free-photo/full-shot-woman-with-cute-greyhound-dog_38898080.htm#fromView=search&page=1&position=52&uuid=9ddc6669-3e79-4dc2-a09c-c84210518efc) | Landing Page | image | Image |
| [Pexels]( https://www.pexels.com/photo/house-lights-turned-on-106399/) | House | placeholder image of a house | Photo by Binyamin Mellish |
| [Pexels](https://www.pexels.com/photo/beige-bungalow-house-259588/) | House | Placeolder | Photo by Pixabay |
| [Canvas](https://www.canva.com/) | Logo | Logo | Personalised logo |


### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for his support throughout the development of this project.
- I would like to thank my Code Insititute Cohort Facilitator Amy for answering all my questions promptly and boosting my confidence.
- I would like to thank a few individuals from my cohort for helping me fight against imposter syndrome and giving feedback on my project.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my partner Jon, for being my rubber duck when I need to debug.

