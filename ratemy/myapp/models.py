from django.db import models
from django import forms
from django.db.models.fields import DateField

# # Create your models here.
class Borough(models.Model):
    pass

class Counsel(models.Model):
    fName = models.CharField(max_length= 15)
    lName = models.CharField(max_length= 15)
    firmN = models.CharField(max_length= 100)
    status = models.ForeignKey
    phoneN = models.IntegerField()
    Address = models.CharField(max_length= 15)
    Address2 = models.CharField(max_length= 15)
    zip_code = models.IntegerField()
    borough = models.ForeignKey
    city = models.CharField(max_length= 15)
    state = models.CharField(max_length= 15) 

class Comment(models.Model):
    fName = models.CharField(max_length= 15)
    lName = models.CharField(max_length= 15)
    date = DateField
    comments = forms.CharField(max_length=500)


class ViewCounsel(models.Model):
    pass

