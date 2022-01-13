from django.shortcuts import render

# Create your views here.
def index(request) :
    n = []
    for i in range(1,101) :
        n.append(i)
    return render(request, 'scroll1/scroll.html', {
        "count": n
    })