from django import forms
from info.models import vacant_position
from django.contrib.auth.forms import UserCreationForm
from info.models import vacant_position
from django.contrib.auth.models import User
from django.forms import ModelForm

class companyRegisterform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']

class companyLoginform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password']


class vacant_positio(ModelForm):
    class Meta:
        model=vacant_position
        fields='__all__'


