from django.urls import path

from .views import (CrearPublicacion, DetallePublicacion, FinalizarPublicacion,
                    PostularsePublicacion, UpdatePublicacion, ListaPublicacion,
                    ListaPublicacionFinalizadas)

app_name="publicacion"

urlpatterns = [
    path('pub/nueva', CrearPublicacion.as_view(), name='crear'),
    path('', ListaPublicacion.as_view(), name='lista'),
    path('pub/<int:pk>', DetallePublicacion.as_view(), name='detalle' ),
    path('pub/<int:pk>/postularse', PostularsePublicacion.as_view(), name='postularse'),
    path('pub/<int:pk>/finalizar', FinalizarPublicacion.as_view(), name='finalizar'),
    path('pub/<int:pk>/update', UpdatePublicacion.as_view(), name='actualizar'),
    path('pub/finalizados', ListaPublicacionFinalizadas.as_view(), name='finalizados'),
]
