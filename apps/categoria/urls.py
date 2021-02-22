from django.urls import path 
from .views import listaCategoria, detalleCategoria

urlpatterns = [
    path('', listaCategoria.as_view()),
    path('<int:pk>', detalleCategoria.as_view(), name='detalle'),
]