from django.db import models
from django.conf import settings
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Comentario(models.Model):
    texto = models.TextField(max_length=400)
    puntuacion =models.IntegerField(
        default=6,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
     )

    pub = models.ForeignKey('publicacion.Publicacion', on_delete=models.CASCADE,
                            related_name='comentarios')
    hacia = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                related_name="comentariosRecibidos") 
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                related_name="comentariosHechos") 
    fecha = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ('-fecha',)
    
    def get_absolute_url(self):
        return reverse('publicacion:detalle', kwargs={'pk': self.pub.id})

