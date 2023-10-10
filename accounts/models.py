from unicodedata import name
from django.db import models
from cart.models import *

# Create your models here.
class Shipping(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zipcode= models.CharField(max_length=10)
    country= models.CharField(max_length=20)
    phone_number=models.CharField(max_length=15)
    email= models.CharField(max_length=20)
