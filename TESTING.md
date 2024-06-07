# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

> [!NOTE]
> The addresses and usernames shown below are not associated with any individuals; they are random placeholder addresses used solely for testing purposes. User privacy and confidentiality have been maintained and strictly adhered to throughout the testing procedure.


## Code Validation
### HTML
I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

These are the files that I was able to validate using the url as the others needed to be logged in to be accessed.
| Validator| File | Screenshot | Notes |
| --- | --- | --- | --- |
|[W3C Validator](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcasa-quest-853d4c81f9b1.herokuapp.com%2Fcontact)| contact.html | ![screenshot](documentation/validation/html-validation/html-contact.png) | No errors found|
|[W3C Validator](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcasa-quest-853d4c81f9b1.herokuapp.com%2F)| index.html | ![screenshot](documentation/validation/html-validation/html-validation-index.png) | No errors found|
|[W3C Validator](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcasa-quest-853d4c81f9b1.herokuapp.com%2Flogin)| login.html | ![screenshot](documentation/validation/html-validation/html-validation-login.png) | No errors found|
|[W3C Validator](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcasa-quest-853d4c81f9b1.herokuapp.com%2Fregister)| register.html | ![screenshot](documentation/validation/html-validation/html-validation-register.png) | No errors found|

These are the HTML files that I valdiated by copying and pasting the HTML code and tested it as a direct input.
| File | Screenshot | Notes |
| --- | --- | --- |
| profile.html | ![screenshot](documentation/validation/html-validation/html-validation-dashboard.png) | No errors found|
| favourites.html | ![screenshot](documentation/validation/html-validation/html-validation-favourites.png) | No errors found|
| new_house.html | ![screenshot](documentation/validation/html-validation/html-validation-new-house.png) | No errors found|
| edit_new_house.html | ![screenshot](documentation/validation/html-validation/html-validation-edit-new-house.png) | No errors found|
| house.html | ![screenshot](documentation/validation/html-validation/html-validation-house.png) | No errors found|
| change_password.html | ![screenshot](documentation/validation/html-validation/html-validation-change-password.png) | No errors found|
| manage_users.html | ![screenshot](documentation/validation/html-validation/html-validation-manage_users.png) | No errors found|
| 404.html | ![screenshot](documentation/validation/html-validation/html-validation-404.png) | No errors found|
| 403.html | ![screenshot](documentation/validation/html-validation/html-validation-403.png) | No errors found|
| 500.html | ![screenshot](documentation/validation/html-validation/html-validation-500.png) | No errors found|

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | style.css | ![screenshot](documentation/validation/css-validation/casa-quest-css-validation.png) ![screenshot](documentation/validation/css-validation/casa-quest-css-validation-direct-input.png) | No error on style.css file, errors marked from the libraries used |


### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | script.js | ![screenshot](documentation/validation/javascript-validation/js-validation-script.png) |  Undefined variable of `M` from materialize initiation |
| static | house.js | ![screenshot](documentation/validation/javascript-validation/js-validation-house.png) ![screenshot](documentation/validation/javascript-validation/jshint-fix-house.png)| Recommendations to use dot notation with my form validation function Fix: (second screenshot) I have changed it to dot notation as recommended. Unused functions called into house template|
| static | email.js | ![screenshot](documentation/validation/javascript-validation/js-validation-email.png) | Undefined variable of `emailjs` and `M` from materialize. Unused variable of `sendmail`. This function was called in the contact.html|

