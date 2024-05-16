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

6. The best thing to do for the app, create a new urls.py file in your app folder so you can avoid creating a mess and make it more complicated. We will declare our routes in that file. Import these modules in this file:-
```
from django.urls import path # This is to configure paths or routes
from . import views # This will help us to receive views from the views.py file which exists in the same directory.

urlpatterns[
    path('path/',views.function, name="function") # This name will specify the name of the route(Not absolute path)
]
```
For the functions we will declare them in views.py file and we will call functions from this file to urls.py file in routes:-
```
def function(request):
    return (Whatever you wanna return)
```
7. Now we have to configure our app views to the main root views. In order to do that we need to import a module in our root urls.py file:-
```
from django.urls import include

# And the route will look something like this:-

urlpatterns = [
    path('admin/', admin.site.urls), # This is default, leave it the way it is
    path('path/', include('nameOfApp.urls'))
]
```
So after doing this our app urls routes will take of the routing.

8. Now to create templates or dynamic files, we will create a new folder in our root directory named: templates. We also have to configure this folder, by going in the main project folder in settings.py in TEMPLATES in  DIRS we will add template:-
```
TEMPLATES = [
    {
        'DIRS':[
            BASE_DIR / 'templates'
        ]
    }
]
```
Now we can go to our apps views and render templates

```
def function(request):
    return render(request, 'templateName.html') # This is how you will pass template in the view and these two are required paraemeters. 
```