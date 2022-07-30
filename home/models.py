from distutils.command.upload import upload
from email.policy import default
from operator import mod
from turtle import xcor
from unicodedata import name
from django.db import models

# Create your models here
class Contact(models.Model):
    name = models.CharField(max_length=122)   
    email = models.CharField(max_length=122)
    Phone =models.CharField(max_length=12)
    text=models.TextField()
    def __str__(self):
        return self.name

class Product(models.Model):
    Product_id=models.CharField(max_length=50)
    Product_name=models.CharField(max_length=50)
    Product_price=models.IntegerField(default=0)
    Product_category = models.CharField(max_length=50)
    Product_desc=models.CharField(max_length=1000)
    Product_image=models.ImageField(upload_to='home/images',default="")

    def __str__(self):
        return self.Product_name
