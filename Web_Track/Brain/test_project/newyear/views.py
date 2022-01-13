from django.shortcuts import render
from datetime import datetime as dt
# Create your views here.

#we can also do the same thing as,
'''
now = dt.now()
if now.month == 1 and now.day == 1 :
    newyear = Yes
else :
    newyear = No
return render(request, "newyear/index.html", {
    "newyear : newyear
    })
'''

def index(request) :
    now = dt.now()
    return render(request, "newyear/index.html", {
        "newyear" : now.month == 1 and now.day == 1 
    }) 