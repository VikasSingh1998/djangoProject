from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_view1(request):
    msg="this is the view in application 2";
    msg="<h2>"+msg+"</h2>"
    return HttpResponse(msg)
