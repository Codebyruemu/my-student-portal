from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . models import *


# usercreation form is the skeleton that enable you
# create the form that django will use to save the User information
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        
class CreatePost(forms.ModelForm):
    class Meta:
        model = Good
        fields='__all__'