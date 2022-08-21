from django import forms
from .models import *

class AmbienteForm(forms.ModelForm):
    class Meta:
        model = Ambiente
        fields = ['nome', 'porta', 'inicio', 'metrosQuadrados']


class PortaForm(forms.ModelForm):
    class Meta:
        model = Porta
        fields = ['nome', 'largura', 'escada', 'ambienteAnterior', 'ambientePosterior'] 