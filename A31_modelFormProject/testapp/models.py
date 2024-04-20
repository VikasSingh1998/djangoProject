from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    marks=models.IntegerField()
    #now do makemigrations and migrate.
    #now in admin.py we will go and do the required activity.
    
    