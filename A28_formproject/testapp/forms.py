from django import forms

class StudentForm(forms.Form):
    name=forms.CharField() #in model we have to specify the length but here it is optionsl
    marks=forms.IntegerField()
    age=forms.IntegerField()
    

