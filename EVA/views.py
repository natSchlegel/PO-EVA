from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Ambiente, Porta

def adicionarAmbientes(request):
    return render(request, 'index.html')
def adicionarPortas(request):
    ambientes = Ambiente.objects.all()
    template = loader.get_template('index2.html')
    context = {'ambientes':ambientes}
    return HttpResponse(template.render(context, request))