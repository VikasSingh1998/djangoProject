from django.shortcuts import render
from testapp.forms import StudentForm

# Create your views here.
def student_input_view(request):
    # form=StudentForm() # create the object of the StudentForm
    submitted=False
    sname=''
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            print('form validations done..!!')
            print("name: ",form.cleaned_data['name'])
            print("marks: ",form.cleaned_data['marks'])
            print("age: ",form.cleaned_data['age'])
            # this will be printed to console bex of normal print 
            sname=form.cleaned_data['name']
            submitted=True
    form=StudentForm() # after submit new form will be displayed 
    return render(request,'testapp/input.html',{'form':form,'submitted':submitted,'sname':sname})

# form=StudentForm() => empty form object to display form to end user 
# form=StudentForm(request.POST) => this form object contains the end user provided data 

# In Django, when you create a form using StudentForm(), 
# it creates an empty form object that can be used to display the form to the end-user. 
# When you use StudentForm(request.POST), 
# it populates the form object with the data submitted by the end-user via a POST request.
 
# form.is_valid() => to check whether all validations are successfull or not 

# cleaned_data => it is a dictionary which contains end user provided data 
# form.cleaned_data['name'] => give the name entered by end user 
# form.cleaned_data['marks'] => give the marks entered by end user 

