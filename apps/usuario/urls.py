from django.urls import path
from .views import RegistroUsuario

app_name = 'usuario'

urlpatterns = [
    path('registrar', RegistroUsuario.as_view(), name="registro"),
]