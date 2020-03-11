from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # / -> views.index()
    path("perfiles", views.perfiles, name="perfiles"),  # /perfiles -> views.perfiles()
    path("login", views.login_user, name="login"),  # /login -> views.login
]  # Lista de rutas de la app -tours-
