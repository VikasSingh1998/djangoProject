from django.contrib import admin
#----------------------------------
#we have to import the Student model from models.py
from testapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','marks']

admin.site.register(Student,StudentAdmin)
# now we will create the superuser => py manage.py createsuperuser
# now run the server and go to admin page and see the table.
# ===================================================
