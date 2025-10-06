from django.urls import path
from . import views

app_name = "reserva"

urlpatterns = [
    path("", views.hreserva ),
    path("agenda/", views.pagreser),
    path("cardapio/", views.cardapio, name="cardapio"),
    path("test/", views.home)
]

