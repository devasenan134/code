from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import UserAccount

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.


def signupuser(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        adhar = request.POST['adhar']
        phone = request.POST['phone']
        if form.is_valid():
            if len(phone) > 10 or len(phone) < 10:
                return render(request, 'accounts/signupuser.html', {
                    'form': form,
                    'error': "Enter a valid Phone number"
                })
            elif len(adhar) > 12 or len(adhar) < 12:
                return render(request, 'accounts/signupuser.html', {
                    'form': form,
                    'error': "Enter a valid Adhar number"
                })
            else:
                user = UserAccount.objects.create_user(
                    username = request.POST['username'],
                    email=request.POST['email'],
                    phone = phone,
                    adhar = adhar,
                    password=request.POST['password1'], 
                    )
                user.save()
                login(request, user)
        else:
            return render(request, 'accounts/signupuser.html', {
                'form': form
            })
        return redirect('/')

    else:
        form = SignupForm()

    return render(request, 'accounts/signupuser.html', {
        'form': form
    })


def loginuser(request):
    if request.method == 'POST':
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])
        form = AuthenticationForm(request.POST)
        if user is not None:
            login(request, user)
        else:
            return render(request, 'accounts/loginuser.html', {
                'form': form,
                'error': "Invalid credentials"
            })
        return HttpResponseRedirect(reverse('home:index'))
    else:
        form = AuthenticationForm()
        return render(request, "accounts/loginuser.html", {
            'form': form
        })

def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('home:index')
