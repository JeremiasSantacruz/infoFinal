from django.urls import path
from .views import RegistroUsuario, UsuarioLogin, UsuarioLogout

app_name = 'usuario'

urlpatterns = [
    path('registrar/', RegistroUsuario.as_view(), name="registro"),
    path('login/', UsuarioLogin.as_view(), name='login'),
    path('logout/', UsuarioLogout.as_view(), name='logout'),
]