from django import forms
from aparelhos.models import Aparelho

#criação do formulario de preenchimento do aparelho.

class AparelhoForm(forms.ModelForm):

    class Meta:
        model = Aparelho
        fields = ['name', 'potencia', 'tempo']
