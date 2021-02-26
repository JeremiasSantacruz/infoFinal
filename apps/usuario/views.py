from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .form import RegistroUsuarioForm
from .models import Usuario


# Create your views here.
class RegistroUsuario(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'usuario/usuario_registro.html'
    success_url = reverse_lazy('usuario:login')
