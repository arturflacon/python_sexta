from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_lenght=11)