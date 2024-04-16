from django import forms 
from django.core import validators
#forms module is inside the django package.
# forms module contain multiple classed ==> Form, ValidationError etc..

# ========================================================================
class FeedBackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(label='Password',widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Re-Enter Password',widget=forms.PasswordInput)
    feedback=forms.CharField(label='give feedback',widget=forms.Textarea)
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)
    
    def clean(self):
        # get total data entered by enduser
        total_cleaned_data=super().clean()
        pwd=total_cleaned_data['password']
        rpwd=total_cleaned_data['rpassword']
        if(pwd != rpwd ):
            raise forms.ValidationError("both password should be same")
        bot_handler_value=total_cleaned_data['bot_handler']
        if len(bot_handler_value)>0:
            raise forms.ValidationError('Request from BOT...cannot be submitted!!!') 
        
        
        
#read about BOT later.