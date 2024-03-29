from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'testapp/index.html')

def movie_view(request):
    head_msg='Durga Movie News'
    m1='OTT is the result the covid'
    m2='OTT is the result the covid'
    m3='OTT is the result the covid'
    my_dict={
        'head_msg':head_msg,
        'm1':m1,
        'm2':m2,
        'm3':m3,
    }
    return render(request,'testapp/movies.html',my_dict)