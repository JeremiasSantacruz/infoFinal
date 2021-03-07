from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class UsuarioManager(models.Manager):
    def finalizadas(self):
        return super(UsuarioManager, self).get_queryset().filter(responsable__isnull=False)
# Create your models here.
class Usuario(AbstractUser):
    puntuacion = models.IntegerField(default=0)
    zona = models.CharField(max_length=70)
    objects = UsuarioManager()

    REQUIRED_FIELDS = ['first_name', 'last_name', 'zona' ]

    def __str__(self):
        return self.first_name + self.last_name
    

    def get_absolute_url(self):
        """
        Obtengo la url del objeto
        """
        return reverse('usuario:perfil', kwargs={'pk':self.pk} )
    
    def puntuacion_prom(self):
        puntuacion = 0
        for coment in self.comentariosRecibidos.all():
            puntuacion = coment.puntuacion + puntuacion
        return puntuacion/self.comentariosRecibidos.count()