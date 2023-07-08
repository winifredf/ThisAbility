from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Employer
from django.shortcuts import redirect

# Create your views here.
def register_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(username=username, password=password)
        user.save()

        return redirect('users:login')
    
    return render(request, 'registration/register.html')

def login_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users:profile')
        else:
            messages.error(request, 'Invalid username and/or password.')
    return render(request, 'registration/login.html')