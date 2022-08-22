from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import AmbienteForm, PortaForm, ConexaoForm
from .models import Ambiente, Porta, Conexao
import igraph as ig


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


def calcFluxoMaximo():
    pesos = Conexao.object.peso()
    nos = Conexao.object.nos()
    qtd = Conexao.object.qtd()
    g = ig.Graph(
        qtd, [nos],
        directed=True
    )
    g.es['capacity'] = [pesos]
    flow = g.maxflow(0, 11, capacity=g.es['capacity'])
    return flow.value


def fluxoMaximo(request):
    maxFlow = calcFluxoMaximo()
    return render(request, 'index3.html', {'maxFlow': maxFlow})
