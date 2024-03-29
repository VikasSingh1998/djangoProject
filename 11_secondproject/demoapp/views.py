from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def time_info_view(request):
    time=datetime.datetime.now()
    s='<h3>Hello current data and time is :'+str(time)+'</h3>'
    return HttpResponse(s)