I used separate script tags in certain HTML files to target only those specific id's in those pages.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| templates | login.html, change_password.html, register.html | ![screenshot](documentation/validation/javascript-validation/jshint-togglepassword.png) |  unused function as it get's called with buttons |
| templates | profile.html | ![screenshot](documentation/validation/javascript-validation/js-validation-profile.png) |  No errors |
| templates | favourites.html | ![screenshot](documentation/validation/javascript-validation/js-validation-favourites.png) | No errors |
| templates | change_password.html | ![screenshot](documentation/validation/javascript-validation/jshint-change-password.png) | unused variable validateForm which get's called on submitting the form |
| templates | new_house.html | ![screenshot](documentation/validation/javascript-validation/js-validation-new-house.png) ![screenshot](documentation/validation/javascript-validation/js-hint-fix-new_house.png)| Undefined variable of `google` from google API. Unused variable of `formValidation()`. This function will be called in once form is submitted.  Unused variable of `initAutoComplete()`. This function initialises google's autocomplete API. Recommendations to use dot notation with my form validation function Fix: (second screenshot) I have changed it to dot notation as recommended. |
| templates | edit_new_house.html | ![screenshot](documentation/validation/javascript-validation/js-validation-edit-house.png) ![screenshot](documentation/validation/javascript-validation/js-hint-fix-edit_new_house.png) | Undefined variable of `google` from google API. Unused variable of `formValidation()`. This function will be called in once form is submitted.  Unused variable of `initAutoComplete()`. This function initialises google's autocomplete API. Recommendations to use dot notation with my form validation function Fix: (second screenshot) I have changed it to dot notation as recommended. |
           

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | app.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/casa-quest/main/app.py) | ![screenshot](documentation/validation/python-validation/python-validation.png) | No issues |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues. As my project contains many pages, I will be splitting it into two tables
| Browser | Landing page(index) | Register | Log in  | Profile | House | Contact | Favourites | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome |![screenshot](documentation/testing/browsers/chrome/chrome-landing-page.png) |![screenshot](documentation/testing/browsers/chrome/chrome-registration-1.png) ![screenshot](documentation/testing/browsers/chrome/chrome-registration-2.png) |![screenshot](documentation/testing/browsers/chrome/chrome-login.png) | ![screenshot](documentation/testing/browsers/chrome/chrome-profile-1.png) ![screenshot](documentation/testing/browsers/chrome/chrome-profile-2.png) | ![screenshot](documentation/testing/browsers/chrome/chrome-house-1.png)![screenshot](documentation/testing/browsers/chrome/chrome-house-2.png) ![screenshot](documentation/testing/browsers/chrome/chrome-house-3.png) | ![screenshot](documentation/testing/browsers/chrome/chrome-contact.png) | ![screenshot](documentation/testing/browsers/chrome/chrome-favourites.png) | Works as expected |
| Safari | ![screenshot](documentation/testing/browsers/safari/safari-landing-page.png) ![screenshot](documentation/testing/browsers/safari/safari-landing-page-2.png) | ![screenshot](documentation/testing/browsers/safari/safari-register-1.png)![screenshot](documentation/testing/browsers/safari/safari-register-1.png) |![screenshot](documentation/testing/browsers/safari/safari-login.png)| ![screenshot](documentation/testing/browsers/safari/safari-profile-1.png) ![screenshot](documentation/testing/browsers/safari/safari-profile-2.png) |![screenshot](documentation/testing/browsers/safari/safari-house-1.png)| ![screenshot](documentation/testing/browsers/safari/safari-house-2.png) | ![screenshot](documentation/testing/browsers/safari/safari-contact.png) | Works as expected |
| Firefox | ![screenshot](documentation/testing/browsers/firefox/firefox-landing-1.png) ![screenshot](documentation/testing/browsers/firefox/firefox-landing-1.png)| ![screenshot](documentation/testing/browsers/firefox/firefox-register-1.png)![screenshot](documentation/testing/browsers/firefox/firefox-register-2.png)| ![screenshot](documentation/testing/browsers/firefox/firefox-login.png) | ![screenshot](documentation/testing/browsers/firefox/firefox-profile-1.png) ![screenshot](documentation/testing/browsers/firefox/firefox-profile-2.png)| ![screenshot](documentation/testing/browsers/firefox/firefox-house-1.png)![screenshot](documentation/testing/browsers/firefox/firefox-house-2.png) ![screenshot](documentation/testing/browsers/firefox/firefox-house-3.png)| ![screenshot](documentation/testing/browsers/firefox/firefox-contact.png) | ![screenshot](documentation/testing/browsers/firefox/firefox-favourites.png)| Works as expected |

