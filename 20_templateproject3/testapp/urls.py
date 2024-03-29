from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('datetime/',views.datetime_view),
    path('datetime1/',views.datetime_view1),
    path('astrology/',views.astrology_view),
]
