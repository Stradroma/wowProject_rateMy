from django.db import models
from django import forms

# # Create your models here.
class Borough(models.Model):
    pass

class Counsel(models.Model):
    counsel_full_name = forms.CharField(max_length=50)
    firm = forms.CharField(max_length=100)
    web_link= forms.CharField(max_length=50)

class Comment(models.Model):
    counsel_full_name = forms.CharField(max_length=50)
    comments = forms.CharField(max_length=500)

class Rating(models.Model):
    pass

class ViewCounsel(models.Model):
    pass

