from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passenger
# Create your views here.

def home(request) :
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
    })

def admin_page(request):
    return HttpResponseRedirect("This is admin page")





#############
def flight(request, flight_id) :
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight" : flight,
        "passengers": flight.passengers.all(),  # not clear....
        "non_passengers": Passenger.objects.exclude(flights = flight).all()
    })

def book(request, flight_id) : # not clear....
    if request.method == "POST" :
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk = int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))