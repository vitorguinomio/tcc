from django.db import models


# Create your models here.
class Reserva(models.Model):
    nome_completo = models.CharField(max_length= 255)
    cpf = models.CharField(max_length=11)
    data_reserva = models.DateField()
    horario_reserva = models.TimeField()
    numero_mesa = models.IntegerField()
    quantidade_adulto = models.IntegerField()
    quantidade_criança = models.IntegerField()
    data_criação = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reserva de {self.nome_completo} para o dia {self.data_reserva}"
