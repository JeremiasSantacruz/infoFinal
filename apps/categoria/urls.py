from django.urls import path 
from .views import listaCategoria

urlpatterns = [
    path('list', listaCategoria.as_view())
]