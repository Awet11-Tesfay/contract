from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    starting_date = models.DateField(default='')