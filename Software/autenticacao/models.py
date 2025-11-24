from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('comum', 'Usuário Comum'),
        ('autonomo', 'Autônomo'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(
        max_length=20,
        choices=TIPO_USUARIO_CHOICES,
        default='comum'
    )

    def __str__(self):
        return f"{self.usuario.username} ({self.get_tipo_usuario_display()})"
