from django.db import models

class Ambiente(models.Model):
    nome = models.CharField(max_length=20, help_text='Entre o nome do ambiente')
    inicio = models.BooleanField(default=False)
    metrosQuadrados = models.FloatField(help_text='Metros quadrados do ambiente')
class Porta(models.Model):
    largura = models.FloatField(help_text='Tamanho da porta em metros')
    escada = models.BooleanField(help_text='Marque se tiver escada')
    conexao = models.ForeignKey('Conexao', on_delete=models.ForeignKey, null=True)
class Conexao(models.Model):
    ambienteAnterior = models.ForeignKey('Ambiente', null=True,  on_delete=models.DO_NOTHING, related_name='ambienteAnterior')
    ambientePosterior = models.ForeignKey('Ambiente', null=True,  on_delete=models.DO_NOTHING, related_name='ambientePosterior')
    peso = models.FloatField()