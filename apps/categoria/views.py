from django.shortcuts import render
from .models import categoria
from django.views.generic import ListView

# Create your views here.
class listaCategoria(ListView):
    model = categoria
    template_name = 'categoria_list.html'