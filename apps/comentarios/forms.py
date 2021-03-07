from django import forms

from .models import Comentario

class CreateComentForms(forms.ModelChoiceField):
    class Meta:
        model = Comentario
        fields = ['texto', 'pub', 'hacia']

    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.pop('user', None)
    #     super(CreateComentForms, self).__init__(*args, **kwargs)

    # def clean_hacia(self, form):
    #     hacia = self.cleaned_data[ 'hacia' ]
    #     if self.user:
    #         aut = self.user.id
    #         if aut == hacia:
    #             raise forms.ValidationError('No puedes comentarte a ti mismo') 
    #     return hacia
