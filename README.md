# Python-Emailer
   Python project to send email when new forum posts made.
## Introduction and Motivation
   If you have an interest in something, there is probably a forum for it. For more specific things, such as NYC Job Exam results, there may only be a forum post that remains active for years. Staying up to date can be hard, as you generally have two options:

   1. Log in to recieve notifications. 
   
      -The requires an account, exposing your email, and assumes the forum supports notifications, be they email or account based.
   2. Periodically revist the forum. 

      -This can get tedious quickly, and if you forget the forum topic name can mean you lose a potentially valuable resource.

   To deal with this, this project will do two things.

   1. Using Scrapy, it will take in an array of forum threads and search for new posts. 
   2. Then, it will use smtplib to email the user whenever a new post is found. 
   
   The idea is that the script will run every X minutes, as defined by the user, defaulting to 30. This will only require that the user makes an email account, such as Gmail, for the script and have access to an always-on computer with internet access.

## Technologies Used

   Scrapy- a Python based web scraping tool.

   Smtplib- a Python library to send emails.

   Pipenv- a virtual environment handler that creates and managed virtualenv environments.

## Completed Tasks
   1. Scraper for forum post, and email processing established.

     Demo of Proof of Concept here: https://github.com/bmurdata/Python-Emailer/tree/Demo-POC?files=1
## To-Do and Improvements

   1. See Demo~Make scraper for specific forum posts.~
   2. See Demo ~Set up emailing process on new posts.~
   3. Set up database to store everything, rather than rely on hard-coded lists or text files.
   4. Allow user to reply back to email with new threads to follow, and instructions on what to check for.
   5. Intergrate app into a web framework(such as Django) to allow user to interact with it on phone or computer outside of terminal.
