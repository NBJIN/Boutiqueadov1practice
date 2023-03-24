from django.contrib import admin
from django.urls import path
from . import views # import views from the . which is current directory 

urlpatterns = [
    path('', views.index, name='home') # this is the root url and render view.index with a name of home 
] 
