from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    abilities = models.CharField(max_length=255)