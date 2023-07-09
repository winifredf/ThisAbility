from django.urls import path
from . import views
from.models import Job
from django.shortcuts import render

app_name = 'jobs'

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})