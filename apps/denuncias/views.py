from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse

from .models import Denuncias
from apps.publicacion.models import Publicacion

# Create your views here.
class CrearDenuncia(LoginRequiredMixin, CreateView):
    model = Denuncias
    fields = ['razon']
    template_name = 'denuncias/crear.html'

    def form_valid(self,  form):
        form.instance.denunciante = self.request.user
        pub = Publicacion.objects.filter(id=self.kwargs.get('pub__id')).first()
        print(pub, self.kwargs, self.request.user)
        form.instance.pub = pub
        form.instance.denunciado = pub.creador
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('denuncias:gracias')

class ConfirmacionDenuncia(LoginRequiredMixin, TemplateView):
    template_name = 'denuncias/gracias.html'
