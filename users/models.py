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

    def __str__(self):
        return self.name

class Employer(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=210)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employers')

    def __str__(self):
        return self.name
    
    