from django.shortcuts import render
from testapp.models import PuneJobs,BengaluruJobs,HydJobs
#we have to import the models classes from models.py to get the correspondig data

# Create your views here.
#we have one homepage form where we will give the link to other page, so for page we have to define the views
def homepage_view(request):
    return(request,'testapp/index.html') #index.html is homepage name

def hydjobs_view(request):
    # jobs_list = HydJobs.objects.all()  #to get all the HydJobs present in the models.py
    jobs_list=[]
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',context=my_dict)

# home(index).html contains ==> hydJobs, BengaluruJobs, puneJobd
#after clicking on the hydjobs ==> we hve to move to the hydjobs.html so we have to give this link inside render()
#hydjobs.html ==> we have to create inside templates/testapp

