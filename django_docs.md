# INTIALIZING DJANGO

django-admin startproject app

# GO TO THE CREATED DIR

app backend

# CREATE DIR INSIDE THE CREATED BACKEND DIR

python manage.py startapp backend



#  AFTER YOU CREATE A DIR IN MAIN DIR YOU NEED TO INCLUDE THE DIRECTORY OF BACKEND OR THE DIRECTORY YOU MAKE INSIDE 

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend'
]



# AFTER YOU INCLUDE THE PATH OF BACKEND DIR, YOU NEED TO CREATE A urls.py FILE INSIDE THE BACKEND AND PUT THIS

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]


# AFTER YOU CREATE URL FILE IN BACKEND DIR  INCLUDE THE URL INSIDE THE BACKEND(MAIN) urls.py file AND INCLIDE THE PATH 

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.urls')),
]



# AFTER THE CREATE A HTTPRESPONSE TO CHEKC IF ITS WORK

from django.shortcuts import render, HttpResponse

 
def home(request):
    return HttpResponse(f"Hello world {request}")



# AFTER THAT IS MAKE SURE YOUR MACHINE IP IS ALLOW TO HOST

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'kvurl681-a4hj9gzb-gan84bkj008p.ac4-preview.marscode.dev',
]

# AFTER THAT IS RUN THE FILE

python manage.py runserver


# IF YOU SUCEFULLY RUN THE SERVER MAKE A TEMPLATES DIR AND TEST MAKE BASE AND HOME.HTML




# THIS IS THE BASE

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>
      {% block title %}
        Django App
      {% endblock %}
    </title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"  rel="stylesheet" />
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">My Django App</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">About</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Contact</a>
          </li>
        </ul>
      </div>
    </nav>
    <div class="container">{% block content %} {% endblock %}</div>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.bundle.min.js" ></script>
  </body>
</html>



# THIS IS THE HOME THE LOGIC OF THIS IS TO EXTEND OR INHERIT THE PROPERTY OF BASE.HTML

{% extends "base.html" %} {% block title %} Home Page {% endblock %}
{% block content %}
<p>THIS IS THE HOME PAGE</p>
{% endblock %}
