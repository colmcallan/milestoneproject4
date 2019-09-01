# Build an Issue-Tracker (milestone project 4)

*Python and JavaScript Full Stack Project by [Colm Callan](https://github.com/colmcallan/milestoneproject4)*

*Django,  jQuery, CSS, font-Awesome, postgresql, heroku, aws*

## [Demo Here](https://milestone-project-4.herokuapp.com/)

---

---

## Overview

- Bugs No More is a Bug and  Ticket Creation site where users can create tickets which can then be voted on to increase the tickets rank to be worked on by the in-house developers.
- The main development features included the login system, bug feed and ticket creation editing and commenting on those tickets.
- The login system uses django AllAuth and allows users to sign up and in with a username and email address.
- The ticket/bugs section makes good use of pagination rendering to enhance to user experience.
- Editing Creating a ticket looks great.
- The design for the website's concept is based on the use of lots of primary colors, a clean interface 
- I hope you enjoy viewing and using this site as much as I have had building it (tough as it was)!

---

## Planning

1. Set User Stories
    - As a user ... I can see what the site is about and its purpose before signing up.
    - As a user ... I can view documentation to how the site works and any faq's.
    - As a user ... I have the option to sign up / sign in with a local profile or my github profile.
    - As a user ... If I forget my password, I can reset it.
    - As a user ... I can create / edit / update / delete my own tickets for a bug. 
    - As a user ... I can make a payment to up-vote a ticket.
    - As a user ... I can view and perform actions on the site on a mobile device comfortably. 

2. Functionality Specifications
    - create superuser and staff with ability to manage tables via the admin panel
    - create login system with django all-auth to allow signing up with github
    - create frontend pages to advertise the site to encourage users to sign up
    - create documentation to show users how to use the site its features.
    - create priority based queue tickets system tickets.
    - create ability for users to comment on tickets/bugs
    - create stripe checkout system for feature up-votes


---

## Content-Structure

To simplify user experience and encourage users to sign up! Most features of the website are behind the login experience. Each App is dedicated and for the most part self contained to the content that it provides. 


    
### Front-end pages:

*Unregistered users*
-  home
-  faq
-  contact
-  login 
-  tickets
-  bugs
-  register


*Registered users*
- home
- faq
- bugs comments 
- tickets comments
- profile
- change password


### Django apps used the create the site:  

- home [ home, faq ]
- accounts ( all-auth, profile, login, logout)
- tickets
- cart (session and context processor based)
- checkout ( stripe )
- bug 
- search
- project

---

## UX-Design

UX, Colors and Design

Throughout the project, I tried to keep the user/consumer at heart and look at it from the view of a real user when designing my site. I feel that I've achieved this well.

**Responsiveness** - My app is fully responsive; through the entire development and design process I continuously tested my app under Chrome Developer tools and testing various different screens sizes. By this I was able to perform periodic checks throughout the development process to ensure that my app was responsive across all device screens ranging from extra small to extra-large. Where needed I just used media queries to fix any resolution issues or responsiveness issues. I have built my app on the [Bootsrap4](https://getbootstrap.com/) a universally used grid system and using custom CSS to ensure full responsiveness. 

My app has been testing by friends and family members where needed notes were made and identified bugs were fixed. 

From doing this I have been able to confidently say that my app is fully responsiveness across all devices. 

---

#### Wireframes:

[Wireframes](https://github.com/colmcallan/milestoneproject4/tree/master/wireframes) 
All wireframes for mobile and desktop can be found here.

---

## Database

for the data of users/inputted tickets/bugs this was used with postgresql and django. 
---


#### Accounts / Profiles  

- used django all-auth to handle user login, signup, password resets ...
- you can sign in with either your email or username, both of which must be unique.
- ability to reset password and link sent to email address provided. [if smtp error populates from google, please contact me in the contact us link in the nav]


#### Bugs Page

- Here you will be able view recent users bugs raised on the site.

- You'll see actions such as:
    - A list of all bugs raised
    - The ability to view the bug and comment on it
    - Up-vote the bug to add it to your cart as a ticket to speed up the fixing process by us
    - Bug results are paginated for a better User Experience
    


#### Tickets

Where there's Code, there's a Bug!

- Tickets are the paid for service to speed up the process of having it fixed.
- You can view the most recently created tickets and paginate through the results.
- You can  the search bar will search through all tickets that are paid for.
- You can only vote on for a ticket once.
- Ticket results are paginated for a better User Experience


The tickets app makes use of django's class based views, namely `ListView, DetailView, CreateView, UpdateView` to do most of the heavy lifting for me. 

#### Comments

Comments are organised from the most the recent, just underneath the tickets details.

- Post a comment 
- If there are no comments yet, you'll see a placeholder indicating that there are none.



#### Single Page /  Create / Update Ticket/Bug

The Details, Create and Edit page share the same ticket details, preview, the difference being one is editable.

- If you are the owner you''ll have the ability to select edit ticket, other wise you'll see the vote or purchase buttons depending on if its a bug or a feature.
- If you are editing the ticket, you'll have the option to delete the ticket, you'll be required to confirm that you wish to delete it again.


#### Cart

You can support tickets by buying votes and adding the ticket to your cart. 

- You'll see an itemised list of the items you have chosen.
- You have the option to purchase multiple votes, both single and double. Each item will be a separate item, this is a chosen design.
- You'll see an itemised list of the items you have chosen, the votes and cost of that item.
-You have the ability to remove any items for your cart by selecting the remove item button and clicking the update cart button.
- An updated total price and item list will then be revised.
- As you click buy votes, you'll see your cart item number increase.
- Items will stay in your cart until you logout.

Ive followed the CI videos partly on this one for creating the context processor which makes for example a cart_items variable available throughout the site, in conjunction with session variables.


#### Payments / Stripe

- You'll be able to review your basket once more and see the final charges.
- I have used Stripe own "Elements" code for taking and validating your cards details from their example on the official website, this does a great job and looks great.
- Upon successful payment, you'll be notified and brought to a success screen where you can then continue to another area of of site.
- if the payment has failed, you will be prompted to try again.

One of the great reasons to use Stripe is not asking the customer for all their details, in a lot of cases its necessary, but I dont see any good reason for this site, so I have left that out by design.
No card details are stored as Stripes JavaScript generated a token to be used for the charge.

#### Contact Us

- A simple use of the mailto service opens the users default mail address. 

---

## Technologies

> *Python, Django, Jinja, Django AllAuth, Postgres, Sqlite3, JavaScript, JQuery,  CSS, Semantic UI, Boostrap4, Fontawesome 5, Git, Heroku*  
 
- Python  
https://docs.python.org/3/  
Used as the backend language  

- Django   
https://www.djangoproject.com/   
Used as the main framwework to create, serve, and interact with the application. 


- Django's Jinja   
http://jinja.pocoo.org/  
Used for the html templates, make good use of partials, template tags and filters. 

- Django AllAuth  
https://django-allauth.readthedocs.io  
Used to manage the user auth model, including social authentication and user management.

- Postgres - Sqlite3  
https://www.postgresql.org/
Sqlite3 was used in Development, Postgres is used on the Heroku deployed application.

- Pycharm  
https://www.jetbrains.com/pycharm/  
Pycharm was used to develop the project and came in really useful for its built in tools including linting, code suggestions, error checking and viewing the sqlite database.

- JavaScript  
https://www.ecma-international.org/   
JavaScript was used extensively for making request to the django backend for query data, as well as DOM manipulation. Provideing a good user experience to a lot of the application.  


- CSS  
http://www.w3.org/Style/CSS/members    

- JQuery  
https://jquery.com/    
JQuery is a requiremnet of some of the pages. 

- Stripe  
https://stripe.com/ie  
Stripe is used as the payment processor for charging credit or debit cards, only the card number is used.

- WhiteNoise  
http://whitenoise.evans.io/en/stable/   
WhiteNoise is used to serve the staticfiles of application when its live on the Heroku Server


---

## Testing

####  Automated written tests

Admittedly, I found this the biggest challenge of writing the project, perhaps as I had left it until the end of the project I found it more difficult to test, and on hindsight and the future, I think I would be better served doing the testing as I go along.

I have used django built in `TestCase` for testing, and I going app by app, tested the views, forms and models associated with each app. Using django allauth here proved an extra challenge as well as having used so many foreign keys and manytomany fields. The pattern generally followed:
 - I believe most tests are noted in each app and all passed.



**Browser compatibility** 


My app will be fully functional across all major modern browsers. I have tested my app on the following browsers.

- [Chrome](https://www.google.com/chrome/)
- [Firefox](https://www.mozilla.org/en-GB/firefox/new/)
- [Opera](https://www.opera.com/)
- [IE Edge](https://www.microsoft.com/en-gb/windows/microsoft-edge)
- [IE](https://www.microsoft.com/en-gb/windows/microsoft-edge)
- [Safari](https://support.apple.com/en_GB/downloads/safari)
- [Chrome Mobile](https://chrome.en.softonic.com/)

---

## Resource Sites Used
- [Edam](https://developer.edamam.com/edamam-docs-recipe-api)
- [Bootsrap4 Docs](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
- [Fontawesome Icons](https://fontawesome.com/)
- [Flask Docs](http://flask.pocoo.org/docs/1.0/)
- [Mongo Docs](https://docs.mongodb.com/)
- [Slack](https://slack.com/intl/en-gb/)
- [Google](https://google.com/)
- [YouTube](https://www.youtube.com/)

---

### HTML & CSS
All my HTML and CSS is valid, checked with the following validators

- [HTML Validator](https://validator.w3.org/)
-  [CSS Validator](https://jigsaw.w3.org/css-validator/)

####  User testing

As always, I have asked multiple friends, and other students from the course to test the website on their devices and received positive feedback  on their side of things on errors, indicating that there was not too many issues to be found. I am satisfied with the outcome.

### NOTED BUG TO BE FIXED 
When a logged in users tries to view a single bug it returns a reversematch error. This is now resolved and returns no errors. There are no broken links on this site.
---


---

## Deployment 

Getting my application ready for deployment consisted of the following: - 
1. Removing all my hard-coded environment variables to project my keys and secrets. These were placed in the heroku Config Vars for production.
2. Ensuring the applications requirements.txt is up-to-date with all the latest packages installed for my app being noted on this file. 
	**The command to update requirements**
		```
		pip3 freeze > requirements.txt
		```
3. Set up the Procfile - *A Procfile is required by Heroku in order to tell the service worker what command to run for my application to start.*
4. Set Flask's debugging to False.
5. Push all my latest production ready code to GitHub ready for deployment via Heroku's GitHub function where you can deploy from GitHub the production ready app.
6. IF using AWS cloud9, uninstall all requirements in the requirements.txt file and reinstall the following;
    1. `boto3`
	2. `botocore`
	3. `certifi`
	4. `chardet`
	5. `coverage`
	6. `Django`
	7. `django-forms-bootstrap`
	8. `django-storages`
	9. `docutils`
	10. `gunicorn`
	11. `idna`
	12. `jmespath`
	13. `psycopg2`
	14. `python-dateutil`
	15. `pytz`
	16. `requests`
	17. `s3transfer`
	18. `six`
	19. `stripe`
	20. `urllib3`


**Upon successful deployment Heroku will give you the URL that is hosted your app**

*Upon unsuccessful deployment Heroku will log the cause of the error and this is view able in the 'view log' section on the Heroku website. Here you will find a detailed report of what has cause your application not to be deployed successfully. *


#### Setting the project up in a local development environment



**Tools you may need:**  

Python 3 installed on your machine: https://www.python.org/downloads/   
PIP installed on your machine: https://pip.pypa.io/en/stable/installing/    
Git installed on your machine: https://gist.github.com/derhuerst/1b15ff4652a867391f03    
A text editor such as Pycharm https://www.jetbrains.com/pycharm/     
Or  Visual Studio Code https://code.visualstudio.com/  

**Instructions**

###### Setting up the project files  

- Click the download zip button on the github repository or open a terminal and enter `git clone`https://github.com/colmcallan/milestoneproject4
- if possible open a terminal session in the unzip folder or `cd` to the correct location
- If needed, Upgrade pip locally by `pip install --upgrade pip`.
** Note: You'll need to set up an account at Stripe to get your personal api keys**
- Once that has been done, you may `cd` into the `src` folder and run `manage.py migrate`
- Followed by `manage.py createsuperuser`, and follows the prompts in the terminal.
- launch the application with `manage.py ruunserver`
- The application should now be launch-able, but not quite fully functional just yet.    



---
### Things that could be improve if had more time
- Allow users to choose an avatar for their profile
- Include data charts of Bugs/Tickets by upvotes

## Credits & Acknowledgments 
Credit is due to the following names. I would like to thank each and every one who has helped or contributed to my project in any way. Please see list of names below:

- Mentor **Guido Cecilio Garcia**
- Youtuber **Pretty Printed**
- Friends who helped functionality and code review **Wesley Redmond**, **Conor Fitzsimons**


#### Thanks  

Stack Overflow was an unbelievably source of information for this projects and my mentor and the tutor support

