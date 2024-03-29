from django.contrib import admin
from testapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','marks','id'] #id is optional
    
admin.site.register(Student,StudentAdmin) 


