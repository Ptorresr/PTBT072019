from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),  # / -> views.index()
    path("perfiles", views.perfiles, name="perfiles"),  # /perfiles -> views.perfiles()
    path("login", views.login_user, name="login"),  # /login -> views.login
    # Rutas para el modelo Tour
    path("tour/eliminar/<int:idTour>", views.tour_eliminar, name="tour_eliminar"),  # /tour/eliminar/id
]  # Lista de rutas de la app -tours-
