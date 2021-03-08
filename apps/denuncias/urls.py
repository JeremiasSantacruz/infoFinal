from django.urls import path

from .views import CrearDenuncia, ConfirmacionDenuncia
app_name = 'denuncias'

urlpatterns = [
    path('<int:pub__id>/denuncia', CrearDenuncia.as_view(), name='crear'),
    path('gracias', ConfirmacionDenuncia.as_view(), name='gracias')
]