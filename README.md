# Django Boilerplate

1. git clone git_url
2. cd name_of_project
3. python3.8 -m venv venv
4. source venv/bin/activate
5. pip install -r requirements.txt
6. open your `settings.py` file and edit the `DATABASES` `NAME` and 'USER' accordingly.
7. create the database you just named in the `settings.py` file. `createdb nameofdb`
8. python manage.py migrate
9. python manage.py createsuperuser
9. python manage.py runserver_plus
