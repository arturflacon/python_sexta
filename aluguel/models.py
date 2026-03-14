from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome Completo', help_text='Nome completo do cliente.')
    telefone = models.CharField(max_length=20, verbose_name='Telefone', help_text='Número de telefone do cliente.')
    usuario = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='Usuário', help_text='Usuário associado a este cliente.')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome


class Administrador(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome Completo', help_text='Nome completo do administrador.')
    usuario = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='Usuário', help_text='Usuário associado a este administrador.')

    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'

    def __str__(self):
        return self.nome


class Chacara(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome da Chácara', help_text='Nome da chácara para aluguel.')
    descricao = models.TextField(verbose_name='Descrição', help_text='Descrição detalhada da chácara.')
    preco_diaria = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço da Diária', help_text='Preço da diária de aluguel da chácara.')
    num_quartos = models.IntegerField(verbose_name='Número de Quartos', help_text='Quantidade de quartos disponíveis na chácara.')
    num_banheiros = models.IntegerField(verbose_name='Número de Banheiros', help_text='Quantidade de banheiros disponíveis na chácara.')

    class Meta:
        verbose_name = 'Chácara'
        verbose_name_plural = 'Chácaras'

    def __str__(self):
        return self.nome


class Reserva(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('CONFIRMADA', 'Confirmada'),
        ('CANCELADA', 'Cancelada'),
        ('CONCLUIDA', 'Concluída'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name='Cliente', help_text='Cliente que realizou a reserva.')
    chacara = models.ForeignKey(Chacara, on_delete=models.PROTECT, verbose_name='Chácara', help_text='Chácara reservada.')
    data_inicio = models.DateField(verbose_name='Data de Início', help_text='Data de início da reserva.')
    data_fim = models.DateField(verbose_name='Data de Fim', help_text='Data de término da reserva.')
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Total', help_text='Valor total da reserva.')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE', verbose_name='Status', help_text='Status atual da reserva.')

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return f"Reserva de {self.cliente.nome} para {self.chacara.nome} ({self.data_inicio} a {self.data_fim})"
