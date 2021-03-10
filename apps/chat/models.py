from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class Chat(models.Model):
    pub = models.ForeignKey('publicacion.Publicacion', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse ('chat:vista', kwargs={'pk': self.pk})
    
    def __str__(self):
        return 'Chat de ' + self.datos.get().usuario.get_full_name() + ' para ' + self.pub.titulo

class Mensaje(models.Model):
    class Meta:
        ordering = ('fecha',)

    fecha = models.DateTimeField(auto_now=False, auto_now_add=True)
    send = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    texto = models.TextField(max_length=200)
    log = models.ForeignKey('chat.Chat', on_delete=models.CASCADE,
                            related_name='mensajes')

    def get_absolute_url(self):
        return reverse ('chat:vista', kwargs={'pk': self.log.id})

