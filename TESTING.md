# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

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
| templates | profile.html | ![screenshot](documentation/validation/javascript-validation/js-validation-profile.png) |  No errors |
| templates | favourites.html | ![screenshot](documentation/validation/javascript-validation/js-validation-favourites.png) | No errors |
| templates | new_house.html | ![screenshot](documentation/validation/javascript-validation/js-validation-new-house.png) ![screenshot](documentation/validation/javascript-validation/js-hint-fix-new_house.png)| Undefined variable of `google` from google API. Unused variable of `formValidation()`. This function will be called in once form is submitted.  Unused variable of `initAutoComplete()`. This function initialises google's autocomplete API. Recommendations to use dot notation with my form validation function Fix: (second screenshot) I have changed it to dot notation as recommended. |
| templates | edit_new_house.html | ![screenshot](documentation/validation/javascript-validation/js-validation-edit-house.png) ![screenshot](documentation/validation/javascript-validation/js-hint-fix-edit_new_house.png) | Undefined variable of `google` from google API. Unused variable of `formValidation()`. This function will be called in once form is submitted.  Unused variable of `initAutoComplete()`. This function initialises google's autocomplete API. Recommendations to use dot notation with my form validation function Fix: (second screenshot) I have changed it to dot notation as recommended. |
           

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | app.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/mikavir/casa-quest/main/app.py) | ![screenshot](documentation/validation/python-validation/python-validation.png) | Some lines were too long to break due to being strings, Therefore, I added # noqa. |

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
| Iphone 13 (Own device) |![screenshot](documentation/responsiveness/iphone13-landing.PNG) ![screenshot](documentation/responsiveness/iphone13-landing-2.PNG) |![screenshot](documentation/responsiveness/iphone-13-register.PNG) ![screenshot](documentation/responsiveness/iphone13-register-2.PNG) |![screenshot](documentation/responsiveness/iphone-13-login.PNG) | ![screenshot](documentation/responsiveness/iphone13-dashboard-1.PNG) ![screenshot](documentation/responsiveness/iphone13-dashboard-2.PNG) ![screenshot](documentation/responsiveness/iphone13-dashboard-3.PNG) | ![screenshot](documentation/responsiveness/iphone13-house1.PNG)![screenshot](documentation/responsiveness/iphone13-house2.PNG) ![screenshot](documentation/responsiveness/iphone13-house3.PNG) | ![screenshot](documentation/responsiveness/iphone13-contact.PNG) | ![screenshot](documentation/responsiveness/iphone13-favourites1.PNG) ![screenshot](documentation/responsiveness/iphone13-favourites2.PNG) ![screenshot](documentation/responsiveness/iphone13-favourites3.PNG)| Flash can be obscured by logo |

| Browser | New House | Edit new house | Change Password  | Manage_users | 404 | 500 | 403 | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mobile DevTools (320px) |![screenshot](documentation/responsiveness/mobile-new-house.png)| ![screenshot](documentation/responsiveness/mobile-edit-house.png)  |![screenshot](documentation/responsiveness/mobile-change-password.png) | ![screenshot](documentation/responsiveness/mobile-manage-users.png) | ![screenshot](documentation/responsiveness/mobile-404.png) |![screenshot](documentation/responsiveness/mobile-500.png)| ![screenshot](documentation/responsiveness/mobile-403.png) | works as expected |
| Tablet DevTools (768px) | ![screenshot](documentation/responsiveness/tablet-new-entry.png)| ![screenshot](documentation/responsiveness/tablet-edit-house.png)  |![screenshot](documentation/responsiveness/tablet-change-password.png) | ![screenshot](documentation/responsiveness/tablet-manage-users.png) | ![screenshot](documentation/responsiveness/tablet-404.png) |![screenshot](documentation/responsiveness/tablet-500.png)| ![screenshot](documentation/responsiveness/tablet-403.png) | works as expected |
| Desktop |![screenshot](documentation/testing/browsers/chrome/chrome-new-house-1.png)  ![screenshot](documentation/testing/browsers/chrome/chrome-new-house-2.png)| ![screenshot](documentation/testing/browsers/chrome/chrome-edit-house-1.png) ![screenshot](documentation/testing/browsers/chrome/chrome-edit-house-2.png) |![screenshot](documentation/testing/browsers/chrome/chrome-change-password.png) | ![screenshot](documentation/testing/browsers/chrome/chrome-manage_users.png) | ![screenshot](documentation/testing/browsers/chrome/chrome-404.png) |![screenshot](documentation/testing/browsers/chrome/chrome-500.png)| ![screenshot](documentation/testing/browsers/chrome/chrome-403.png) | works as expected |
| Iphone13 (Own device) |![screenshot](documentation/responsiveness/iphone13-add-house.PNG)  ![screenshot](documentation/responsiveness/iphone13-add-house.PNG)| ![screenshot](documentation/responsiveness/iphone13-edit-house.PNG) ![screenshot](documentation/responsiveness/iphone13-edithouse-2.PNG) |![screenshot](documentation/responsiveness/iphone13-changepassword.PNG) | ![screenshot](documentation/responsiveness/iphone13-manage-users.PNG) | ![screenshot](documentation/responsiveness/iphone13-404.PNG) |![screenshot](documentation/responsiveness/iphone13-500.PNG)| ![screenshot](documentation/responsiveness/iphone13-403.PNG) | works as expected |

