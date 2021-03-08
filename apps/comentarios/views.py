from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Comentario
from .forms import CreateComentForms

# Create your views here.
class HacerComentario(CreateView):
    model = Comentario
    template_name = 'comentarios/nuevo.html'
    form_class = CreateComentForms

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super(HacerComentario, self).form_valid(form)

class CambiarComentario(UpdateView):
    model = Comentario

class EliminarComentario(DeleteView):
    model = Comentario
