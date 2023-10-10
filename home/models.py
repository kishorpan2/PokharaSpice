from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import re
from datetime import date
# Create your models here.

class UserManager(models.Manager):
    def user_validator(self,post_data):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(post_data['username']) < 2:
            errors['username']='User name needs to be atleast 2 characters'
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email']='Check your email'
        if len(post_data['password']) < 8:
            errors['password']='Password needs to be atleast 8 characters'   
        return errors
    def login_validator(self,post_data):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email']='Check your email'
        if len(post_data['password']) < 8:
            errors['password']='Password needs to be  atleast 8 characters'   
        return errors

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified= models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    def __str__(self):
        return self.username