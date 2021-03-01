from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Usuario 

class RegistroUsuarioForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('zona', 'email', 'first_name', 'last_name')

class ActualizarUsuarioForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('zona', 'email', 'first_name', 'last_name')
