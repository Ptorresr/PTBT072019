from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # / -> views.index()
    path("perfiles", views.perfiles, name="perfiles"),  # /perfiles -> views.perfiles()
]  # Lista de rutas de la app -tours-
