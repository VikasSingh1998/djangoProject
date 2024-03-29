"""
URL configuration for OneProjectMultipleApp project.

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
# from firstApp import views
# from secondApp import views
#here second app views will override the first app views ==> create ambiguity 
#so in second app app1_view1 is not present
#AttributeError: module 'secondApp.views' has no attribute 'app1_view1'. Did you mean: 'app2_view1'?
#To solve this error, we will use alias name
from firstApp import views as v1
from secondApp import views as v2
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test1/',v1.app1_view1),
    path('test2/',v2.app2_view1),
]
# http://127.0.0.1:8000/test1/
# http://127.0.0.1:8000/test2/