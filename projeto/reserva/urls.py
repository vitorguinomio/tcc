# Dentro do arquivo /reserva/urls.py

from django.urls import path
from . import views

# Boa prática: Define um "namespace" para evitar conflito com outras apps
app_name = 'reserva' 

urlpatterns = [
    # A rota '' (vazia) chama a view 'home' e recebe o nome 'home'
    path('', views.reservar, name='reservar'),
]