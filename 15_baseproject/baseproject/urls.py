"""
URL configuration for baseproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
# from testapp import 
from testapp import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('first/', views.first_view),
    # path('second/', views.second_view),
    # path('third/', views.third_view),
    # path('fourth/', views.fourth_view),
    # path('fifth/', views.fifth_view),
    path('testapp/', include('testapp.urls')),
    
]
# http://127.0.0.1:8000/testapp/first/  ==> hit this url

#A Django project can contain multiple appliction and 
#each application can contain multiple views. 
#defing url pattern for all the views of application inside views.py of the project create maintence problem. and reduces maintainability of the appliction.

#S0, we have to define the urls pattern inside that appliaction only.
#dont define the url at project level

#we have to define the url at application level so that if we copy the appication into the other project ,so along with the appliation urls for the views will also be copied 
#so maintenance will be easy.

##############################
#Now once we defined the urls inside the appliactions then we can import the urls from the application and use it at project level


