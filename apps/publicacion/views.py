from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Publicacion
# Create your views here.
class CrearPublicacion(LoginRequiredMixin, CreateView):
    login_url = 'usuario:login'
    model = Publicacion
    template_name = 'publicacion/crear.html'
    fields = ['titulo', 'descripcion', 'categoria', 'responsable', ]

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super(CrearPublicacion, self).form_valid(form)
