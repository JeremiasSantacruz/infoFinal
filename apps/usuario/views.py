from django.contrib.auth.views import (LoginView, LogoutView,
                                       PasswordResetDoneView,
                                       PasswordResetView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

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

class UsuarioResetPassword(PasswordResetView):
    template_name = 'usuario/reset.html'
    email_template_name = 'usuario/resetEmail.html'
    subject_template_name = 'usuario/resetSujeto.txt'
    success_url = reverse_lazy('usuario:pass_reset_done')

class UsuarioResetPasswordDone(PasswordResetDoneView):
    template_name = 'usuario/resetDone.html'

class UsuarioConfirmacionReset(PasswordResetConfirmView):
    template_name = 'usuario/passConfirm.html'
    success_url = reverse_lazy('usuario:pass_complete')

class UsuarioConfirmacionDone(PasswordResetCompleteView):
    template_name = 'usuario/passCompletado.html'
