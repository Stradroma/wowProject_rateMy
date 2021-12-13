from django import forms
from django.forms import ModelForm
from .models import Counsel 

class AddCounsel(ModelForm):
    class Meta:
        model = Counsel
        