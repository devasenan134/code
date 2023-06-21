from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect(reverse('flights:home'))
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            is_admin = request.POST.get("is_admin")
            user = authenticate(username=username, password=password)
        
            if user is not None:
                login(request, user)
                if is_admin:
                    return HttpResponse("This has to be redirected to admin page in flights app")
                else:
                    return HttpResponse("This has to be redirected to home page in flights app")
            else:
                messages.info(request, "Username or password is incorrest")

        return render(request, "all_users/login.html", {
        })



def logout_user(request):
    logout(request)
    return redirect(reverse("all_users:login_user"))
