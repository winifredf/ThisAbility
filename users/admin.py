from django.contrib import admin
from .models import User, Employer
from jobs.models import Job

# Register your models here.
admin.site.register(User)
admin.site.register(Employer)
admin.site.register(Job)
