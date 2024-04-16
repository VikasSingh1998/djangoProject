from django.urls import path
from . import views
urlpatterns = [
    path('form/', views.feedback_view),
]
# inside the urls.py we give the link to view 