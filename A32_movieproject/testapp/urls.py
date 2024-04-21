# from django.urls import path
# from testapp import views
# urlpatterns = [
#     path('movies/', views.index_view),
#     path('movies/listmovies/', views.list_movies_view),
#     path('movies/movieform/', views.input_movie_view),
# ]
# # inside the urls.py we give the link to view 

# //-----------------------
from django.urls import path
from testapp import views

urlpatterns = [
    path('movies/', views.index_view, name='index_view'),
    path('movies/listmovies/', views.list_movies_view, name='list_movies_view'),
    path('movies/movieform/', views.input_movie_view, name='input_movie_view'),
]
