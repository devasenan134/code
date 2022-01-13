from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from .models import UserAccount

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = UserAccount
        fields = [
            'email',
            'username',
            'phone',
            'adhar',
            'password1',
            'password2'
        ]   
    