from django import forms
from .models import Ambiente, Porta, Conexao, Populacao


class AmbienteForm(forms.ModelForm):
    class Meta:
        model = Ambiente
        fields = ['nome', 'metrosQuadrados']


class PortaForm(forms.ModelForm):
    class Meta:
        model = Porta
        fields = ['largura', 'escada']


class ConexaoForm(forms.ModelForm):
    class Meta:
        model = Conexao
        fields = ['ambientePosterior', 'ambienteAnterior', 'peso']


class PopulacaoForm(forms.ModelForm):
    class Meta:
        model = Populacao
        fields = ['populacao']
