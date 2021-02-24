from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Categoria


# Create your views here.
class ListaCategoria(ListView):
    """
    Vista generica que lista todas las categorias
    """
    model = Categoria
    context_object_name ="categorias"

class DetalleCategoria(DetailView):
    """
    Vista generica de detalle, listando todas las publicaciones
    """
    model = Categoria
    template_name = 'categoria/detalleCategoria.html'

class CrearCategoria(CreateView):
    """
    Formulario generico, deprecaded
    """
    model = Categoria
    fields = [
        'nombre',
        'desc',
    ]

class UpdateCategoria(UpdateView):
    """
    Formulario generico, deprecaded
    """
    model = Categoria
    #success_url = reverse('categoria:lista')
    fields = [
        'nombre',
        'desc',
    ]

class DeleteCategoria(DeleteView):
    """
    Formulario generico, deprecaded
    """
    model = Categoria
    template_name = 'categoria/categoria_delete.html'
    success_url = reverse_lazy('categoria:lista')
