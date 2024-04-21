from django import forms
#  we hvae to implement the forms for the model to take the input
from testapp.models import Movie

# we have to display all the fields for the Movie in the form to take the inuput form the user.
class MovieForm(forms.ModelForm):#this is model based form
    class Meta:
        model=Movie
        fields='__all__'