| Browser | New House | Edit new house | Change Password  | Manage_users | 404 | 500 | 403 | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chrome |![screenshot](documentation/testing/browsers/chrome/chrome-new-house-1.png)  ![screenshot](documentation/testing/browsers/chrome/chrome-new-house-2.png)| ![screenshot](documentation/testing/browsers/chrome/chrome-edit-house-1.png) ![screenshot](documentation/testing/browsers/chrome/chrome-edit-house-2.png) |![screenshot](documentation/testing/browsers/chrome/chrome-change-password.png) | ![screenshot](documentation/testing/browsers/chrome/chrome-manage_users.png) | ![screenshot](documentation/testing/browsers/chrome/chrome-404.png) |![screenshot](documentation/testing/browsers/chrome/chrome-500.png)| ![screenshot](documentation/testing/browsers/chrome/chrome-403.png) | works as expected |
| Safari | ![screenshot](documentation/testing/browsers/safari/safari-new-house-1.png) ![screenshot](documentation/testing/browsers/safari/safari-new-house-2.png) | ![screenshot](documentation/testing/browsers/safari/safari-edit-house-1.png)![screenshot](documentation/testing/browsers/safari/safari-edit-house-2.png) |![screenshot](documentation/testing/browsers/safari/safari-change-password.png)| ![screenshot](documentation/testing/browsers/safari/safari-manage-users.png) |![screenshot](documentation/testing/browsers/safari/safari-404.png)| ![screenshot](documentation/testing/browsers/safari/safari-500.png) | ![screenshot](documentation/testing/browsers/safari/safari-403.png) | Works as expected |
| Firefox | ![screenshot](documentation/testing/browsers/firefox/firefox-new-house-1.png) ![screenshot](documentation/testing/browsers/firefox/firefox-new-house-2.png) | ![screenshot](documentation/testing/browsers/firefox/firefox-edit-house-1.png) ![screenshot](documentation/testing/browsers/firefox/firefox-edit-house-2.png) | ![screenshot](documentation/testing/browsers/firefox/firefox-change-password.png) | ![screenshot](documentation/testing/browsers/firefox/firefox-manage-users.png) | ![screenshot](documentation/testing/browsers/firefox/firefox-404.png)| ![screenshot](documentation/testing/browsers/firefox/firefox-500.png) |![screenshot](documentation/testing/browsers/firefox/firefox-403.png)| Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Landing page(index) | Register | Log in  | Profile | House | Contact | Favourites | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile DevTools (320px) |![screenshot](documentation/responsiveness/mobile-landing-page.png) |![screenshot](documentation/responsiveness/mobile-register.png)|![screenshot](documentation/responsiveness/mobile-login.png) | ![screenshot](documentation/responsiveness/mobile-dashboard.png)  | ![screenshot](documentation/responsiveness/mobile-house-2.png) ![screenshot](documentation/responsiveness/mobile-house-3.png)![screenshot](documentation/responsiveness/mobile-house1.png)| ![screenshot](documentation/responsiveness/mobile-contact.png) | ![screenshot](documentation/responsiveness/mobile-favourites.png) | Works as expected |
| Tablet DevTools (768px) | ![screenshot](documentation/responsiveness/tablet-landing.png)| ![screenshot](documentation/responsiveness/tablet-register.png)  |![screenshot](documentation/responsiveness/tablet-login.png) | ![screenshot](documentation/responsiveness/tablet-dashboard.png) | ![screenshot](documentation/responsiveness/tablet-house.png) |![screenshot](documentation/responsiveness/tablet-favourites.png)| ![screenshot](documentation/responsiveness/tablet-403.png) | works as expected |
| Desktop |![screenshot](documentation/testing/browsers/chrome/chrome-landing-page.png) |![screenshot](documentation/testing/browsers/chrome/chrome-registration-1.png) ![screenshot](documentation/testing/browsers/chrome/chrome-registration-2.png) |![screenshot](documentation/testing/browsers/chrome/chrome-login.png) | ![screenshot](documentation/testing/browsers/chrome/chrome-profile-1.png) ![screenshot](documentation/testing/browsers/chrome/chrome-profile-2.png) | ![screenshot](documentation/testing/browsers/chrome/chrome-house-1.png)![screenshot](documentation/testing/browsers/chrome/chrome-house-2.png) ![screenshot](documentation/testing/browsers/chrome/chrome-house-3.png) | ![screenshot](documentation/testing/browsers/chrome/chrome-contact.png) | ![screenshot](documentation/testing/browsers/chrome/chrome-favourites.png) | Works as expected |
| Iphone 13 (Own device) |![screenshot](documentation/responsiveness/iphone13-landing.PNG) ![screenshot](documentation/responsiveness/iphone13-landing-2.PNG) |![screenshot](documentation/responsiveness/iphone-13-register.PNG) ![screenshot](documentation/responsiveness/iphone13-register-2.PNG) |![screenshot](documentation/responsiveness/iphone-13-login.PNG) | ![screenshot](documentation/responsiveness/iphone13-dashboard-1.PNG) ![screenshot](documentation/responsiveness/iphone13-dashboard-2.PNG) ![screenshot](documentation/responsiveness/iphone13-dashboard-3.PNG) | ![screenshot](documentation/responsiveness/iphone13-house1.PNG)![screenshot](documentation/responsiveness/iphone13-house2.PNG) ![screenshot](documentation/responsiveness/iphone13-house3.PNG) | ![screenshot](documentation/responsiveness/iphone13-contact.PNG) | ![screenshot](documentation/responsiveness/iphone13-favourites1.PNG) ![screenshot](documentation/responsiveness/iphone13-favourites2.PNG) | Flash can be obscured by logo |

