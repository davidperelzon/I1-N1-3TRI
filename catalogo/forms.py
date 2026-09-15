from django import forms
from .models import Bolo

class BoloForm(forms.ModelForm):
    class Meta:
        model = Bolo
        fields = ['nome', 'sabor', 'ingredientes', 'descricao', 'preco', 'disponivel']
        labels = {
            'nome': 'Nome do bolo',
            'sabor': 'Sabor',
            'ingredientes': 'Ingredientes',
            'descricao': 'Descrição',
            'preco': 'Preço',
            'disponivel': 'Disponível',
        }
        widgets = {
            'ingredientes': forms.Textarea(attrs={'rows': 4}),
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }
