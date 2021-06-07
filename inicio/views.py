from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(request, *args, **kwargs):
    return render(request, "home.html", {})

def another(*args, **kwargs):
    return HttpResponse('<h1>Esta es otra pagina</h1>');

def letras(request, *arg, **kwargs):
    return render(request, "letters/first.html", {})
