DJango Project
Installation and Configuration Process

(Python Installation)

Commands:

-   pip install pipenv
-   pipenv shell
-   pipenv install django
-   pipenv install djangorestframework
-   django-admin startproject <project_name> .

*   sudo apt-get install python3-dev default-libmysqlclient-dev build-essential

-   pipenv install mysqlclient

*   sudo apt-get install mysql-server

-   sudo mysql -u root -p
    -   (CREATE DATABASE demo_db;)
    -   (USE demo_db;)
    -   (ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';)
-   python manage.py startapp <app_name>
-   python manage.py makemigrations <model_name>
-   python manage.py migrate
-   python manage.py runserver <port>

CRUD PROCESS:

-   Create Applications
-   Create Models
-   Create Serializers File
-   Configure DB on settings
-   Run migration commands
-   Create CRUD methods on Views
-   Config urls on app folder
-   Config urls on main folder
-   Add CORS settings
-   Test Methods on Postman

CORS settings for localhost (settings.py):

-   Add cors application
-   Add cors middleware
-   Add cors Whitelist
-   Reference: https://github.com/UskoKruM/django_mysql_api/blob/master/Proyecto_API/Proyecto_API/settings.py
