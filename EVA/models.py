from django.db import models

class Ambiente(models.Model):
    nome = models.CharField(max_length=20, help_text='Entre o nome do ambiente')
    porta = models.ForeignKey('Porta', on_delete=models.DO_NOTHING)
    inicio = models.BooleanField()
    metrosQuadrados = models.FloatField(help_text='Metros quadrados do ambiente')

class Porta(models.Model):
    nome = models.CharField(max_length=20, help_text='Identificador da porta')
    largura = models.FloatField(help_text='Tamanho da porta em metros')
    escada = models.BooleanField(help_text='Marque se tiver escada')
    ambienteAnterior = models.ForeignKey('Ambiente', on_delete=models.DO_NOTHING)
    ambientePosterior = models.ForeignKey('Ambiente', on_delete=models.DO_NOTHING)


