from django.urls import path

from .views import (RegistroUsuario, UsuarioLogin, UsuarioLogout,
                    UsuarioResetPassword, UsuarioResetPasswordDone,
                    UsuarioConfirmacionReset, UsuarioConfirmacionDone,
                    Perfil, ActualizarUsuario, FinalizadasUsuario)

app_name = 'usuario'

urlpatterns = [
    path('registrar/', RegistroUsuario.as_view(), name="registro"),
    path('login/', UsuarioLogin.as_view(), name='login'),
    path('logout/', UsuarioLogout.as_view(), name='logout'),
    path('<int:pk>/', Perfil.as_view(), name='perfil'),
    path('<int:pk>/up', ActualizarUsuario.as_view(), name='actualizar'),
    path('<int:pk>/finalizadas', FinalizadasUsuario.as_view(), name='finalizadas'),
    # Direcciones para el reseteo de contrasenia
    path('pass_reset/', UsuarioResetPassword.as_view() ,name='password_reset'),
    path('pass_reset_done/', UsuarioResetPasswordDone.as_view(), name='pass_reset_done' ),
    path('<uidb64>/<token>/', UsuarioConfirmacionReset.as_view(), name='pass_confirm'),
    path('pass_reset/done', UsuarioConfirmacionDone.as_view(), name='pass_complete'),
]
