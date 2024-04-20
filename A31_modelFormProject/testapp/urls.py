from django.urls import path
from testapp import views
urlpatterns = [
    path('form/', views.student_view),
]
# inside the urls.py we give the link to view 
