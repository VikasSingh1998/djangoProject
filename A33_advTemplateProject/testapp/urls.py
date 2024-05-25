from django.urls import path
from testapp import views

urlpatterns = [
    path('', views.home_page_view, name='home_page_view'),
    path('movies/', views.movies_page_view, name='movies_page_view'),
    path('politics/', views.politics_page_view, name='politics_page_view'),
    path('sports/', views.sports_page_view, name='sports_page_view'),
]
