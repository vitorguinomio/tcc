from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def cronograma(request):
    return render(request, 'cronograma/cronograma.html')