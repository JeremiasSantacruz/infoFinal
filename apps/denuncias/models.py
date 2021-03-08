from django.db import models
from django.conf import settings
from django.urls import reverse


# Create your models here.
class Denuncias(models.Model):

    class Meta:
        ordering = ('-fecha',)

    denunciado = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                        related_name='denunciado')
    denunciante = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                        related_name='denunciante')
    pub = models.ForeignKey('publicacion.Publicacion', on_delete=models.CASCADE)
    razon = models.TextField(max_length=200)
    fecha = models.DateTimeField(auto_now=False, auto_now_add=True)
    activa = models.BooleanField(default=True)
    