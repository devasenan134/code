from dataclasses import field
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUser(UserCreationForm):
    # type = models.CharField(choices = ['security', 'manager'])
    idno = forms.IntegerField()
    class Meta:
        model = User
        fields = ('username', "idno", "password1", "password2")


class LeaveForm(forms.Form):
    class Meta:
        model = Leave
        fields = ("from_date", "to_date", "reason")