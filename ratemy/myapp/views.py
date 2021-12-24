from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AddCounselForm
from datetime import datetime
from django.utils import timezone

# Create your views here.
def delete_review(request):
    review = Review.objects.get(pk=review_id)
    review.delete()
    return redirect('list-events')
# views for home.html
def home(request):
    if request.method == 'GET':
        return render(request=request, template_name='home.html')
# views for borough.html
def borough(request):
    if request.method == 'GET':
        return render(request=request, template_name='borough.html')
# views for viewcounsel.html
def viewcounsel(request):
    if request.method == 'GET':
        return render(request=request, template_name='viewcounsel.html')
# views for counselprofile.html
def counselprofile(request):
    if request.method == 'GET':
        return render(request=request, template_name='counselprofile.html')
# views for addcounsel.html
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
# views for about.html
def about(request):
    if request.method == 'GET':
        return render(request=request, template_name='about.html')
# views for bronx.html
def bronx(request):
    if request.method == 'GET':
        return render(request=request, template_name='bronx.html') 
# views for manhattan.html
def manhattan(request):
    if request.method == 'GET':
        return render(request=request, template_name='manhattan.html') 
# views for queens.html
def queens(request):
    if request.method == 'GET':
        return render(request=request, template_name='queens.html')  
# views for brooklyn.html
def brooklyn(request):
    if request.method == 'GET':
        return render(request=request, template_name='brooklyn.html') 
# views for staten_island.html
def staten_island(request):
    if request.method == 'GET':
        return render(request=request, template_name='staten_island.html') 

                                 