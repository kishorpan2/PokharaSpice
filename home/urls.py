from unicodedata import name
from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('', home , name="home"),
    path('register',register_attempt, name="register_attempt"),
    path('login', login_attempt, name="login_attempt"),
    path('token' , token_send , name="token_send")
]
