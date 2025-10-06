from django.urls import path
from . import views

app_name = "conograma"

urlpatterns = [
    path("", views.conograma ),

]

