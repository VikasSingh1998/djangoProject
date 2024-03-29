from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.
def datetime_views(request):
    curr_dt=datetime.datetime.now();#get current date and time
    # date=curr_dt.data();#take out the current date formt he current date and time
    # time=curr_dt.time();#take out the current time from the current date and time
    hour=curr_dt.hour;
    
    msg="Hello Friend, "
    if(hour<12):
        msg+="Good Morning!"
    elif(hour<16):
        msg+="Good Afternoon!"
    elif(hour<21):
        msg+="Good Evening!"
    else:
        msg+="good night !!!"
    
    msg ="<h2>"+msg+"</h2><hr>"
    msg+="<h2> Server time is: "+str(curr_dt)+"</h2>"
    print(msg);
    return HttpResponse(msg)
    
    
    
    
    
    
    

