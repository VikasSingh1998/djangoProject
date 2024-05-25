from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    dept=models.CharField(max_length=50)
    date=models.DateField()

# we have to register this model into the admin.py
# we have to create the superuser. ==> py manage.py createsuperuser






