# seu_app/views.py

from django.shortcuts import render

def home(request):
    # O terceiro argumento (contexto) é opcional.
    return render(request, 'reserva/home.html')