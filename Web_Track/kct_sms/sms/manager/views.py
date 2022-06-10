from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

from .forms import CreateUser, LeaveForm

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('manager:home'))
    else:
        form = CreateUser()
        if request.method == 'POST':
            form = CreateUser(request.POST)
            if form.is_valid():
                form.save()
                username = request.POST.get('username')
                messages.success("Account is created for: ", username)
                return redirect(reverse('manager:loginpage'))

        return render(request, "manager/register.html", {
            "form": form,
        })

def loginpage(request):
    if request.user.is_authenticated:
        return redirect(reverse('manager:home'))
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            idno = request.POST.get('idno')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('manager:home'))

        return render(request, "manager/login.html", {

    })


def logoutpage(request):
    if request.method == "POST":
        logout(request)
        return redirect(reverse("manager:loginpage"))
    
    return redirect(reverse("manager:loginpage"))


@login_required(login_url="manager:loginpage")
def home(request):
    my_routine = SecurityRoutine.objects.filter(name = request.user)
    leave_applied = Leave.objects.filter(name=request.user)
    return render(request, 'manager/home.html', {
        "routines": my_routine,
        "leave_applied": leave_applied,
    })

def view_leave(request):
    leave_applied = Leave.objects.filter(name=request.user)
    return render(request, 'manager/leaves.html', {
        "leave_applied": leave_applied,
    })


def apply_leave(request):
    leave_form = LeaveForm()
    return render(request, "manager/apply_leave.html", {
        "form": leave_form,
    })
