from django.shortcuts import render

# Create your views here.
def index(request):
    """ Atiende la petición GET / """
    return render(request, "tours/index.html")  # templates/tours/index.html

def perfiles(request):
    """ Atiende la petición GET /perfiles """
    return render(request, "tours/perfil.html")  # templates/tours/perfil.html
