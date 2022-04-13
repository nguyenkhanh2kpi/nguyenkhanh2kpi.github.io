from distutils.command.upload import upload
from email.policy import default
from operator import mod
from statistics import mode
from turtle import title
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(default='', max_length=100)
    slug = models.SlugField(max_length=40)
    description = models.TextField(default='')
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.title}"


class Product(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    images = models.ImageField(upload_to = 'images', null  = False, default= None)

    def __str__(self):
        return f"{self.title}, {self.category}, {self.images}"

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default='')
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product},{self.title}"