from django.urls import path 
from .views import  crearCategoria, updateCategoria, listaCategoria, detalleCategoria, deleteCategoria

urlpatterns = [
    path('', listaCategoria.as_view(), name='categoria_lista'),
    path('nuevo/', crearCategoria.as_view(), name='categoria_crear' ), 
    path('<int:pk>/update', updateCategoria.as_view(), name='categoria_actualizar'),
    path('<int:pk/delete', deleteCategoria.as_view(), name='categoria_eliminar'),
    path('<int:pk>', detalleCategoria.as_view(), name='categoria_detalle'),
]