from django.shortcuts import render
from testapp.forms import FeedBackForm
# Create your views here.

def feedback_view(request):
    form = FeedBackForm() 
    submitted=False
    name=''
    if request.method=='POST':
        form=FeedBackForm(request.POST) #create the object while post 
        if form.is_valid(): # at this line it will check whether for any field clean method is defined or not in the forms.py, so control will go there.
            print("form validated..")
            print("#"*20)
            print("Name:",form.cleaned_data['name'])
            print("rollno:",form.cleaned_data['rollno'])
            print("email:",form.cleaned_data['email'])
            print("feedback:",form.cleaned_data['feedback'])
            submitted=True
            name=form.cleaned_data['name']
        else:
            print("validation failed..")

    # form = FeedBackForm() #create the object of FeedBackForm class
    return render(request,'testapp/feedback.html',{'form':form,'submitted':submitted,'name':name})

#now we have to create html file to display the form.
