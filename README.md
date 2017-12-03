# notes_app
Notes App or To-Do list application built on Python Django Framework.

Use Cases->

1. User Signup.
2. Login control for the signed up users.
3. Create, Read, Update, Delete & Mark as complete Operations for Notes.
4. Share notes with multiple users present in the database.
5. Separate section of My Notes & Shared Notes.

To run this app you need to have Python and Django (using pip) installed

Install NodeJS dependencies
Run npm install to install all needed dependencies.

To install bower components (using node package manager): 
 npm install -g bower
 
To install semantic ui ->
  Install Gulp First-> 
  npm install -g gulp
  Then->
  npm install semantic-ui --save
  
Make migrations for databse(models setup) ->
python manage.py makemigrations
python manage.py migrate

Run the app ->
python manage.py runserver


