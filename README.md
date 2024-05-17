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

9. Now we are able to render pages, we can now use template engine to create some dynamic content without calling the same information again and again. For example: In an application we have a navbar, instead of calling it again and again we might just create a main.html file and put boilerplate code in it, and work just call it inside of our other pages. Create three files: main.html, home.html, contact.html, navbar.html.

navbar.html
```
<nav>
    <a href="/">Home</a>
    <a href="/contact">Contact</a>
</nav>
```
main.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>StudyBud</title>
</head>
<body>

    {% include 'navbar.html' %}

    {% block content %}

    {% endblock %}
</body>
</html>
```
home.html
```
{% extends 'main.html' %}
{% block content %}
<h1> This is the home page </h1>
{% endblock content %}
```
contact.html
```
{% extends 'main.html' %}
{% block content %}
<h1> This is the contact page </h1>
{% endblock content %}
```
So, in this example we created a block inside main.html and before block we included navbar.html. When we work on another pages we just have to extend the main.html and but all the html content inside the block content, this is being done by Django Template Engine, and this will help to create dynamic content.

10. We can pass in variables inside our routes and we can use those variables inside the template they are reffereing to. For example we have one route home and we are passing list inside and then using it, and iterating it:

views.py
```
learn = [
    {'chapter':1, 'name':'Basic Python'},
    {'chapter':2, 'name':'Python with OOP'},
    {'chapter':3, 'name':'Python Backend with Django'},
]
def home(request):
    context = {'books':learn}
    return render(request, 'home.html',context)
```
home.html
```
{% for book in books %}

<div>
    <h2>Book Id: {{book.chapter}} -- Book Name: {{book.name}}</h2>
</div>

{% endfor %}
```
This templating will allow to use the variable which is passed as 3rd argumnent, and can be used inside the template using for loop. *Make sure to end the for loop, in templating engine you have to end certain logical conditions.