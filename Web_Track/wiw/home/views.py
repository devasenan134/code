from django.shortcuts import render
from .models import Video

# Create your views here.

def home(request):
    data = Video.objects.all()
    return render(request, "home/home.html", {
        "videos": data
    })
