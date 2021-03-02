from django.urls import path

from .views import CrearPublicacion, DetallePublicacion

app_name="publicacion"

urlpatterns = [
    path('nueva', CrearPublicacion.as_view(), name='crear'),
    path('<int:pk>', DetallePublicacion.as_view(), name='detalle' )
]
