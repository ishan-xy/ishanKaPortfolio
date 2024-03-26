from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse

def index(request):
    
    
    
    return render(request, 'home/index.html')

def projects(request):
    return redirect(reverse('projects:index'))