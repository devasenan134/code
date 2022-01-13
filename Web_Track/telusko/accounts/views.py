from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def loginuser(request):
    if request.method == "GET":
        return render(request, 'accounts/loginuser.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= username, password=password)

        if user is not None: 
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('accounts:loginuser')


def logoutuser(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'GET':
         return render(request, 'accounts/register.html')
        
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('accounts:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('accounts:register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                auth.login(request, user)
        else:
            messages.info(request, 'Passwords not matching')
            return redirect('accounts:register')
        return redirect('/')