## Lighthouse Audit

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports.
Avoid testing the local version (especially if developing in Gitpod), as this can have knock-on effects of performance.

If you don't have Lighthouse in your Developer Tools,
it can be added as an [extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk).

Don't just test the home page (unless it's a single-page application).
Make sure to test the Lighthouse Audit results for all of your pages.

**IMPORTANT**: You must provide screenshots of the results, to "prove" that you've actually tested them.

Sample Lighthouse testing documentation:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/lighthouse/lighthouse-home-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-home-desktop.png) | Some minor warnings |
| About | ![screenshot](documentation/lighthouse/lighthouse-about-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-about-desktop.png) | Some minor warnings |
| Gallery | ![screenshot](documentation/lighthouse/lighthouse-gallery-mobile.png) | ![screenshot](documentation/lighthouse/lighthouse-gallery-desktop.png) | Slow response time due to large images |
| x | x | x | repeat for any other tested pages/sizes |

## Defensive Programming

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Defensive programming (defensive design) is extremely important!

When building projects that accept user inputs or forms, you should always test the level of security for each.
Examples of this could include (not limited to):

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

PP3 (Python-only):
- Users must enter a valid letter/word/string when prompted
- Users must choose from a specific list only

MS3 (Flask) | MS4/PP4/PP5 (Django):
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

You'll want to test all functionality on your application, whether it's a standard form,
or uses CRUD functionality for data manipulation on a database.
Make sure to include the `required` attribute on any form-fields that should be mandatory.
Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser).

You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable.
Ideally, tests cases should focus on each individual section of every page on the website.
Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine,
consider documenting tests on each element of the page
(ie. button clicks, input box validation, navigation links, etc.) by testing them in their happy flow,
and also the bad/exception flow, mentioning the expected and observed results,
and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature01.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature02.png) |
| About | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature03.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature04.png) |
| Gallery | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature05.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature06.png) |
| Contact | | | | | |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature behaved as expected, and it did Y | Test concluded and passed | ![screenshot](documentation/features/feature07.png) |
| | Feature is expected to do X when the user does Y | Tested the feature by doing Y | The feature did not respond to A, B, or C. | I did Z to the code because something was missing | ![screenshot](documentation/features/feature08.png) |
| repeat for all remaining pages | x | x | x | x | x |

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Another way of performing defensive testing is a simple Pass/Fail for each test.
The assessors prefer the above method, with the full test explained, but this is also acceptable in most cases.

When in doubt, use the above method instead, and delete the table below.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Gallery | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| Contact | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |
| repeat for all remaining pages | x | x | x | x |

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Repeat for all other tests, as applicable to your own site.
The aforementioned tests are just an example of a few different project scenarios.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

## User Story Testing

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature01.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature02.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature03.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature04.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature05.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/features/feature06.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature07.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature08.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/features/feature09.png) |
| repeat for all remaining user stories | x |

## Automated Testing

I have not conducted automated tests on my application because it was not suitable. Jest, the testing framework for JavaScript, does not handle event handlers effectively, and many of my JavaScript functions rely on external libraries such as Materialize.

I have researched methods for automated testing with Flask and Python, and found that using Flask-Pytest could be a viable option. However, the more I delved into it, the more complex and challenging it seemed.

I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

## Bugs

- White space appearing below footer only on Firefox mobile device.
    ![screenshot](documentation/bugs/bug01.png)

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

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bugs/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bugs/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bugs/bug04.png)

    - To fix this, I _____________________.

## Unfixed Bugs

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/bugs/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/bugs/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/bugs/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

> [!NOTE]  
> There are no remaining bugs that I am aware of.
