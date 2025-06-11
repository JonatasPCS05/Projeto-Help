from django import forms
from .models import Servico

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['endereco', 'tipo_servico', 'descricao']

        widgets = {
            'tipo_servico': forms.Select(attrs={'class': 'form-select'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Ex: Rua das Flores, 123, Bairro, Cidade - RJ'}),
            'descricao': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Descreva em detalhes o que precisa ser feito.'}),
        }

        labels = {
            'endereco': 'Endereço Completo para o Serviço',
            'tipo_servico': 'Qual serviço você precisa?',
            'descricao': 'Descrição Detalhada',
        }