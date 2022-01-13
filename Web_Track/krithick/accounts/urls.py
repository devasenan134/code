from . import views
from django.urls import path

app_name = "accounts"
urlpatterns = [
    path("signup/", views.signupuser, name="signupuser"),
    path('login/', views.loginuser, name="loginuser"),
    path("logout/", views.logoutuser, name="logoutuser"),
]
