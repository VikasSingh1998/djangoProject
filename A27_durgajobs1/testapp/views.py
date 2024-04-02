from django.shortcuts import render
from testapp.models import PuneJobs,BengaluruJobs,HydJobs
#we have to import the models classes from models.py to get the correspondig data

# Create your views here.
#we have one homepage form where we will give the link to other page, so for page we have to define the views
def index_view(request):
    return render(request, 'testapp/index.html') #index.html is homepage name

def hydjobs_view(request):
    jobs_list = HydJobs.objects.all()  #to get all the HydJobs present in the models.py
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',context=my_dict)

def bengalurujobs_view(request):
    jobs_list = BengaluruJobs.objects.all()  #to get all the BengaluruJobs present in the models.py
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/bglrjobs.html',context=my_dict)

def punejobs_view(request):
    jobs_list = PuneJobs.objects.all()  #to get all the PuneJobs present in the models.py
    my_dict = {'jobs_list':jobs_list}
    return render(request,'testapp/punejobs.html',context=my_dict)

# home(index).html contains ==> hydJobs, BengaluruJobs, puneJobd
#after clicking on the hydjobs ==> we hve to move to the hydjobs.html so we have to give this link inside render()
#hydjobs.html ==> we have to create inside templates/testapp
