from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.urls import reverse

from apps.chat.models import Chat, Mensaje

# Create your views here.
class VistaChat(DetailView):
    model = Chat
    template_name = "chat/vista.html"

class NuevoChat(CreateView):
    model = Chat

class NuevoMensaje(CreateView):
    model = Mensaje
    fields = ['texto', 'log']
    template_name = 'chat/enviarMensaje.html'

    def form_valid(self, form):
        form.instance.send = self.request.user
        return super(NuevoMensaje, self).form_valid(form)
  