from django.shortcuts import render
from testapp.models import Student

# Create your views here.
def upper_data_view(request):
    records = Student.objects.all()
    return render(request,'testapp/upper.html',{'records':records})








