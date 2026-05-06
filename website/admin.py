from django.contrib import admin

from .models import Administrador, Chacara, Cliente, Reserva


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'usuario']
    search_fields = ['nome', 'telefone', 'usuario__username']


@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'usuario']
    search_fields = ['nome', 'usuario__username']


@admin.register(Chacara)
class ChacaraAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco_diaria', 'num_quartos', 'num_banheiros', 'tem_piscina', 'tem_churrasqueira', 'tem_estacionamento']
    search_fields = ['nome']
    list_filter = ['tem_piscina', 'tem_churrasqueira', 'tem_estacionamento']


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'chacara', 'data_inicio', 'data_fim', 'valor_total', 'status', 'data_pedido']
    list_filter = ['status', 'chacara']
    search_fields = ['cliente__nome', 'chacara__nome']
    date_hierarchy = 'data_inicio'
    readonly_fields = ['data_pedido', 'valor_total']

