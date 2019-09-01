# Build an Issue-Tracker (milestone project 4)

*Python and JavaScript Full Stack Project by [Colm Callan](https://github.com/colmcallan/milestoneproject4)*

*Django,  jQuery, CSS, font-Awesome*

---

---

## Overview

- Bugs No More is a Bug and Feature Ticket Creation site where users can create tickets which can then be voted on to increase the tickets rank to be worked on by the in-house developers.
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
    - As a user ... I can delete my account and all tickets associated with it.
    - As a user ... I can see charts indicating the highest voted and most tended to bugs and features.
    - As a user ... I can see an activity feed of recent actions by users site wide.
    - As a user ... I can create / edit / update / delete my own tickets for a bug / feature. 
    - As a user ... I can create / edit / update / delete my own comments for a bug / feature.
    - As a user ... I can add / remove my own up-vote to another users bug/feature.
    - As a user ... I can make a payment to up-vote a feature which will be reflected in the sites most tended to charts.
    - As a user ... I can view and perform actions on the site on a mobile device comfortably. 

2. Functionality Specifications
    - create superuser and staff with ability to manage tables via the admin panel
    - create login system with django all-auth to allow signing up with github
    - create frontend pages to advertise the site to encourage users to sign up
    - create documentation to show users how to use the site its features.
    - create charts showing bugs / features with highest up-votes (daily, weekly , monthly)
    - create priority based queue tickets system for bugs and features
    - create ability for users to comment on tickets
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

- home [ home, faq, profile ]
- accounts ( all-auth  )
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

#### Wireframes:

[Wireframes](https://github.com/colmcallan/milestoneproject4/tree/master/wireframes) 
All wireframes for mobile and desktop can be found here.

---

## Database

for the data of users/inputted tickets/bugs this was used with postgresql and django. 
---

## Features

#### Accounts / Profiles  

- used django all-auth to handle user login, signup, password resets ...
- you can sign in with either your email or username, both of which must be unique.
- ability to reset password and link sent to email address provided. 


#### Bugs Page

- Here you will be able view recent users bugs raised on the site.

- You'll see actions such as:
    - A list of all bugs raised
    - The ability to view the bug and comment on it
    - up-vote the bug to add it to your cart as a ticket to speed up the fixing process by us
    


#### Tickets

Where there's Code, there's a Bug!

- Tickets are the paid for service to speed up the process of having it fixed.
- You can view the most recently created tickets and paginate through the results.
- You can  the search bar will search through all tickets that are paid for.
- You can use filter will filter your results, you can also search and filter results together.
- If your search become to narrow, you can the reset all button to start again.
- You can only vote on for a bug once.


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

You can support bugs by buying votes and adding the ticket to your cart. 

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


#### Browser Testing

While my main choice of browser for development is google chrome, I regularly checked the performance on firefox and opera browsers. Making use of browser resizing and dev tools device toolbars on each browser to test responsiveness and how how the grid, fonts and media queries were performing and the consistency between each. Adjusting to find a happy medium for all three.

After I had test deployed the site to heroku I was able to see the real life versions which I was able to test on a android phone, amazon fire tablet and at different orientations. Unfortunately, I have no safari devices which I am able test on.

The two css libraries in use, semantic ui and beardcss, and the few media queries I wrote were quite sufficient and while there was a few times that trying to override the css styles of those libraries become difficult I was able to get it fixed without any real issues. 

####  User testing

As always, I have asked multiple friends, and other students from the course to test the website on their devices and received positive feedback  on their side of things on errors, indicating that there was not too many issues to be found. I am satisfied with the outcome.

### NOTED BUG TO BE FIXED 
When a logged in users tries to view a single bug it returns a reversematch error. This is noted and a high priority to fix (with the time left to submit my project, I have to submit without being resolved. however it works for a user not logged in. that was the only bug raised and noted)

---

## GIT

Git has been used extensively through the entire project build. I have regularly made commits at each meaningful stage and also at regular intervals to save me work.

I have created different branches to develop important apps such as the tickets app and the comments app. On completion, I would then merge the branch into the master branch and push to github.

I have made use of the .gitignore file to exclude my unneeded files such as pycache, venv and pycharm files and folders.

Unsure of what to exclude for django I referenced gitignore.io for a generic django template to help me decide what to exclude from pushing to github. 

---

## Deployment

#### Deployment to Heroku


My deployment process was as follows:
- Installed `whitenoise` and configured my settings file for it, performed a test with debug off and collected staticfiles to ensure it worked and the 404, 500 pages work as expected.
- Installed `heroku-cli` on my machine, logged in and added the heroku remote to git.
- On heroku I added the Postgres add-on .   
- Installed pillow, dj-database-url and gunicorn.
- Created a Procfile and requirements.txt
- Further set-up my settings (manage.py) to read from the env vars on Heroku which I set it.
- Pushed to heroku and when the build process had successfully finished, ran migrations and created a superuser.
- The application was now fully deployed and ready for the database to be populated. 

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
Next your need to install a virtual environment for the python interpreter, I recommend using pythons built in virtual environment. Enter the command `python -m venv venv` . NOTE: Your python command may differ, such as `python3` or `py`.
- Activate the `venv` with the command `source venv/bin/activate`, again this may differ depending on your operating system, please check https://docs.python.org/3/library/venv.html for further instructions.
- If needed, Upgrade pip locally by `pip install --upgrade pip`.
- Install all required modules with the command `pip -r requirements.txt`.
- In the `src/project/settings/` folder create a new file called `local.py`. Copy all the values from `production.py` to this file. You'll now need to change the values of all variables to your personal values.
** Note: You'll need to set up an account at Stripe and Mailgun to get your personal api keys**
- Once that has been done, you may `cd` into the `src` folder and run `./manage.py migrate`
- Followed by `./manage.py createsuperuser`, and follows the prompts in the terminal.
- launch the application with `./manage.py ruunserver`
- The application should now be launch-able, but not quite fully functional just yet.    



---

## Credits

Aside from the aforementioned below, all code is my own work, referencing and making use of official documentation when needed.


#### Thanks  

Stack Overflow was an unbelievably source of information for this projects and my mentor and the tutor support

