from django.db import models
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    """
    Categoria que define el tipo de las publicaciones.
    """
    nombre = models.CharField(max_length=25)
    desc = models.CharField(max_length=60)

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        """
        Cuando updateView y CreateView son existosa en ves de definir el succes_url
        esas clase usan get_absolute_url
        """
        return reverse('categoria:detalle', kwargs={'pk':self.pk} )