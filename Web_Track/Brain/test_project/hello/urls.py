from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("deva", views.deva, name="deva"),
    path("kum", views.kum, name="kum")
]