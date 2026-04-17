from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


class Cliente(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome Completo', help_text='Nome completo do cliente.')
    telefone = models.CharField(max_length=11, verbose_name='Telefone', help_text='Número de telefone (somente dígitos).')
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
    preco_diaria = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço da Diária', help_text='Preço por diária em reais.')
    tem_estacionamento = models.BooleanField(default=False, verbose_name='Tem Estacionamento', help_text='Indica se a chácara possui estacionamento.')
    tem_piscina = models.BooleanField(default=False, verbose_name='Tem Piscina', help_text='Indica se a chácara possui piscina.')
    tem_churrasqueira = models.BooleanField(default=False, verbose_name='Tem Churrasqueira', help_text='Indica se a chácara possui churrasqueira.')
    num_quartos = models.IntegerField(verbose_name='Número de Quartos', help_text='Quantidade de quartos disponíveis.')
    num_banheiros = models.IntegerField(verbose_name='Número de Banheiros', help_text='Quantidade de banheiros disponíveis.')

    class Meta:
        verbose_name = 'Chácara'
        verbose_name_plural = 'Chácaras'

    def __str__(self):
        return self.nome


class Reserva(models.Model):
    STATUS_PENDENTE = 'PENDENTE'
    STATUS_CONFIRMADA = 'CONFIRMADA'
    STATUS_RECUSADA = 'RECUSADA'
    STATUS_CANCELADA = 'CANCELADA'

    STATUS_CHOICES = [
        (STATUS_PENDENTE, 'Pendente'),
        (STATUS_CONFIRMADA, 'Confirmada'),
        (STATUS_RECUSADA, 'Recusada'),
        (STATUS_CANCELADA, 'Cancelada'),
    ]

    cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT,
        verbose_name='Cliente', help_text='Cliente que realizou o pedido de reserva.'
    )
    chacara = models.ForeignKey(
        Chacara, on_delete=models.PROTECT,
        verbose_name='Chácara', help_text='Chácara que está sendo reservada.'
    )
    data_inicio = models.DateField(
        verbose_name='Data de Início', help_text='Data de chegada na chácara.'
    )
    data_fim = models.DateField(
        verbose_name='Data de Fim', help_text='Data de saída da chácara.'
    )
    valor_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True,
        verbose_name='Valor Total', help_text='Calculado automaticamente: diária × número de dias.'
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDENTE,
        verbose_name='Status', help_text='Status atual da reserva.'
    )
    data_pedido = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Data do Pedido', help_text='Data e hora em que o pedido foi feito.'
    )
    data_decisao = models.DateTimeField(
        null=True, blank=True,
        verbose_name='Data da Decisão', help_text='Data e hora em que o pedido foi aprovado ou recusado.'
    )
    observacoes = models.TextField(
        blank=True,
        verbose_name='Observações', help_text='Descrição do evento ou informações adicionais para a administradora.'
    )

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        ordering = ['-data_pedido']

    def __str__(self):
        return f"Reserva de {self.cliente.nome} — {self.chacara.nome} ({self.data_inicio} a {self.data_fim})"

    def clean(self):
        if self.data_inicio and self.data_fim:
            if self.data_fim < self.data_inicio:
                raise ValidationError({'data_fim': 'A data de fim não pode ser anterior à data de início.'})

            conflitos = Reserva.objects.filter(
                chacara=self.chacara,
                status=self.STATUS_CONFIRMADA,
                data_inicio__lt=self.data_fim,
                data_fim__gt=self.data_inicio,
            )
            if self.pk:
                conflitos = conflitos.exclude(pk=self.pk)
            if conflitos.exists():
                raise ValidationError(
                    'Já existe uma reserva confirmada que se sobrepõe a estas datas. '
                    'Consulte o calendário de disponibilidade antes de escolher as datas.'
                )

    def save(self, *args, **kwargs):
        if self.data_inicio and self.data_fim and self.chacara_id:
            dias = (self.data_fim - self.data_inicio).days
            if dias > 0:
                self.valor_total = self.chacara.preco_diaria * dias
        super().save(*args, **kwargs)
