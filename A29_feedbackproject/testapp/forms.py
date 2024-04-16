from django import forms 
from django.core import validators
#forms module is inside the django package.
# forms module contain multiple classed ==> Form, ValidationError etc..

# class FeedBackForm(forms.Form):
#     name=forms.CharField()
#     rollno=forms.IntegerField()
#     email=forms.EmailField()
#     feedback=forms.CharField(widget=forms.Textarea)
    
#     #validation by using clean method
#     def clean_name(self):
#         print("validating the name field")
#         inputname =self.cleaned_data['name']
#         if len(inputname)<4:
#             raise forms.ValidationError("min name length must be 4")
#         return inputname
    
#     def clean_rollno(self):
#         print("validating the roll number field")
#         inputroll =self.cleaned_data['rollno']
#         return inputroll
    
#     def clean_email(self):
#         print("validating the email field")
#         inputemail =self.cleaned_data['email']
#         return inputemail
    
#     def clean_feedback(self):
#         print("validating the feedback field")
#         inputfeedback =self.cleaned_data['feedback']
#         return inputfeedback
#================================================================
# Django's Inbuilt Core Validators:
# -------------------------------------
# how to implenet the custom validators by using the same validators parameter
# def name_start_with_d(value):
#     print("name start with d or D is validating..")
#     if value[0].lower() !='d':
#         raise forms.ValidationError("name should start with d or D")

# def gmail_validator(value):
#     print("validating the gmail..")
#     if value[-10:] != '@gmail.com':
#         raise forms.ValidationError("gmail should end with @gmail.com")


# class FeedBackForm(forms.Form):
#     name=forms.CharField(validators=[name_start_with_d])
#     rollno=forms.IntegerField()
#     email=forms.EmailField(validators=[gmail_validator])
#     feedback=forms.CharField(widget=forms.Textarea,
#                              validators=[validators.MaxLengthValidator(50),
#                                          validators.MinLengthValidator(10),]
#                              )

#===============================================================
# we have seen ==>
# 1. by using field level clean method 
# 2. by using inbuilt validators
# 3. our own customized validators
# -----------
# now we will se "validatio of total form by using single clean method"
# ========================================================================
class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)
    
    def clean(self):
        print("total form validaation..")
        total_cleaned_data=super().clean()
        
        print("validating the name")
        input_name=total_cleaned_data['name']
        if(input_name[0].lower() !='d'):
            raise forms.ValidationError("Name should start with d or D")
        if(len(input_name)<4):
            raise forms.ValidationError("Name should contain atleat 4 latter")
        
        print("validating the email")
        input_mail=total_cleaned_data['email']
        if(input_mail[-10:] !='@gmail.com'):
            raise forms.ValidationError("only @gmail.com id are allowed")
        




#=================================================================
#views.py is responsible to create the form object and send it to html file to display.
# clean_name ==> django will call this method 
#clean_fieldname => this name is always fixed.
# //=====================================
# see the django document for this inbuild validation
