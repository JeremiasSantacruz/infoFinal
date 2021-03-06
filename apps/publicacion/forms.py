from django.core.exceptions import ValidationError
from django import forms 
from django.utils.translation import ugettext_lazy as _

from .models import Publicacion

class PostulanteForm(forms.ModelForm):
    class Meta:
        model =  Publicacion
        fields = ['postulantes']


        
class FinalizarForm(forms.ModelForm):
    class Meta:
        model =  Publicacion
        fields = ['responsable',]

    


