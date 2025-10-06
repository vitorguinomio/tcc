from django.shortcuts import render
from django.http import HttpResponse

def hreserva(request):
    contexto = {
        "nome":"Lan"
    }
    return render(request, 'reserva/home.html', contexto)
# Create your views here.
def pagreser (request):
    return HttpResponse("Nessa pagina voce faz a reserva no restaurante")

def cardapio(request):
    return render(request, 'reserva/cardapio.html' )

def home(request):
    return render(request, 'reserva/home.html')