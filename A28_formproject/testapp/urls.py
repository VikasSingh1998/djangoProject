from django.urls import path
from . import views
urlpatterns = [
    path('data/', views.student_input_view),
]
# inside the urls.py we give the link to view 