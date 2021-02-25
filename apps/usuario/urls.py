from django.urls import path
from .views import RegistroUsuario

urlpatterns = [
    path('registar', RegistroUsuario.as_view(), name="registro")
]