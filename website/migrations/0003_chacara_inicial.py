from django.db import migrations

DESCRICAO = (
    "Bem-vindo ao cantinho mais especial da família! "
    "O Sítio de Lurdes é um refúgio feito com carinho para quem quer descansar de verdade — "
    "longe da agitação, perto da natureza e dos bons momentos. "
    "Mergulhe na piscina, reúna todos na churrasqueira e aproveite cada instante com quem você ama. "
    "Com quartos aconchegantes, banheiros espaçosos e estacionamento para acomodar toda a turma, "
    "pensamos em cada detalhe para que você só precise se preocupar em curtir. "
    "Venha criar memórias inesquecíveis aqui com a gente!"
)


def criar_chacara(apps, schema_editor):
    Chacara = apps.get_model('website', 'Chacara')
    if not Chacara.objects.exists():
        Chacara.objects.create(
            nome='Sítio de Lurdes',
            descricao=DESCRICAO,
            preco_diaria='400.00',
            tem_estacionamento=True,
            tem_piscina=True,
            tem_churrasqueira=True,
            num_quartos=2,
            num_banheiros=2,
        )


def remover_chacara(apps, schema_editor):
    Chacara = apps.get_model('website', 'Chacara')
    Chacara.objects.filter(nome='Sítio de Lurdes').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0002_reserva_novos_campos'),
    ]

    operations = [
        migrations.RunPython(criar_chacara, remover_chacara),
    ]
