from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kwargs):
    return render(request, "home.html", {})

def another(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})

def letras(request, *arg, **kwargs):
    return render(request, "angular/first.html", {})
