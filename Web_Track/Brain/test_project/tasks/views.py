from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.

class NewTaskForm(forms.Form) :
    task = forms.CharField(label="New Task")
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

def index(request):
    if "tasks" not in request.session :
        request.session["tasks"] = []   # creating a empty list for each users or sessions  
        ''' sessions store data about our each visits, it stores info like ID or info about you in this case our tasks.
        sessions are like big dictionary.'''
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"] # this passes that list, i created above.
    })

def add(request) :
    if request.method == "POST" :
        form = NewTaskForm(request.POST)
        if form.is_valid() :       # server side validation.
            task = form.cleaned_data["task"]
            if task not in request.session["tasks"] :
                request.session["tasks"] += [task]
                return HttpResponseRedirect(reverse("tasks:index"))
            return render(request, 'tasks/add.html', {
                "form" : form,
                "added" : "Task already added!!"
            })
        else :
            return render(request, "tasks/add.html", {
                "form" : form
            })
    return render(request, "tasks/add.html", {
        "form" : NewTaskForm()
    })


def clear(request) :
    if "tasks" in request.session :
        request.session.pop("tasks") # used a dict method to del the item "tasks" in the dict session.
    request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks" : request.session["tasks"]   
    })
