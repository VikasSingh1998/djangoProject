from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_view(request):
    s='<h2>this is the first view</h2>'
    return HttpResponse(s)

def second_view(request):
    s='<h2>this is the second view</h2>'
    return HttpResponse(s)

def third_view(request):
    s='<h2>this is the third_view</h2>'
    return HttpResponse(s)

def fourth_view(request):
    s='<h2>this is the fourth_view</h2>'
    return HttpResponse(s)

def fifth_view(request):
    s='<h2>this is the fifth_view</h2>'
    return HttpResponse(s)



