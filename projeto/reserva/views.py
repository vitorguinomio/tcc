# seu_app/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReservaForm

def FazerReserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sua reserva foi feita com sucesso')
            return redirect('reserva:FazerReserva')
    
    else:
        form = ReservaForm()
    
    return render (request, 'reserva/reservar.html', {'form', form})


def reservar(request):
    return render(request, 'reserva/reservar.html')