from django.db import models

# Create your models here.
class HydJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.BigIntegerField()

class BengaluruJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.BigIntegerField()

class PuneJobs(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.BigIntegerField()

#Here we have create 3 models==> 3 tables
# In Django, a model is a subclass of the django.db.models.Model class 
# Each model represents a single table in the database, where each field of the model corresponds to a column in that table.

#we have to use the database like oracle,mysql, sqlite(default) etc.
#now do==> py manage.py makemigrations and migrate
#table created ==> classname_modelname
#testapp_punejobs(only lowercase) will be created.

#I want to see these tables into the admin interface
#so we have to write code into the admin.py
#by using the faker module we can insert the data into db, but i am ignoring the concept.

