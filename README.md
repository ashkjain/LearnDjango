# LearnDjango

Step 1: Create Virtual Enviornment: python -m venv nameOfTheEnviornment
Step 2: Start Enviornment: venv/Scripts/activate
*To Turn of the Enviornment: Deactivate

# Run this command for windows to run the virtual envornment: Set-ExecutionPolicy RemoteSigned -Scope Process

Step 3: Install Django in the enviornment: pip install django
* Now you can use command 'django-admin' to see what commands are available for you to use.

1. To create a project write command: 'django-admin startproject projectName'. This will give you Django Starting Boilerplate code and settings for the project.

2. To run the project, get in the directory and use this command: 'python manage.py runserver'

3. To create an app you run the command: 'python manage.py startapp nameOfApp'

4. It is not automatically configured, so we will go to settings.py in main Project and in INSTALLED APPS we will create a connection: "'nameOfApp.apps.NameOfAppConfig',". We will put name of app and then in it, we have a file called apps.py, then in it based on the name of the application it will create a function which will use Title Case and config at the end of it. This is how we will establish a connection between the project and the app.

5. To create a url we need to go to urls.py and inside we will declare a new function:
```
def function(request):
    return (here you will return what you want)
```
Also you have to configure that, so in same file under urlpatters you will add your route:
```
path('path/to/config,function),
```

