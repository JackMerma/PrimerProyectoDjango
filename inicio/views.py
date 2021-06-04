from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myHomeView(*args, **kwargs):
    return HttpResponse('<h1>Hola mundo</h1>')

def another(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return HttpResponse('<h1>Otra pagina</h1>')
