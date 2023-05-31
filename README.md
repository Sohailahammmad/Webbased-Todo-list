# Webbased-Todo-list
Create a Django app and models

Create a new Django project (if not already created) using the command: django-admin startproject todolist_app.

Create a new Django app within the project using the command: python manage.py startapp todolist.

Open the models.py file in the todolist app directory and define the models as per the requirements. 

Run database migrations using the command: python manage.py makemigrations followed by python manage.py migrate.
Step 2: Enable Django Admin interface

Open the admin.py file in the todolist app directory and register the TodoItem model to be displayed in the Django Admin interface.
Start the Django development server using the command: python manage.py runserver and access the admin interface at http://localhost:8000/admin.

Log in as a superuser (create one using python manage.py createsuperuser if not already done) and verify that the TodoItem model is displayed in the admin interface.

Step 3: Create REST APIs using DRF

Install Django Rest Framework using the command: pip install djangorestframework.

Open the urls.py file in the project directory (todolist_app) and add the necessary URL patterns for the API endpoints.

Create a new file serializers.py in the todolist app directory and define the serializer for the TodoItem model
Create and share a Postman collection

Create a new Postman collection and add the following requests corresponding to the API endpoints:

Create a todo item (POST)

Read one todo item (GET)

Read all todo items (GET)

Update a todo item (PUT or PATCH)

Delete a todo item (DELETE)

Share the Postman collection by exporting it as a JSON file or providing a shareable link.

Step 5: Enable basic authentication for APIs

Install Django Rest Framework's authentication package using the command: pip install djangorestframework-simplejwt.

Configure Django settings to include the authentication classes. Open the settings.py file in the project directory (todolist_app) and modify the REST_FRAMEWORK

Generate a secret key for JWT authentication by running the command: python manage.py shell and executing code.










