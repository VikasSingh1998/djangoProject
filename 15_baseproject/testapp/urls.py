#defing the urls at application level
from django.urls import path
from . import views # . means current package

urlpatterns = [
    path('first/', views.first_view),
    path('second/', views.second_view),
    path('third/', views.third_view),
    path('fourth/', views.fourth_view),
    path('fifth/', views.fifth_view),
]
#A Django project can contain multiple appliction and 
#each application can contain multiple views. 
#defing url pattern for all the views of application inside views.py of the project create maintence problem. and reduces maintainability of the appliction.

#S0, we have to define the urls pattern inside that appliaction only.
#dont define the url at project level

#we have to define the url at application level so that if we copy the appication into the other project ,so along with the appliation urls for the views will also be copied 
#so maintenance will be easy.


