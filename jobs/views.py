from django.shortcuts import render
from .models import Job

# Create your views here.
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})
