from django.contrib import admin
from testapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','subject','dept','date']
    
admin.site.register(Student,StudentAdmin)
    
