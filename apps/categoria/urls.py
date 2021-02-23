from django.urls import path 
from .views import  crearCategoria, updateCategoria, listaCategoria, detalleCategoria, deleteCategoria

app_name="categoria"

urlpatterns = [
    path('', listaCategoria.as_view(), name='lista'),
   # path('nuevo/', crearCategoria.as_view(), name='crear' ), 
   # path('<int:pk>/update', updateCategoria.as_view(), name='actualizar'),
   # path('<int:pk>/delete', deleteCategoria.as_view(), name='eliminar'),
    path('<int:pk>', detalleCategoria.as_view(), name='detalle'),
]