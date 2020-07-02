"""Assesment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from . import views
urlpatterns = [
    url('Home',views.Home ,name = "Home"),
    url('Profile', views.Profile, name = 'Profile'),
    url('Login', views.Login, name = 'login'),
    url('Signup', views.Signup, name = 'Signup'),
    url('Logout', views.Logout, name = 'logout'),
    url('posts', views.Posts, name = 'posts')
]