| Browser | New House | Edit new house | Change Password  | Manage_users | 404 | 500 | 403 | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile DevTools (320px) |![screenshot](documentation/responsiveness/mobile-new-house.png)| ![screenshot](documentation/responsiveness/mobile-edit-house.png)  |![screenshot](documentation/responsiveness/mobile-change-password.png) | ![screenshot](documentation/responsiveness/mobile-manage-users.png) | ![screenshot](documentation/responsiveness/mobile-404.png) |![screenshot](documentation/responsiveness/mobile-500.png)| ![screenshot](documentation/responsiveness/mobile-403.png) | works as expected |
| Tablet DevTools (768px) | ![screenshot](documentation/responsiveness/tablet-new-entry.png)| ![screenshot](documentation/responsiveness/tablet-edit-house.png)  |![screenshot](documentation/responsiveness/tablet-change-password.png) | ![screenshot](documentation/responsiveness/tablet-manage-users.png) | ![screenshot](documentation/responsiveness/tablet-404.png) |![screenshot](documentation/responsiveness/tablet-500.png)| ![screenshot](documentation/responsiveness/tablet-403.png) | works as expected |
| Desktop |![screenshot](documentation/testing/browsers/chrome/chrome-new-house-1.png)  ![screenshot](documentation/testing/browsers/chrome/chrome-new-house-2.png)| ![screenshot](documentation/testing/browsers/chrome/chrome-edit-house-1.png) ![screenshot](documentation/testing/browsers/chrome/chrome-edit-house-2.png) |![screenshot](documentation/testing/browsers/chrome/chrome-change-password.png) | ![screenshot](documentation/testing/browsers/chrome/chrome-manage_users.png) | ![screenshot](documentation/testing/browsers/chrome/chrome-404.png) |![screenshot](documentation/testing/browsers/chrome/chrome-500.png)| ![screenshot](documentation/testing/browsers/chrome/chrome-403.png) | works as expected |
| Iphone13 (Own device) |![screenshot](documentation/responsiveness/iphone13-add-house.PNG)  ![screenshot](documentation/responsiveness/iphone13-add-house.PNG)| ![screenshot](documentation/responsiveness/iphone13-edit-house.PNG) ![screenshot](documentation/responsiveness/iphone13-edithouse-2.PNG) |![screenshot](documentation/responsiveness/iphone13-changepassword.PNG) | ![screenshot](documentation/responsiveness/iphone13-manage-users.PNG) | ![screenshot](documentation/responsiveness/iphone13-404.PNG) |![screenshot](documentation/responsiveness/iphone13-500.PNG)| ![screenshot](documentation/responsiveness/iphone13-403.PNG) | works as expected |


## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Landing | ![screenshot](documentation/testing/lighthouse/lighthouse-landing-mobile.png) | ![screenshot](documentation/testing/lighthouse/lighthouse-landing-desktop.png) | Initially warning on performance level due to image sizes too big. I have compressed the images now and the performance level have become better |
| Register | ![screenshot](documentation/testing/lighthouse/lighthouse-register-mobile.png) | ![screenshot](documentation/testing/lighthouse/lighthouse-register-desktop.png) | No issues |
| Login | ![screenshot](documentation/testing/lighthouse/lighthouse-login-mobile.png) | ![screenshot](documentation/testing/lighthouse/lighthouse-login-desktop.png) | Slow response time due to large images |
| Profile | ![screenshot](documentation/testing/lighthouse/lighthouse-profile-mobile.png) | ![screenshot](documentation/testing/lighthouse/lighthouse-profile-desktop.png) | Warnings on accessbility due to lack of name for button. Fix: added aria-label to fabourite button. Screenshots are the fixed version |
| House | ![screenshot](documentation/testing/lighthouse/lighthouse-house-mobile.png) ![screenshot](documentation/testing/lighthouse/lighthouse-house-mobile-fix.png)| ![screenshot](documentation/testing/lighthouse/lighthouse-house-desktop.png) ![screenshot](documentation/testing/lighthouse/lighthouse-house-desktop-fix.png) | Accessibility due to links and colour contrats. Secons screenshot is the fix after fixing colour contrasts |
| Contact | ![screenshot](documentation/testing/lighthouse/lighthouse-contact-mobile.png) | ![screenshot](documentation/testing/lighthouse/lighthouse-contact-desktop.png) | No Issues |
| Favourites | ![screenshot](documentation/testing/lighthouse/lighthouse-favourites-mobile.png) | ![screenshot](documentation/testing/lighthouse/lighthouse-favourites-desktop.png) | No issues |
| New Entry | ![screenshot](documentation/testing/lighthouse/lighthouse-add-house-desktop.png) | ![screenshot](documentation/testing/lighthouse/lighthouse-add-house-desktop.png) | Initial warnings on accessbility where some form elements did not have a form. Fix: Add aria-label to those form elements. the screenshots are the update fix version |
| Edit House | ![screenshot](documentation/testing/lighthouse/lighthouse-edit-house-mobile.png) | ![screenshot](documentation/testing/lighthouse/lighthouse-edit-house-desktop.png) | No Issues |
| Change Password | ![screenshot](documentation/testing/lighthouse/lighthouse-change-password-mobile.png) | ![screenshot](documentation/testing/lighthouse/lighthouse-change-password-desktop.png) | No issues |
| Manage Users | ![screenshot](documentation/testing/lighthouse/lighthouse-manage-users-mobile.png) | ![screenshot](documentation/testing/lighthouse/lighthouse-manage-users-desktop.png) | No issues |
| 404 | ![screenshot](documentation/testing/lighthouse/lighthouse-404-mobile.png) | ![screenshot](documentation/testing/lighthouse/lighthouse-404-desktop.png) | No Issues|
| 500 | ![screenshot](documentation/testing/lighthouse/lighthouse-500-mobile.png) | ![screenshot](documentation/testing/lighthouse/lighthouse-500-desktop.png) | No Iss8es |
| 403 | ![screenshot](documentation/testing/lighthouse/lighthouse-403-mobile.png) | ![screenshot](documentation/testing/lighthouse/lighthouse-403-desktop.png) | No Issues |

