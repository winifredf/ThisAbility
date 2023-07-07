from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    date = models.DateField()