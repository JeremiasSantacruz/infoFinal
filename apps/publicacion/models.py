from django.db import models
from ..categoria.models import Categoria
from django.conf import settings

# Create your models here.
class Publicacion(models.Model):
    """
    Modelo de publicaciones de la apps
    """
    class Meta:
        db_table = 'publicacion'

    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                related_name="publicaciones")
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    responsable = models.BooleanField(default=False)
    categoria = models.ForeignKey('categoria.Categoria', 
                                on_delete=models.SET_DEFAULT,
                                default='1',
                                related_name='publicaciones',
                                )
    # chat = models.ForeignKey('Chat', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
    