from django.shortcuts import render
import datetime
import random
# Create your views here.
def datetime_view(request):
    date=datetime.datetime.now()
    my_dict = {'msg':date}
    return render(request,'testapp/datetime.html',context=my_dict)
    # return render(request,'testapp/datetime.html', {'msg':date})

#how to send the multile values in the dictionary
def datetime_view1(request):
    date=datetime.datetime.now()
    name='Django'
    prerequisits='python'
    my_dict = {'date':date,'name':name,'prerequisits':prerequisits}
    return render(request,'testapp/datetime1.html',context=my_dict)
    # return render(request,'testapp/datetime.html', {'msg':date})
    
def astrology_view(request):
    msg_list=[
        'message1',
        'message2',
        'message3',
        'message4',
    ]   
    names_list=['vikas','ravi','prashant','aditya',]
    date=datetime.datetime.now()
    name=random.choice(names_list)
    msg=random.choice(msg_list)
    my_dict={'date':date,'name':name,'msg':msg}
    return render(request,'testapp/astrology.html',context=my_dict)
    
#=====================================================================
#Here we have to send this msg to the template file
#but we can send our data in the form of dictionary only.
#To send the dynamic content from views.py to template file we use template tags/template variable.
#we can send as the part of context dictionary.
#we can send only dictionary, we cant send variable directly.
