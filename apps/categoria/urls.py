from django.urls import path 
from .views import listaCategoria, detalleCategoria, crearCategoria

urlpatterns = [
    path('', listaCategoria.as_view(), name='lista'),
    path('<int:pk>', detalleCategoria.as_view(), name='detalle'),
    path('nuevo/', crearCategoria.as_view(), name='crear' ), 
]