from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# import models
from .models import Cat

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', { 'cats': cats })


#make a view function
#make the html page
#add the view to the urls.py inside of main.app.urls