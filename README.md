# Django-Form
# Django-Message Board

 This is a Django based contact form, which has a simple form which is connected to a SQL-Lite database and has a feature to be added elements such as a Nav-bar and stuffs. It has an admin Interface to view the entires in the DB.




To run the project:

-> Navigate into the workshop folder.
-> python manage.py runserver.
          This will start a local develpment server, which has this project running. For ex http://127.0.0.1:8000/
-> Once the response is submitted, to view the response, navigate to http://127.0.0.1:8000/admin/ and use admin:admin as the username and password.
-> Inside the contact column, see the response sumbitted.
-> To access the database, see the SQL Lite DB file inside the directory.

## UPDATE:(SEPT-7-22)
->Now you can display content in the MESSAGE-BOARD, while updating the content in the admin panel, withou touching the code.


## Before running the programme, delete the db.sqlite3.
## Run these commands in the terminal.  
### python manage.py makemigrations
### python manage.py migrate
### python manage.py createsuperuser
### python manage.py runserver


Then create a super user with your desired credentials.


NOTE: Not a production grade!
