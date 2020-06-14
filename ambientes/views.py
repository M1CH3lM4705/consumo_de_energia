from django.shortcuts import render, get_object_or_404, redirect
from ambientes.models import Ambiente
from aparelhos.forms import AparelhoForm
from .forms import AmbienteForm
from django.contrib import messages

# Create your views here.


def index(request):
    ambientes = Ambiente.objects.all()
    template_name = 'ambientes/index.html'
    context = {
        'ambientes':ambientes,
    }
    return render(request, template_name, context)

def Cadastrar_ambiente(request):
    template_name = 'ambientes/cadastro_ambiente.html'
    ambientes = Ambiente.objects.all()
    context = {}
    if request.method == 'POST':
        form = AmbienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success = (request, 'Ambiente cadastrado com sucesso!')
            return redirect('ambientes:index')
    else:
        form = AmbienteForm()
    context = {
        'form':form,
        'ambientes':ambientes
    }
    return render(request, template_name, context)

def editar_ambiente(request, pk):
    ambientes = get_object_or_404(Ambiente, pk=pk)

    if request.method == 'POST':
        form = AmbienteForm(request.POST, instance=ambientes)
        if form.is_valid():
            form.save()
            messages.success = (request, 'Ambiente alterado com sucesso!')
            return redirect('ambientes:index')
    else:
        form = AmbienteForm(instance=ambientes)
    template_name = 'ambientes/update_ambiente.html'
    context = {
        'form':form,
    }
    return render(request, template_name, context)



def deletar_ambiente(request, pk):
    ambientes = get_object_or_404(Ambiente, pk=pk)
    ambientes.delete()
    return redirect('ambientes:index')


def select_ambiente(request, slug):
    ambiente = get_object_or_404(Ambiente, slug=slug)
    context = {}
    template_name = 'aparelhos/lista_aparelho.html'
    if request.method == 'POST':
        form = AparelhoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aparelho cadastrado com sucesso!')
            return redirect('aparelhos:lista-aparelhos')
    else:
        form = AparelhoForm()
    context['form'] = form
    context['ambiente'] = ambiente
    return render(request, template_name, context)
