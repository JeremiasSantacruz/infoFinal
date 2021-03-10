from django.urls import path
from apps.chat.views import NuevoChat, NuevoMensaje, VistaChat

app_name = 'chat'

urlpatterns = [
    path('nuevo/', NuevoChat.as_view(), name='crear'),
    path('<int:pk>', VistaChat.as_view(), name='vista'),
    path('<int:chat_pk>/mensaje', NuevoMensaje.as_view(), name='mensaje'),
]
