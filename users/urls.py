from django.urls import path
from . import views
from .forms import EmployerRegistrationForm

app_name = 'users'

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('register/employer/', views.register_employer, name='employer_register'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
    path('profile/', views.user_profile, name='profile'),
    


]