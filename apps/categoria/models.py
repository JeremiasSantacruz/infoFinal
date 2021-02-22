from django.db import models

# Create your models here.
class categoria(models.Model):
    nombre = models.CharField(max_length=25)
    desc = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre