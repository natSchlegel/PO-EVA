from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .forms import PortaForm, AmbienteForm

from .models import Ambiente, Porta


def adicionarAmbientes(request):
    if request.method == "POST":
        form = AmbienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adicionarAmbiente')
    else:
        form = AmbienteForm()
    return render(request, 'index.html', {'form': form})


def adicionarPortas(request):
    ambientes = Ambiente.objects.all()
    template = loader.get_template('index2.html')
    context = {'ambientes': ambientes}
    return HttpResponse(template.render(context, request))
