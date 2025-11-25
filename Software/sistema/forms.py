from django import forms
from .models import Servico

class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['endereco', 'tipo_servico', 'descricao']
        widgets = {
            'tipo_servico': forms.Select(attrs={'class': 'form-select'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Ex: Rua das Flores, 123...'}),
            'descricao': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'endereco': 'Endereço Completo',
            'tipo_servico': 'Tipo de Serviço',
            'descricao': 'Descrição',
        }

class PropostaForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = ['data_visita', 'valor_hora']
        widgets = {
            'data_visita': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'valor_hora': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '0.00'}),
        }
        labels = {
            'data_visita': 'Data e Hora da Visita',
            'valor_hora': 'Valor por Hora (R$)',
        }