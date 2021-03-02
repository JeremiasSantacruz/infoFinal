from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import CreateView, DetailView

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

class DetallePublicacion(DetailView):
    model = Publicacion
    template_name = 'publicacion/detalle.html'

    def post(self, request, *arg, **kwargs):
        if request.user.is_authenticated :
            pub = super(DetallePublicacion, self).get_object()
            if request.user != pub.creador :
                pub.postulantes.add(self.request.user) 
            return render(request, 'publicacion:detalle')
        return {'message': 'error '}
