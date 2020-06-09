from django.shortcuts import render, redirect, get_object_or_404
from .forms import AparelhoForm
from django.contrib import messages
from .models import Aparelho

# Create your views here.

def calcSimulador(request):
    pass

#função que cadastra o aparalho
def cadastroAparelho(request):
    template_name = 'aparelhos/cadastro_aparelho.html'
    context = {}
    if request.method == 'POST':
        form = AparelhoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aparelho cadastrado com sucesso.')
            return redirect('aparelhos:lista-aparelhos')
    else:
        form = AparelhoForm()
    context['form'] = form
    return render(request, template_name, context)

#função que mostra uma lista de aparelhos
def detalheAparelho(request):
    aparelho = Aparelho.objects.all()
    context = {
        'aparelhos':aparelho
    }
    template_name = 'aparelhos/detalhes_aparelho.html'
    return render(request, template_name, context)