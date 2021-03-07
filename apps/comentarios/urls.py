from django.urls import path
from .views import CambiarComentario, HacerComentario, EliminarComentario

app_name="comentario"

urlpatterns = [
    path('', HacerComentario.as_view(), name='nuevo'),
    path('<int:pk>/cambiar', CambiarComentario.as_view(), name='cambiar'),
    path('<int:pk>/eliminar', EliminarComentario.as_view(), name='eliminar'),
]