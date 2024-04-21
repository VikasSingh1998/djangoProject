from django.db import models

# Create your models here.
# first we will create the table.
class Movie(models.Model):
    rdate=models.DateField()
    moviename = models.CharField(max_length=30)
    hero=models.CharField(max_length=30)
    heroine=models.CharField(max_length=30)
    rating=models.IntegerField()
    
    
#once the model is ready-=> do the makemigrations and migrate
# now we have to check whether the table got created or not 
# ==> we have to register the admin in the admin interface.
# ==> create the superuser-> py manage.py createsuperuser
# once the superuser ans password(vikas123,vikas123), is created, then  run the server.
# py manage.py runserver
# vist ==> ..../admin page  ==> but before this we have to register this model inside the admin.py
# //================================================================
# we have done index pagee and showmovies to display the movies.
# ------------------------------
# Now we will do the add movies page.
# for this we will create the form to take the input from the user. 
# we will save the input into the database.
# we will create the file => forms.py


