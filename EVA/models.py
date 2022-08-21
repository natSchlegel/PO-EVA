from django.db import models

class Ambiente(models.Model):
    nome = models.CharField(max_length=20, help_text='Entre o nome do ambiente')
    inicio = models.BooleanField()
    metrosQuadrados = models.FloatField(help_text='Metros quadrados do ambiente')
    ambientePosterior = models.ForeignKey('Ambiente', null=True,  on_delete=models.DO_NOTHING)
    porta = models.ForeignKey('Porta', on_delete=models.DO_NOTHING)

class Porta(models.Model):
    nome = models.CharField(max_length=20, help_text='Identificador da porta')
    largura = models.FloatField(help_text='Tamanho da porta em metros')
    escada = models.BooleanField(help_text='Marque se tiver escada')

