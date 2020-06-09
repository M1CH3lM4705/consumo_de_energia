from django.shortcuts import render

from ambientes.models import Ambiente

# Create your views here.


def listAmbiente(request):
    ambientes = Ambiente.objects.all()
    template_name = 'ambiente/lista_ambientes.html'
    context = {
        'ambientes':ambientes,
    }
    return render(request, template_name, context)
