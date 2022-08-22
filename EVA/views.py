from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import AmbienteForm, PortaForm, ConexaoForm, PopulacaoForm
from .models import Ambiente, Porta, Conexao, Populacao
import igraph as ig


def adicionarAmbientes(request):
    if request.method == 'POST':
        formA = AmbienteForm(request.POST)
        formP = PopulacaoForm(request.POST)
        if formA.is_valid():
            formA.save()
            formP.save()
            return redirect('adicionarAmbiente')
    else:
        formA = AmbienteForm()
        formP = PopulacaoForm()
    context = {'formA': formA, 'formP': formP}
    return render(request, 'index.html', context)


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


def mostrarPortas(request):
    portas = Porta.objects.all().prefetch_related('conexao')
    context = {'portas': portas}
    return render(request, 'index3.html', context)


def calcFluxoMaximo():
    nos = []
    pesos = []
    qtd = []
    for x in Conexao.objects.all():
        nos.append((x.ambienteAnterior, x.ambientePosterior))
        pesos.append(int(x.peso))
        qtd.append(int(x.ambienteAnterior))

    tamanho = max(qtd)
    g = ig.Graph(
        tamanho, nos,
        directed=True
    )
    g.es['capacity'] = pesos
    flow = g.maxflow(0, tamanho - 1, capacity=g.es['capacity'])
    return int(flow.value)


def calcTempoEvacucao():
    aux = []
    for i in Populacao.objects.all():
        aux.append(i.populacao)

    pop = aux[-1]
    maxFlow = calcFluxoMaximo()
    return int(pop / (maxFlow * 6))


def fluxoMaximo(request):
    maxFlow = calcFluxoMaximo()
    tempo = calcTempoEvacucao()
    pop = (maxFlow * 6) * tempo
    context = {'maxFlow': maxFlow, 'tempo': tempo, 'pop': pop}
    return render(request, 'index4.html', context)
