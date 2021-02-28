from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView

from .forms import RegistroUsuarioForm
from .models import Usuario


# Create your views here.
class RegistroUsuario(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'usuario/registro.html'
    success_url = reverse_lazy('usuario:login')

class UsuarioLogin(LoginView): #Tengo que refactorar a LoginUsuario
    template_name = 'usuario/login.html'
    redirect_field_name = 'usuario/logout.html'

class UsuarioLogout(LogoutView):
    template_name = 'usuario/logout.html'


