from django.shortcuts import render
from testapp.models import Movie
from testapp.forms import MovieForm

# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')

def list_movies_view(request):
    movies_list=Movie.objects.all()
    # we have to send this object to another html page which will 
    # display the movies information when we will click show movies.
    return render(request,'testapp/movieslist.html',{'movies_list':movies_list})
    

# def input_movie_view(request):
#     form=MovieForm() #create the movie form object
#     if request.method=='POST':
#         form=MovieForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print("movies saved into the database!!")
#         return index_view(request)
#     return render(request,'testapp/movieform.html',{'form':form})
#     #send this form objec to the html page.

def input_movie_view(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            print("Movie saved into the database!!")
            return index_view(request)  # Redirect to the index view after saving the movie
    else:
        form = MovieForm()  # Create the movie form object for GET requests

    return render(request, 'testapp/movieform.html', {'form': form})
