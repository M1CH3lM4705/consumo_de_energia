from django.shortcuts import render, redirect, get_object_or_404
from .forms import AparelhoForm
from django.contrib import messages
from .models import Aparelho
from .models import Ambiente

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