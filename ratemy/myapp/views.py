from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def home(request):
    if request.method == 'GET':
        return render(request=request, template_name='home.html')

def borough(request):
    if request.method == 'GET':
        return render(request=request, template_name='borough.html')

def viewcounsel(request):
    if request.method == 'GET':
        return render(request=request, template_name='viewcounsel.html')

def counselprofile(request):
    if request.method == 'GET':
        return render(request=request, template_name='counselprofile.html')

def addcounsel(request):
    if request.method == 'GET':
        return render(request=request, template_name='addcounsel.html')

def about(request):
    if request.method == 'GET':
        return render(request=request, template_name='about.html')