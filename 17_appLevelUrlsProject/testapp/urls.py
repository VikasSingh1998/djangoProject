#defing the urls at application level

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('exam/', views.exams_view),
    path('attendence/', views.attendence_view),
    path('fees/', views.fees_view),
]