from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # / -> views.index()
]  # Lista de rutas de la app -tours-
