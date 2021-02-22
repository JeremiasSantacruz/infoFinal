from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import categoria

# Create your views here.
class listaCategoria(ListView):
    model = categoria
    template_name = 'categoria_list.html'

class detalleCategoria(DetailView):
    model = categoria
    template_name = 'categoria/detalleCategoria.html'

class crearCategoria(CreateView):
    model = categoria
    template_name = 'categoria/crearCategoria.html'
    fields = [
        'nombre',
        'desc',
    ]