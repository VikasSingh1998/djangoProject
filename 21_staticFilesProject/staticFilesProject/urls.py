"""
URL configuration for staticFilesProject project.

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
from django.urls import path,include
from testapp import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('staticFiles/', include('testapp.urls')),
]
# http://127.0.0.1:8000/staticFiles/staticFiles/
# http://127.0.0.1:8000 --> to reach the server and project
# staticFiles --> will be resolved by using project level urls.py
# staticFiles --> this will be resolved by using application level urls.py

 