from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class Usuario(AbstractUser):
    puntuacion = models.IntegerField(default=0)
    zona = models.CharField(max_length=70)
    # postulante = models.ForeignKey('publicacion.Publicacion', on_delete=models.CASCADE,
    #                                 related_name='postulantes')
    
    REQUIRED_FIELDS = ['first_name', 'last_name', 'zona' ]

    def __str__(self):
        return self.first_name + self.last_name
    

    def get_absolute_url(self):
        """
        Obtengo la url del objeto
        """
        return reverse('usuario:perfil', kwargs={'pk':self.pk} )