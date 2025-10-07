# Dentro do arquivo /reserva/urls.py

from django.urls import path
from . import views

app_name = 'cardapio' 

urlpatterns = [

    path('', views.cardapio, name='cardapio')
]