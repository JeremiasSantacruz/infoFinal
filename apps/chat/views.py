from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.urls import reverse

from apps.chat.models import Chat, Mensaje

# Create your views here.
class VistaChat(DetailView):
    model = Chat

class NuevoChat(CreateView):
    model = Chat

class NuevoMensaje(CreateView):
    model = Mensaje

    def get_success_url(self):
        return reverse('chat:vista', kwargs={'pub__id': self.chat.pub.id; 'post_id': self.chat.postulante.id})
