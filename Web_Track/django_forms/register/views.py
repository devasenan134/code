from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import SignupForm 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    return render(request, 'register/register.html')


def signupuser(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        email = request.POST['email']
        if form.is_valid() :
            if User.objects.filter(email=email).exists():
                 return render(request, 'register/signupuser.html', {
                     'form': form,
                     'error': "Email already exists"
                 })
            else:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
        else:
            return render(request, 'register/signupuser.html', {
                'form': form 
            })
        return redirect('/register')       # difference btwn using redirect, httpresponseredirect, render 

    else:
        form = SignupForm()

    return render(request, 'register/signupuser.html', {
        'form': form
    })


def loginuser(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        form = AuthenticationForm(request.POST)
        if user is not None:
            login(request, user)
        else:
            return render(request, 'register/loginuser.html', {
                'form': form,
                'error': "Invalid credentials"
            })
        return HttpResponseRedirect(reverse('register'))
    else:
        form = AuthenticationForm()
        return render(request, "register/loginuser.html", {
            'form': form
        })


@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('register'))

'''
@login_required
def passwordchange(request):
    if request.method == 'POST':
        u = User.objects.get(request.POST)
        name = u.username
        print(name)
        u.set_password('12345678')
        u.save()
'''
