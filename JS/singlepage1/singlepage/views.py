from django.shortcuts import render
from django.http import HttpResponse, Http404


# Create your views here.

def index(request) :
    return render(request, "singlepage/index1.html")


texts = ["jgkjn ;jih;kjh; e86ene66e6i7i7i76o  lb kj;  i gkjb kbkjkjb",
    "sdgsaha er haerheratettht strj trjtsrj tsjtrsj ar",
    "fgb kbrsgakjghrgharkghdrgh;ghighagiadhgipughaghariuhrguahripghaergiuarhg"]


def section(request, num) :
    if 1 <= num <=3 :
        return HttpResponse(texts[num - 1])
    else :
        raise Http404("No such section")