## Accessibility
I have used [wave](https://wave.webaim.org/) to ensure that the web application complies to accessibility. Only a few pages are included as the other pages are not accessible as login is required.

| Wave Link | Notes |
|-----------------|-----------------|
|[Landing Page](https://wave.webaim.org/report#/https://casa-quest-853d4c81f9b1.herokuapp.com/)| No errors, 0 contrast errors |
|[Contact](https://wave.webaim.org/report#/https://casa-quest-853d4c81f9b1.herokuapp.com/contact)|No errors, 0 contrast errors |
|[Login](https://wave.webaim.org/report#/https://casa-quest-853d4c81f9b1.herokuapp.com/login) | No errors, 0 contrast errors |
|[Register](https://wave.webaim.org/report#/https://casa-quest-853d4c81f9b1.herokuapp.com/register) | No errors, 0 contrast errors |


## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| New_house | | | | | |
| | Users cannot submit an empty form | Tested the form by submitting an empty form by removing the `required` if a bad users do so. | Form validation worked and an error message appeared | Test concluded and passed | ![screenshot](documentation/testing/defensive-programming/defensive-programming-form-validation-addhouse.png) |
| | Users cannot submit an image that is larger than 10mb to cloudinary | Tested the form by submitting an image that is 15mb | Form was submitted but a placeholder image was instead used and a flash message of error of 'uploading image' | Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-file-validation.gif) |
| | When users submit a validated form, user is redirected to the dashboard with house | Tested by completing the form and adding the house | The feature behaved as expected | Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-add-house.gif) |
| Edit_new_house | | | | | |
| | When user submits a validated form, user is redirected back to profile and a flash message appears to confirm update | Tested the form by submitting a validated form | Feature behaved as expected | Test concluded and passed | ![gic](documentation/testing/defensive-programming/defensive-programming-edit-house.gif) |
| | Users cannot submit an empty form |Tested the form by submitting an empty form by removing the `required` if a bad users do so.  | Form validation worked and an error message appeared | Test concluded and passed | ![screenshot](documentation/testing/defensive-programming/defensive-programming-edit-house.png) |
| | Users cannot submit an image that is larger than 10mb to cloudinary | Tested the form by submitting an image that is 15mb | Form was submitted but no change to the image was made | Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-file-validation-2.gif) |
| House | | | | | |
| | Users cannot submit an empty form |Tested the all the form by submitting an empty form by removing the `required` if a bad users do so.  | Form validation worked and an error message appeared | Test concluded and passed | ![screenshot](documentation/testing/defensive-programming/defensive-programming-house-1.png) ![screenshot](documentation/testing/defensive-programming/defensive-programming-house-2.png)|
| Manage Users | | | | | |
| | Users that is not 'systemadmin' will not be able to access manage users | Tested the feature by brute forcing the url | The feature behaved as expected and I was redirected to a 403 page | Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-manage-user-access.gif) |
| | Deleting a user should prompt a message afterwards that user have been deleted | Tested the feature by deleting a user | No message was shown | Fixed it by rearranging the flash message before the return statement | ![gif](documentation/testing/defensive-programming/defensive-programming-manage-users1.gif) |
| User Access | | | | | |
| | User should not be able to access other user's dashboard | Tested the feature by brute forcing the url | The feature behaved as expected and I was redirected back to profile | Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-no-access-to-other-profiles.gif) |
| | User should not be able to access other user's houses | Tested the feature by brute forcing the url | The feature behaved as expected and I was redirected back to profile | Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-no-access-to-other-houses.gif) |
| |Users cannot perform CRUD functionality while logged-out | Tested the feature by brute forcing the url while user is logged out | The feature behaved as expected and I was redirected back to logged in page | Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-no-access-if-not-logged-in.gif) |
| Index Page | | | | | |
| | If user has not logged in or registered, call out button should lead to register page | Tested the feature by doing clicking the button | The feature behaved as expected,| Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-call-outbtn-1.gif) |
| | If user is logged in, call out button should lead to profile | Tested the feature by doing clicking the button | The feature behaved as expected,| Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-call-outbtn2.gif) |
| House | | | | | |
| | If user edits an information that doesnt exist, user is redirected to a 404 page | Tested the feature updating before adding information | The feature behaved as expected,| Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-editing-info.gif) |
| Register | | | | | |
| | Submitting an empty form should lead to an flash message | Tested by manually removing the required fields and submitting the form with empty inputs | The feature behaved as expected,| Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-register3.gif) |
| | When all required field is met, user should be redirected to their dashboard | Tested by making an account | The feature behaved as expected,| Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-register.gif) |
| | If user does not meet the required fields | Tested by making not having the same password as the confirmation password | Error appeared that registration failed | Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-register2.gif) |
| Login | | | | | |
| | When all required field is met, user should be redirected to their dashboard | Tested by making an account | The feature behaved as expected,| Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-login.gif) |
| | If user does not meet the required fields| Tested by making submitting an empty form by removing `required` temporarily | Error appeared that "incorrect username/password" | Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-login2.gif) |
| Contact | | | | | |
| | When user makes a validated message, user is shown a thank you message and receives an auto-reply | Tested by making a validated message | The feature behaved as expected and received an email| Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-contact.gif) ![screenshot](documentation/testing/defensive-programming/defensive-programming-contact2.png) |
| Dashboard | | | | | |
| | When a user tries to delete a house, they would be prompted with a delete modal with a confirmation. If confirmed, House is deleted and user is redirected back to dashboard | Tested by clicking the 'x' button and the confirm button |The feature behaved as expected and a flash message appeared to alert that the house has been deleted| Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-dashboard.gif)  |
| | When a user clicks on the heart button, It would add the house to favourites. User is redirected to favourites | Tested by clicking the heart button |The feature behaved as expected and a flash message appeared to alert that the house has been added to the favourites| Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-favourites.gif)  |
| | When a user clicks on the view more button, they would be redirected to the house page |  Tested by clicking the 'view more' button |The feature behaved as expected |Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-view-more.gif)  |
| Favourite/Dashboard | | | | | |
| | When a user clicks on the solid heart button, It would remove the house to favourites. User is redirected back to dashboard | Tested by clicking the remove button |The feature behaved as expected and a flash message appeared to alert that the house has been removed from the favourites | Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-unfavourite.gif)  |
| House | | | | | |
| | Add button triggers a form modal | Tested by clicking all the add button |The feature behaved as expected | Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensuve-programming-add-info.gif)  |
| | All forms submitted when required field is met | Tested by submitting all forms |The feature behaved as expected | Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-add-info2.gif)  |
| Change Password | | | | | |
| | Submitting an empty form should show an error message| Tested by manually removing the required fields and submitting the form with empty inputs | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/testing/defensive-programming/defensive-programming-change-password1.png)  |
| | If the current password is incorrect or the new password and confirm password do not match, a flash message should be displayed.| Tested by entering an incorrect current password, followed by testing with a mismatched new password and confirm password.  | The feature behaved as expected | Test concluded and passed | ![screenshot](documentation/testing/defensive-programming/defensive-programming-change-password2.png)  |

