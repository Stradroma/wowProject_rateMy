from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AddCounselForm
from datetime import datetime

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
    submitted = False
    if request.method == "POST":
        form = AddCounselForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('addcounsel.html?submitted=True')
    
    else:
        form = AddCounselForm
        if 'submitted' in request.method == 'GET':
            submitted = True
    
    return render( request, 'addcounsel.html', context = {'form' : form, 'submitted' : submitted} )

def about(request):
    if request.method == 'GET':
        return render(request=request, template_name='about.html')

def bronx(request):
    if request.method == 'GET':
        return render(request=request, template_name='bronx.html') 

def manhattan(request):
    if request.method == 'GET':
        return render(request=request, template_name='manhattan.html') 

def queens(request):
    if request.method == 'GET':
        return render(request=request, template_name='queens.html')  

def brooklyn(request):
    if request.method == 'GET':
        return render(request=request, template_name='brooklyn.html') 

def staten_island(request):
    if request.method == 'GET':
        return render(request=request, template_name='staten_island.html') 
                                             