from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    puntuacion = models.IntegerField(default=0)
    direccion = models.CharField(max_length=70)
    