| '404', '500', '403 pages | | | | | |
| | 'Home' button should redirect back to landing page | Tested by clicking all the home button| The feature behaved as expected | Test concluded and passed | ![gif](documentation/testing/defensive-programming/defensive-programming-404.gif)   ![gif](documentation/testing/defensive-programming/defensive-programming-500.gif)  ![gif](documentation/testing/defensive-programming/defensive-programming-403.gif)|




## User Story Testing


| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to see a clear logo, so that I can remember the brand. | ![screenshot](documentation/feature/feature-logo.png) |
| As a new site user, I would like to see a clear message of the web app, so that I can understand the web applicatioon well.| ![screenshot](documentation/feature/feature-callout.png)  ![screenshot](documentation/feature/feature-landing.png)|
| As a new site user, I would like to see navigation bar, so that I can easily navigate around the site. | ![screenshot](documentation/feature/feature-navigation.png) |
|  As a new site user, I would like to see a contact page, so that I can get in touch with the administrators of the application if I need help. | ![screenshot](documentation/feature/feature-contact.png) |
|  As a new site user, I would like to see social media icons so that I can reach out at the other sources.| ![screenshot](documentation/feature/feature-social-media-links.png) |
| As a returning site user, I would like to be able to register, so that I can have a personal account | ![screenshot](documentation/feature/feature-login.png) |
| As a returning site user, I would like to be able to make new entries of properties, so that I can keep a log of my properties. | ![screenshot](documentation/feature/feature-add-house.png) |
| As a returning site user, I would like to edit the information, so that I can have a more accurate information on the property. | ![screenshot](documentation/feature/feature-edit-house.png) |
| As a returning site user, I would like to delete the entry, so that I can eliminate properties that I'm not interested. | ![screenshot](documentation/feature/feature-delete-house.png) |
| As a returning site user, I would like to see a community of homebuyers, so that I can learn more about buying houses. | Future feature |
| As a returning site user, I would like to be able to make a post in the community of homebuyers, so that I can share my experience. | Future feature |
| As a returning site user, I would like to be able to make a comment in a post in the community of homebuyers, so that I can share my experience. | Future feature |
| As a returning site user, I would like to be able to see all the properties that I have added in one page so I can easily compare them | ![screenshot](documentation/feature/feature-dashboard.png)|
| As a returning site user, I would like to be able to mark some properties as my favourite so that I can keep track of my top choices | ![screenshot](documentation/feature/feature-favourite.png)|
| As a returning site user, I would like the ability to access a dedicated page for each house, allowing me to add and view detailed information specific to that property. | ![screenshot](documentation/feature/feature-house.png)|
| As a returning site user, I would like the ability to add information on that specific property | ![screenshot](documentation/feature/feature-add-details-button.png)|
| As a returning site user, I would like the ability to edit information on that specific property | ![screenshot](documentation/feature/feature-edit-button.png)|
| As a returning site user, I would like to be able to see a map of the location of the house so I can see the facilities nearby | ![screenshot](documentation/feature/feature-map.png)|
| As a returning site user, I would like to be able to log out to keep my session secure from who will be using the same device as me | ![screenshot](documentation/feature/feature-logout.png)|
| As a returning site user, I would like to be able to change my password, so that I can keep my account secure | ![screenshot](documentation/feature/change-password.png)|
| As a site administrator, I would like to keep connected with my users , so that they can report any user experience. | ![screenshot](documentation/feature/feature-contact.png) |
| As a site administrator, I should be able to view who created the house post so I can monitor the content and account| ![screenshot](documentation/feature/feature-createdby.png)|
| As a site administrator, I need to manage and view user accounts effectively to ensure control over the user base and monitor user activity.| ![screenshot](documentation/feature/feature-manage-users.png)|
| As a site administrator, I should be able to delete posts that is against the rules, so that I can ensure that the community is safe. | Future feature |
| As a site administrator, I should be able to delete users that is violating the rules, so that I can ensure that the community is safe. |  ![screenshot](documentation/feature/feature-deactivate-account.png) |
| As a site administrator, I should be able to direct users back to home if they have reached a page that is not found |  ![screenshot](documentation/feature/feature-404.png) |
| As a site administrator, I should be able to direct users back to home if they have reached a page that is forbidden to access. |  ![screenshot](documentation/feature/feature-403.png) |
| As a site administrator, I should be able to direct users back to home if the web application have reached an internal server error.|  ![screenshot](documentation/feature/feature-500.png) |


## Automated Testing

I have not conducted automated tests on my application because it was not suitable. Jest, the testing framework for JavaScript, does not handle event handlers effectively, and many of my JavaScript functions rely on external libraries such as Materialize.

I have researched methods for automated testing with Flask and Python, and found that using Flask-Pytest could be a viable option. However, the more I delved into it, the more complex and challenging it seemed.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

## User Feedback
This web application have been tried out by a few individuals. This is a feedback given by a user and the bugs have been fixed since then.

- " It looks really good, you've put a lot of work in. I encountered a few bugs that I thought I would let you know.
When I first registered it would not accept my name of < user's name > in the 'Name' field no matter how many times I clicked. It kept requesting to be in the correct format but didn't show me the format. It only accepts Name if it is typed lowercase with no spaces, almost like a username, yet I can use capitals in the username. It may need to be set explicitly in your code like you have for username and password.
The little arrow to the right of the house type options is not clickable to activate the dropdown menu. You can access the houses by clicking on the main field, but not by the arrow.
When I make a post for a house, I don't have to click 'Chain free' however when I update or edit the post it requires me to click 'Chain Free' to save the edited post, even if I don't want to. Could be a Boolean field that is triggered perhaps in the editing form"



## Bugs

- Tooltipped buttons posting data and making duplicate id.
    
    ![gif](documentation/bugs/bug02.gif)

    - To address this issue, I conducted research and found that the default type of a button is set to submit, as discussed on [Stack Overflow](https://stackoverflow.com/questions/41904199/whats-the-point-of-button-type-button). Consequently, I added `type="button"` to ensure that the button's behavior aligns with our intentions. Additionally, I implemented defensive measures to prevent duplicate ID post requests.

        ```python
            if house_data is None:
                mongo.db.houseChecks.insert_one(add_house_check_info)
                flash("Personal House Checks Added")
                return redirect(url_for("view_house", house_id=house_id))
            error_message = "House Check Information already exists"
            return render_template("500.html", error_message=error_message)
        ```
- Chain free checkboxes is mandatory for edit_new_house:
    ![screenshot](documentation/bugs/bug04.png)

    - To fix this issue, I removed the `required` attribute to the input.


- Name requirement for registration was not working properly
    ![screenshot](documentation/bugs/bug06.png)

    - To fix this issue, I went to [stackoverflow](https://stackoverflow.com/questions/19619428/html5-form-validation-pattern-alphanumeric-with-spaces) to find the most appropriate pattern for names and to accept space characters ''. I have change dthe required pattern to the recommended `pattern="[A-Za-z ]{5,32}` and removed `min` and `max` fields.


- Checkboxes are not being filled.
    ![gif](documentation/bugs/bug03.gif)

    - To resolve this issue, I discovered that I had duplicate IDs for checkbox elements, causing interference with their functionality. I rectified this by adjusting the IDs of the duplicate elements, resulting in the proper functioning of the checkboxes.

- Unable to log in.

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this issue, I realised that I have set the code to be:
        `"password": generate_password_hash("password")`

    - Therefore, I changed the password from a string back to a variable:

        `"password": generate_password_hash(password)`



- White space appearing below footer only on Firefox mobile device.
    
    ![screenshot](documentation/bugs/bug01.PNG)

    - The `top: 100vh;` property places the footer 100% down from the top of the viewport, positioning it at the bottom of the visible area. However, this did not make any changes.

        ```css
        body > footer {
            position: sticky;
            top: 100vh;
        }
        ```
    - Added padding-bottom to main to increase content and push footer down on smaller devices. It did not make any changes
        ```css
        main {
            padding-bottom: 10vh;
            }
        ```
    - **FIX** After researching more, I came across to a explanation of the error from [StackOverflow](https://stackoverflow.com/questions/14510899/white-space-after-the-footer-only-in-firefox-and-ie). It turns out that the firefox gives less bottom margin to headings. After testing the margins in my footer elements, This caused the elements to overflow whic gave me the idea to change the height of my footer to `min-height` of 30vh to make it more responsive.

- Label not being displayed with Materialize select and arrow not clickable.

    ![gif](documentation/bugs/bug08.gif)

    - Materialize has a bug in their select label as shown in their [issue#393](https://github.com/materializecss/materialize/issues/393) which causes the label to not display. Their svg carat is also not clickable. To fix this, this code was applied to `selectForm()` in script.js.

    ```js
        // This time out waits for materialize to initialize and then rearranges the location of the label in the Dom so it can be displayed. The svg also allows for a click trigger.
        setTimeout(() => {
            // Select each .select-wrapper.input-field and swap the label and ul if needed
            $('.select-wrapper.input-field').each(function() {
            const $parentDiv = $(this);

            // get the label and ul within the parent div
            const $label = $parentDiv.children('label');
            const $ul = $parentDiv.children('ul.select-dropdown');
            const $caret = $parentDiv.find('svg.caret');
            const $input = $parentDiv.find('input.select-dropdown');

            // move the label before the ul if it's not already
            if ($label.length && $ul.length && $label.next()[0] !== $ul[0]) {
                $label.insertBefore($ul);
            }

            // Ensure the caret triggers the dropdown
            if ($caret.length && $input.length) {
                $caret.on('click', function() {
                    $input.trigger('click');
                });
            }

            // Close the dropdown when an option is clicked
            $ul.children('li').on('click', function() {
                $input.trigger('click');
            });
            });
        }, 0);
    ```

- Editing house leads to a internal sever error

    ![gif](documentation/bugs/bug07.gif)

    - To resolve this issue, I have realised that I have misspelled `house['username']` to `house['usename']` . I have fixed the typo.
    ```python
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
    ```

- Flash is not showing when user is deleted
    ![gif](documentation/testing/defensive-programming/defensive-programming-manage-users1.gif)

    - To fix this, I had rearrange the flash statement before the return statement as it was initially after the return statement.
    
    *original code*

    ```python
    return redirect(url_for(
        "manage_users",  username=session["user"]
        ))
    flash("The user has been deleted")
    ```

    *Fixed code*
    ```python
    flash("The user has been deleted")
    return redirect(url_for(
        "manage_users",  username=session["user"]
        ))
    ```

## Unfixed Bugs

> [!NOTE]  
> There are no remaining bugs that I am aware of.
