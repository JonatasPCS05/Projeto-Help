from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Servico(models.Model):
    TIPO_SERVICO_CHOICES = [
        ('pedreiro', 'Pedreiro'),
        ('marido_de_aluguel', 'Marido de Aluguel'),
        ('piscineiro', 'Piscineiro'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    endereco = models.CharField(max_length=255)
    tipo_servico = models.CharField(max_length=20, choices=TIPO_SERVICO_CHOICES)
    descricao = models.TextField()
    data_solicitacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.get_tipo_servico_display()} para {self.usuario.username} em {self.data_solicitacao.strftime("%d/%m/%Y")}'