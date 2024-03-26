from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    
    return render(request, 'projects/projects.html', context)