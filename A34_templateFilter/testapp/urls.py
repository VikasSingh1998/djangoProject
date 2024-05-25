from django.urls import path
from testapp import views

urlpatterns = [
    path('upper/', views.upper_data_view, name='upper_data_view'),
]
