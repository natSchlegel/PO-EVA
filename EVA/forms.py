from django import forms
from .models import Ambiente, Porta


class AmbienteForm(forms.ModelForm):
    class Meta:
        model = Ambiente
        fields = ['nome', 'metrosQuadrados']


class PortaForm(forms.ModelForm):
    class Meta:
        model = Porta
        fields = ['largura', 'escada']
