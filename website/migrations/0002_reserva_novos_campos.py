import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        # Novos campos
        migrations.AddField(
            model_name='reserva',
            name='data_pedido',
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                help_text='Data e hora em que o pedido foi feito.',
                verbose_name='Data do Pedido',
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva',
            name='data_decisao',
            field=models.DateTimeField(
                blank=True,
                null=True,
                help_text='Data e hora em que o pedido foi aprovado ou recusado.',
                verbose_name='Data da Decisão',
            ),
        ),
        migrations.AddField(
            model_name='reserva',
            name='observacoes',
            field=models.TextField(
                blank=True,
                default='',
                help_text='Descrição do evento ou informações adicionais para a administradora.',
                verbose_name='Observações',
            ),
            preserve_default=False,
        ),
        # valor_total agora é nullable (calculado automaticamente)
        migrations.AlterField(
            model_name='reserva',
            name='valor_total',
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text='Calculado automaticamente: diária × número de dias.',
                max_digits=10,
                null=True,
                verbose_name='Valor Total',
            ),
        ),
        # Atualiza choices: remove CONCLUIDA, adiciona RECUSADA
        migrations.AlterField(
            model_name='reserva',
            name='status',
            field=models.CharField(
                choices=[
                    ('PENDENTE', 'Pendente'),
                    ('CONFIRMADA', 'Confirmada'),
                    ('RECUSADA', 'Recusada'),
                    ('CANCELADA', 'Cancelada'),
                ],
                default='PENDENTE',
                help_text='Status atual da reserva.',
                max_length=20,
                verbose_name='Status',
            ),
        ),
        # Adiciona ordering
        migrations.AlterModelOptions(
            name='reserva',
            options={
                'ordering': ['-data_pedido'],
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
            },
        ),
    ]
