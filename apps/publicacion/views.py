from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy

from .models import Publicacion, Postulante
from .forms import PostulanteForm, FinalizarForm
from apps.chat.models import Chat


# Create your views here.
class CrearPublicacion(LoginRequiredMixin, CreateView):
    login_url = 'usuario:login'
    model = Publicacion
    template_name = 'publicacion/crear.html'
    fields = ['titulo', 'descripcion', 'categoria',  ]

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super(CrearPublicacion, self).form_valid(form)

class DetallePublicacion(DetailView):
    model = Publicacion
    template_name = 'publicacion/detalle.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['esPostulante'] = Postulante.objects.filter(publicacion= self.kwargs['pk'], usuario=self.request.user)
        return context
         

class PostularsePublicacion(LoginRequiredMixin, CreateView):
    """
    Agrega el usuarion logeado a la lista de postulantes de una publicacion.
    """
    model = Postulante
    template_name = 'publicacion/postularse.html'
    form_class = PostulanteForm

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.chat = Chat.objects.create(pub=form.instance.publicacion)
        return super().form_valid(form)


class FinalizarPublicacion(LoginRequiredMixin, UpdateView):
    """
    Finaliza/Reactiva la publicacion de un usuario logeado
    """
    model = Publicacion
    template_name = 'publicacion/finalizar.html'
    form_class = FinalizarForm
    
class UpdatePublicacion(LoginRequiredMixin, UpdateView):
    model = Publicacion
    template_name = 'publicacion/update.html'
    fields = ['titulo', 'descripcion', 'categoria',]

class ListaPublicacion(ListView):
    model = Publicacion
    context_object_name = 'publicaciones'
    template_name = 'publicacion/listaMain.html'
    queryset = Publicacion.custom.all()

class ListaPublicacionFinalizadas(ListView):
    model = Publicacion
    context_object_name = 'publicaciones'
    template_name = 'publicacion/listafinalizados.html'
    queryset = Publicacion.custom.finalizadas()
