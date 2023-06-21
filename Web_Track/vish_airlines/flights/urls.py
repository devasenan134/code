from django.urls import path
from . import views

app_name = "flights"
urlpatterns = [
    path("", views.home, name="home"),
    path("/admin_page", views.admin_page, name="admin_page"),
]