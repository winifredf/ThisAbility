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



