from django.shortcuts import render
from testapp.models import Employee
#here we will fetch the data from the database and print to the console
#we are using the model concepts
#we have defined our table into the models.py, so we have to import that table

##

# Create your views here.
def  empdata_view(request):
    emp_list=Employee.objects.all()
    my_dict={'emp_list':emp_list}
    # print(emp_list)
    return render(request,'testapp/emp.html',context=my_dict)