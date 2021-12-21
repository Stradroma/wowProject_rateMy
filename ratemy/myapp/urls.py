from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('borough', views.borough, name='borough'),
    path('viewcounsel', views.viewcounsel, name='viewcounsel'),
    path('counselprofile', views.counselprofile, name='counselprofile'),
    path('addcounsel', views.addcounsel, name='addcounsel'),
    path('about', views.about, name='about'),
    path('bronx', views.bronx, name='bronx'),
    path('manhattan', views.manhattan, name='manhattan'),
    path('queens', views.queens, name='queens'),
    path('brooklyn', views.brooklyn, name='brooklyn'),
    path('staten_island', views.staten_island, name='staten_island'),
]