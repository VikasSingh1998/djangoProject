from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hyderabad_jobs_views(request):
    s='<h3>Hyderabad jobs related information</h3>'
    return HttpResponse(s)

def bengaluru_jobs_views(request):
    s='<h3>Bengaluru jobs related information</h3>'
    return HttpResponse(s)

def pune_jobs_views(request):
    s='<h3>Pune jobs related information</h3>'
    return HttpResponse(s)



#