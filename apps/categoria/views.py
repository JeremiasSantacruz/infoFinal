from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Categoria

# Create your views here.
class listaCategoria(ListView):
    model = Categoria
    template_name = 'categoria_list.html'
    context_object_name ="categorias"

class detalleCategoria(DetailView):
    model = Categoria
    template_name = 'categoria/detalleCategoria.html'

class crearCategoria(CreateView):
    model = Categoria
    fields = [
        'nombre',
        'desc',
    ]

    def get_success_url(self, **kwargs):
        return reverse_lazy('categoria:lista')

class updateCategoria(UpdateView):
    model = Categoria
    #success_url = reverse('categoria:lista')
    fields = [
        'nombre',
        'desc',
    ]

    def get_success_url(self, **kwargs):
        return reverse_lazy('categoria:lista')

class deleteCategoria(DeleteView):
    model = Categoria
    template_name = 'categoria/categoria_delete.html'
    success_url = reverse_lazy('categoria:lista')
