from django import forms
from core.models import Produto

#11 - Formulário COM integração ao Banco de Dados  (forms.ModelForm = vinculado ao modelo Produto)
class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco']
