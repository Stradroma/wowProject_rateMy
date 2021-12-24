from typing import AbstractSet
from django import forms
from django.forms import ModelForm, widgets
from .models import Counsel 

class AddCounselForm(ModelForm):
    class Meta:
        model = Counsel
        fields = '__all__'
        labels = {
            'fName' : '', 
            'lName' : '',
            'firmN' : '',
            'status' : '',
            'phoneN' : '',
            'Address' : '',
            'Address2' : '',
            'zip_code' : '',
            'borough' : '',
            'city' : '',
            'state' : '',
        }

        widgets = {
            'fName' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Counsel First Name'}), 
            'lName' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Counsel Last Name', 'id' : 'nameID'}),
            'firmN' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Firm Name'}),
            'status' : forms.Select(attrs={'class' : 'form-select', 'placeholder' : 'Status'}),
            'phoneN' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Phone Numer'}),
            'Address' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Address'}),
            'Address2' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Adress 2'}),
            'zip_code' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Zip Code'}),
            'borough' : forms.Select(attrs={'class' : 'form-select', 'placeholder' : 'Borough', 'id' : 'boroughID'}),
            'city' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'City'}),
            'state' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'State'}),
            

        }
        