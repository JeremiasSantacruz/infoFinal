from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from .forms import ActualizarUsuarioForm, RegistroUsuarioForm
from .models import Usuario


# Create your views here.
class RegistroUsuario(CreateView):
    form_class = RegistroUsuarioForm
    template_name = 'usuario/registro.html'
    success_url = reverse_lazy('usuario:login')

class UsuarioLogin(LoginView): #Tengo que refactorar a LoginUsuario
    template_name = 'usuario/login.html'

class UsuarioLogout(LogoutView):
    template_name = 'usuario/logout.html'

# Vista de usuario
class Perfil(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = 'usuario/perfil.html'

class FinalizadasUsuario(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = 'usuario/listafinalizados.html'


    def get_queryset(self, **kwargs):
        queryset = Usuario.objects.filter(id=self.kwargs['pk'], 
                                            publicaciones__responsable__isnull=False)
        return queryset
    
class ActualizarUsuario(LoginRequiredMixin, UpdateView):
    login_url = 'user/login.html'
    template_name = 'usuario/actualizar.html'
    model = Usuario
    fields = [
        'first_name', 'last_name', 'email', 'zona', 
    ]

    def get_success_url(self):
        return  reverse_lazy('usuario:perfil', args= [self.object.id] )

# Clases para la resetear la contrasenas
class UsuarioResetPassword(PasswordResetView):
    """
    Vista para resetear contrasenia, manda email a la consola
    """
    template_name = 'usuario/reset.html'
    email_template_name = 'usuario/resetEmail.html'
    subject_template_name = 'usuario/resetSujeto.txt'
    success_url = reverse_lazy('usuario:pass_reset_done')

class UsuarioResetPasswordDone(PasswordResetDoneView):
    """
    Vista cuando se envia el mail.
    """
    template_name = 'usuario/resetDone.html'

class UsuarioConfirmacionReset(PasswordResetConfirmView):
    """
    Usamos el, formulario por defecto para cambiar la contrasenia dado el token
    """
    template_name = 'usuario/passConfirm.html'
    success_url = reverse_lazy('usuario:pass_complete')

class UsuarioConfirmacionDone(PasswordResetCompleteView):
    """
    Por fin terminamos y guardamos la contrasenia
    """
    template_name = 'usuario/passCompletado.html'
