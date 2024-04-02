from django.contrib import admin
from testapp.models import PuneJobs,BengaluruJobs,HydJobs

# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phone'] 
admin.site.register(HydJobs,HydJobsAdmin)
# admin.site.register(model_name,class_name)

class BengaluruJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phone']
admin.site.register(BengaluruJobs,BengaluruJobsAdmin)


class PuneJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phone']  
admin.site.register(PuneJobs,PuneJobsAdmin)

#now we have to create the superuser ==> to access admin interface
# py manage.py createsuperuser ==> to create the super user
# http://127.0.0.1:8000/admin/ ==> login after giving id and password

#till now we have ==> models are ready and database table are ready
#now we will go for html==> to display the data
#for this we create the "templates" inside mai project folder and templates inside settings.py
#after templates ==> we have to create the static folder inside the main project and do the required activity inside settings.py
#NOW GO TO THE views.py and define the views
