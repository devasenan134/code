from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request) :
    return render(request, "hello/index.html")

def deva(request) :
    return HttpResponse("Hello, devasenan!")

def kum(request) :
    return HttpResponse("Hello, kumaresan!")

def greet(request, name) :
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
