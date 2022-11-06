from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('First Web-site page')

def test2(request):
    return HttpResponse('Second Web-site page')