from django import forms
from aparelhos.models import Aparelho, Aparelho_Ambiente

#criação do formulario de preenchimento do aparelho.

class AparelhoForm(forms.ModelForm):

    class Meta:
        model = Aparelho
        fields = ['name', 'potencia']



class RelationForm(forms.ModelForm):

    class Meta:
        model = Aparelho_Ambiente
        fields = ['ambiente', 'aparelho', 'quantidade', 'tempo', 'status']

    

