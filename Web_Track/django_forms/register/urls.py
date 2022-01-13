from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name="register"),
    path('signup', views.signupuser, name='signupuser'),
    path('login', views.loginuser, name='loginuser'), 
    path('logout', views.logoutuser, name='logoutuser')
    #path('change_password', views.passwordchange, name='passwordchange'),
]
