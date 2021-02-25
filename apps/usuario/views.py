from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Usuario


# Create your views here.
class PerfilUsuario(DetailView):
    model = Usuario
    template_name = 'usuario/perfil.html'
    

class RegistroUsuario(CreateView):
    model = Usuario
    template_name = 'usuario/usuario_registro.html'
    fields = [
        'first_name',
        'last_name',
        'email',
        'direccion',
    ]

    def get_success_url(self):
        return reverse_lazy('usuario:login')

class ActualizarUsuario(UpdateView):
    model = Usuario
    fields = [
        'first_name',
        'last_name',
        'email',
        'direccion',
    ]

    def get_success_url(self):
        return reverse_lazy('usuario:perfil', kwargs={'pk': self.object.id})

class EliminarUsuario(DeleteView):
    model = Usuario
    success_url = reverse_lazy('Home')

#class LoginUsuario(LoginView):
#    model = Usuario