from django.shortcuts import render

from .models import Tour

# Create your views here.
def index(request):
    """ Atiende la petición GET / """

    lista_tours = Tour.objects.all()
    ntours = len(lista_tours)

    return render(request, "tours/index.html",
        {"tours":lista_tours, "ntours":ntours}
    )  # templates/tours/index.html

def perfiles(request):
    """ Atiende la petición GET /perfiles """
    return render(request, "tours/perfil.html")  # templates/tours/perfil.html
