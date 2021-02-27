from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    puntuacion = models.IntegerField(default=0)
    direccion = models.CharField(max_length=70)
    
    REQUIRED_FIELDS = ['direccion']

    def __str__(self):
        return self.first_name + self.last_name
    