from django.db import models
from django.contrib.auth.models import User

class Servico(models.Model):
    TIPO_SERVICO_CHOICES = [
        ('pedreiro', 'Pedreiro'),
        ('marido_de_aluguel', 'Marido de Aluguel'),
        ('piscineiro', 'Piscineiro'),
    ]
    
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('proposta_enviada', 'Proposta Enviada'),
        ('pendente', 'Pendente'),
        ('concluido', 'Concluído'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='solicitacoes')
    autonomo = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='servicos_atendidos')
    recusado_por = models.ManyToManyField(User, related_name='vagas_recusadas', blank=True)
    
    endereco = models.CharField(max_length=255)
    tipo_servico = models.CharField(max_length=20, choices=TIPO_SERVICO_CHOICES)
    descricao = models.TextField()
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberto')
    data_visita = models.DateTimeField(null=True, blank=True)
    valor_hora = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f'{self.get_tipo_servico_display()} - {self.status}'