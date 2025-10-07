# Dentro do arquivo /projeto/urls.py

from django.contrib import admin
from django.urls import path, include  # VERIFIQUE SE 'include' ESTÁ IMPORTADO

urlpatterns = [
    path('admin/', admin.site.urls),

    # Esta linha diz ao Django para usar as rotas do arquivo reserva/urls.py
    # para a página inicial do site.
    path('', include('reserva.urls')),
    path('cardapio/', include('cardapio.urls')),
    path('cronograma/', include('cronograma.urls'))
]