from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view ),
    path('hydjobs_page', views.hydjobs_view ),
    path('bengalurujobs_page', views.bengalurujobs_view ),
    path('punejobs_page', views.punejobs_view ),
]