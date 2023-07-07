from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Employer

# Create your views here.
def register_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

