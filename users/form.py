from django import forms
from .models import  User

class UserModel(forms.ModelForm):
    class Meta:
            model = User
           
            attrs={'class':'form-control'} #adding custom classes to forms
            

