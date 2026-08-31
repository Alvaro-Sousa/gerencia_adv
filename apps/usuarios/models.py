from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuarios(AbstractUser):
    class TipoUsuario(models.TextChoices):
        CLIENTE = "CLIENTE", "Cliente"
        ADVOGADO = "ADVOGADO", "Advogado"

    username = None
    email = models.EmailField(unique=True)
    tipo_usuario = models.CharField(
        max_length=20,
        choices=TipoUsuario.choices,
        default=TipoUsuario.CLIENTE,
    )
    atualizado_em = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.get_full_name() or self.email