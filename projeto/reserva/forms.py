from django.forms import ModelForm
from django import forms
from .models import Reserva


class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = [ "nome_completo", "cpf", "data_reserva", "horario_reserva", "numero_mesa" , "quantidade_criança", "quantidade_adulto" ]
        widgets = {
            'data_reserva': forms.DateInput(attrs={'type': 'date'}),
            'horario_reserva': forms.TimeInput(attrs={'type': 'time'}),
        }
