from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')

def movies_view(request):
    head_msg="Movies Information"
    sub_msg1="RRR"
    sub_msg2="Bahubali"
    sub_msg3="Rajniti"
    sub_msg4="Mahabharat"
    my_dict={
        'head_msg':head_msg,
        'sub_msg1':sub_msg1,
        'sub_msg2':sub_msg2,
        'sub_msg3':sub_msg3,
        'sub_msg4':sub_msg4,
    }
    return render(request,'testapp/movies.html',my_dict)

def sports_view(request):
    head_msg="Sports Information"
    sub_msg1="kohli"
    sub_msg2="sachin"
    sub_msg3="dhoni"
    sub_msg4="rohit"
    my_dict={
        'head_msg':head_msg,
        'sub_msg1':sub_msg1,
        'sub_msg2':sub_msg2,
        'sub_msg3':sub_msg3,
        'sub_msg4':sub_msg4,
    }
    return render(request,'testapp/sports.html',my_dict)
