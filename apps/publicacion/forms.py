from django.core.exceptions import ValidationError
from django import forms 
from django.utils.translation import ugettext_lazy as _

from .models import Publicacion, Postulante

class PostulanteForm(forms.ModelForm):
    class Meta:
        model =  Postulante
        fields = ['publicacion']


        
class FinalizarForm(forms.ModelForm):
    class Meta:
        model =  Publicacion
        fields = ['responsable',]

    


