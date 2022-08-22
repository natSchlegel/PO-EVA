from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import AmbienteForm, PortaForm, ConexaoForm
from .models import Ambiente, Porta, Conexao


def adicionarAmbientes(request):
    if request.method == 'POST':
        formA = AmbienteForm(request.POST)
        if formA.is_valid():
            formA.save()
            return redirect('adicionarAmbiente')
    else:
        formA = AmbienteForm()
    return render(request, 'index.html', {'formA': formA})


def adicionarPortas(request):
    ambienteAnterior = Ambiente.objects.all()
    ambientePosterior = Ambiente.objects.all()
    ambiente = Ambiente.objects.all()
    if request.method == 'POST':
        adicionarConexao(request)
        formP = PortaForm(request.POST)
        if formP.is_valid():
            formP.save()
            return redirect('adicionarPortas')
    else:
        formP = PortaForm()
    context = {'ambienteAnterior': ambienteAnterior, 'ambientePosterior': ambientePosterior, 'ambiente': ambiente,
               'formP': formP}
    return render(request, 'index2.html', context)


def adicionarConexao(request):
    if request.method == 'POST':
        formC = ConexaoForm(request.POST)
        if formC.is_valid():
            formC.save()
