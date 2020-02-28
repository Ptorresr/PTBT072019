from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    """ Atiende la petición GET / """
    return HttpResponse("<h1>Página de inicio! Hecho con <3</h1>")
