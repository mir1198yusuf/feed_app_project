# Sample Feed app built in Django 


I created this project as a part of tech evaluation assignment for internship opportunity at a company.


*This sample application contains limited features and therefore can be updated to include new ones.*


## Brief description of project:

- It is basically like a mini-feeds app like LinkedIn or Facebook where user can create post and other users can see, comment, add reactions on it.


## Functionalities included in project:

1. User can create post including text and file of any type.
2. On Feed page user can see posts of all other users with details like created by, created on, post, total upvotes, total comments
3. If file in post is video/image it will be displayed along with the post using html <img> or <video> tag. For other types, just the url link will be displayed for downloading it.
4. User can filter the post using two filters : keyword in post or created_by user id
5. Login/ logout 
6. pagination at bottom  for post and comment page
7. User can upvote other posts. If already upvoted, the button will be hidden
8. User can comment on other posts

## Tools and technologies :

- Django - Python framework for web application
- HTML - for creating django webpage templates
- W3.CSS - CSS framework which is similar to Bootstrap
- python-decouple - Python library for separating secret setting parameters of project from source code
- dj_database_url - Python library to simplify database connection values
- PythonAnywhere - for deployment of django application, serving static & media files
- Sublime Text Editor - for writing code
- Git - for version control

## How to run this project :

0. Make sure you have Python 3, Git and virtualenv library installed
1. Create a directory - `feed_folder`
2. Inside `feed_folder`, create virtual environment using `virtualenv menv`
3. Activate virtualenv by going in `menv`>`Scripts`> run `activate`. `menv` is now activated in shell or cmd prompt.
4. Inside `feed_folder`, run `git clone https://github.com/mir1198yusuf/feed_app_project`
5. Navigate to newly created folder `feed_app_project`, run `pip install -r requirements.txt`
6. Generate Django secret key for project. Run `python generate_secret_key.py` and copy the output string
7. Paste it in `.env` file at `YOUR_SECRET_KEY`
8. Run `python manage.py migrate` to apply database migrations.
9. Create a user `python manage.py createsuperuser`
10. Finally start the project - `python manage.py runserver`
11. Go to the link displayed in shell/cmd prompt to view site. 

## Demo live site

This will be updated soon.


