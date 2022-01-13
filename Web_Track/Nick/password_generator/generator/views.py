from django.shortcuts import render
from django.http import HttpResponse
from random import choice

# Create your views here.
def home(request) :
    return render(request, 'generator/home.html')


def password(request) :
    passwd = ""
    length = int(request.POST.get('length', 8))
    uc_opt = request.POST.get('uppercase')
    no_opt = request.POST.get('numbers')
    sp_opt = request.POST.get('special_char')
    characters = list("abcdefghijklmnopqrstuvwxyz")
    
    if uc_opt :
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if no_opt :
        characters.extend(list("0123456789"))
    if sp_opt :
        characters.extend(list("~!@#$%^&*()_+"))

    for i in range(length) :
        passwd += choice(characters)


    return render(request, 'generator/password.html',{
        "password": passwd
    })

