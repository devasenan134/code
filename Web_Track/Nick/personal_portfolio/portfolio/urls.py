from . import views
from django.urls import path

app_name = "portfolio"
urlpatterns = [
    path("", views.home, name="home"),
    path("resume", views.resume, name="resume")
]