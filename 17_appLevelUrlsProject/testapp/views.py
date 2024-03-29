from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def exams_view(request):
    s='<h2>exam view</h2>'
    return HttpResponse(s)

def attendence_view(request):
    s='<h2>attendence view</h2>'
    return HttpResponse(s)

def fees_view(request):
    s='<h2>fees_view</h2>'
    return HttpResponse(s)

