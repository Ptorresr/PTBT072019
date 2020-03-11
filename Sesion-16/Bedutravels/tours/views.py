from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Tour, User

# Create your views here.
@login_required()
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

def login_user(request):
    """ Atiende la petición GET /login """
    # Inicializando variable msg a vacio
    msg = ""

    # Obtener los datos del formulario
    if request.method == "POST":
        user_form = (request.POST["username"], request.POST["password"])
        next_url = request.GET.get("next", "/")
        user = authenticate(username=user_form[0], password=user_form[1])
        if user is not None:
            # Se inicializan las variables de sesión
            login(request, user)
            return redirect(next_url)
        else:
            msg = "Error datos de acceso inválidos!"

    return render(request, "registration/login.html",
        {
            "msg":msg
        }
    )
