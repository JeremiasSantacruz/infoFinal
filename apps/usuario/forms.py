from django.contrib.auth.forms import UserCreationForm

from .models import Usuario 

class RegistroUsuarioForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = UserCreationForm.Meta.fields + ('direccion', 'email', 'first_name', 'last_name')