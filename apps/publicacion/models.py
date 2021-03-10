from django.db import models
from django.conf import settings
from django.urls import reverse

# Create your models here.
class PublicacionManager(models.Manager):
    # Devuelve las publicaciones activas
    def get_queryset(self):
        return super(PublicacionManager, self).get_queryset().filter(responsable=None)

    # Devuelve Publicaciones finalizadas    
    def finalizadas(self):
        return super(PublicacionManager, self).get_queryset().exclude(responsable=None)

class Publicacion(models.Model):
    """
    Modelo de publicaciones de la apps
    """
    class Meta:
        db_table = 'publicacion'
        ordering = ('-fecha',)

    objects = models.Manager()
    custom = PublicacionManager()

    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING,
                                related_name="publicaciones")
    categoria = models.ForeignKey('categoria.Categoria', 
                                on_delete=models.SET_DEFAULT,
                                default='1',
                                related_name='publicaciones',
                                )
    titulo = models.CharField(max_length=50)
    activa = models.BooleanField(default=True)
    descripcion = models.TextField(max_length=200)
    responsable = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    on_delete=models.DO_NOTHING, 
                                    related_name='responsable',
                                    blank=True, null=True)
    fecha = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse('publicacion:detalle', kwargs={'pk': self.pk})
        
    def __str__(self):
        return self.titulo
    
class Postulante(models.Model):
    publicacion = models.ForeignKey('publicacion.Publicacion', on_delete=models.CASCADE,
                                    related_name='postulantes')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    chat = models.ForeignKey('chat.Chat', on_delete=models.CASCADE, related_name='datos')
    
    class Meta:
        unique_together = ('publicacion', 'usuario')
   
    def get_absolute_url(self):
        return reverse('publicacion:detalle', kwargs={'pk': self.publicacion.id}) 
    
    def __str__(self):
        return self.usuario.get_full_name() + ' Postulante para ' + self.publicacion.titulo
