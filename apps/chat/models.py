from django.db import models
from django.conf import settings

# Create your models here.
class Chat(models.Model):
    postulante = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    pub = models.ForeignKey('publicacion.Publicacion', on_delete=models.CASCADE)


class Mensaje(models.Model):
    class Meta:
        ordering = ('-fecha',)

    fecha = models.DateTimeField(auto_now=False, auto_now_add=True)
    send = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    texto = models.TextField(max_length=200)
    log = models.ForeignKey(Chat, on_delete=models.CASCADE,
                            related_name='mensajes')

