from django.shortcuts import render, redirect, get_object_or_404
from .forms import AparelhoForm, RelationForm
from django.contrib import messages
from .models import Aparelho, Aparelho_Ambiente

# Create your views here.

def calcSimulador(request):
    pass

#função que cadastra o aparalho
def cadastro_Aparelho(request):
    template_name = 'aparelhos/cadastro_aparelho.html'
    context = {}
    if request.method == 'POST':
        form = AparelhoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aparelho cadastrado com sucesso.')
            return redirect('aparelhos:lista_aparelhos')
    else:
        form = AparelhoForm()
    context['form'] = form
    return render(request, template_name, context)

#função que mostra uma lista de aparelhos
def lista_Aparelho(request):
    aparelhos = Aparelho.objects.all()
    context = {
        'aparelhos':aparelhos,
    }
    template_name = 'aparelhos/index.html'
    return render(request, template_name, context)

def edit_aparelho(request, pk):
    aparelho = get_object_or_404(Aparelho, pk=pk)
    
    if request.method == 'POST':
        form = AparelhoForm(request.POST, instance=aparelho)
        if form.is_valid():
            form.save()
            messages.success(request, 'Os dados foram alterados com sucesso')
            return redirect('aparelhos:index')
    else:
        form = AparelhoForm(instance=aparelho)
    template_name = 'aparelhos/editar_aparelho.html'
    context = {
        'form':form,
    }
    return render(request, template_name, context)

def deletar_aparelho(request, pk):
    aparelho = get_object_or_404(Aparelho, pk=pk)
    aparelho.delete()
    messages.success(request, 'Aparelho apagado com sucesso!')
    return redirect('aparelho:lista_aparelhos')


def relation(request):
    template_name = 'aparelhos/relations.html'
    context = {}
    if request.method == 'POST':
        form = RelationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aparelho adicionado ao ambiente com sucesso.')
            return redirect('aparelhos:lista_aparelhos')
    else:
        form = RelationForm()
    context['form'] = form
    return render(request, template_name, context)
