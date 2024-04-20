from django.shortcuts import render
from testapp.models import Student
from testapp.forms import StudentForm

# Create your views here.
def student_view(request):
    form=StudentForm() # create the StudentForm object
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print("Record Saved into the DataBase!!")
    return render(request,'testapp/studentform.html',{'form':form})
    # send this form object to the html page.