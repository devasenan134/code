from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.
def home(request) :
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {
        'projects': projects        
    })

def resume(request) :
    return HttpResponse("<h1 style='text-align:center;'>Coming soon :)</h1>")


def icons(request) :
    return render(request, 'portfolio/Untitled.html')
