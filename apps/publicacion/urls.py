from django.urls import path

from .views import CrearPublicacion
app_name="publicacion"

urlpatterns = [
    path('nueva', CrearPublicacion.as_view(), name='crear'),
]
