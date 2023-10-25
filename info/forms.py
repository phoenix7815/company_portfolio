from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class userdetails(forms.ModelForm):

    class Meta:
        model=user_details
        fields="__all__"


class SignUpForm(UserCreationForm):
   
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1')



