from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import EmployerRegistrationForm
from django.contrib.auth import logout
from .forms import UserLoginForm
from django.contrib.auth.decorators import login_required
from .models import Job


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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users:profile')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'registration/login.html')

def register_employer(request):
    if request.method == 'POST':
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')  
    else:
        form = EmployerRegistrationForm()
    
    return render(request, 'registration/employer_register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users:profile')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    
    return render(request, 'registration/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('users:login')

def user_profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'users/profile.html', context)

