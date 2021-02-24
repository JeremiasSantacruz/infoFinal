from django.urls import path
from .views import (CrearCategoria, DeleteCategoria, DetalleCategoria,
                    ListaCategoria, UpdateCategoria)

app_name="categoria"

urlpatterns = [
    path('', ListaCategoria.as_view(), name='lista'),
    #path('nuevo/', CrearCategoria.as_view(), name='crear' ), 
    #path('<int:pk>/update', UpdateCategoria.as_view(), name='actualizar'),
    #path('<int:pk>/delete', DeleteCategoria.as_view(), name='eliminar'),
    path('<int:pk>', DetalleCategoria.as_view(), name='detalle'),
]
