from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *

class userdetails(forms.ModelForm):

    class Meta:
        model=user_details
        fields="__all__"


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class extra_details(ModelForm):

    class Meta:
        model=user_details
        exclude=['application']

class apply(ModelForm):
    class Meta:
        model=vacant_position
        fields=['id']