from django.urls import path
from . import views
from.models import Job
from django.shortcuts import render

app_name = 'jobs'

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('<int:job_id>/', views.job_detail, name='job_detail'),
]