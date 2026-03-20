from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .models import Cliente, Administrador, Chacara, Reserva


class IndexView(TemplateView):
    template_name = "website/modelo.html"

class ContatoView(TemplateView):
    template_name = "website/contato.html"

class SobreView(TemplateView):
    template_name = "website/sobre.html"


class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'telefone']  # 'usuario' será tratado em um fluxo de registro de usuário separado
    template_name = 'website/cliente_form.html' # Você precisará criar este template
    success_url = reverse_lazy('index') # Redireciona para a página inicial após o sucesso


class AdministradorCreate(CreateView):
    model = Administrador
    fields = ['nome']  # 'usuario' será tratado em um fluxo de registro de usuário separado
    template_name = 'website/administrador_form.html' # Você precisará criar este template
    success_url = reverse_lazy('index')


class ChacaraCreate(CreateView):
    model = Chacara
    fields = [
        'nome', 'descricao', 'preco_diaria', 'tem_estacionamento',
        'tem_piscina', 'tem_churrasqueira', 'num_quartos', 'num_banheiros'
    ]
    template_name = 'website/chacara_form.html' # Você precisará criar este template
    success_url = reverse_lazy('index')


class ReservaCreate(CreateView):
    model = Reserva
    fields = [
        'cliente', 'chacara', 'data_inicio', 'data_fim', 'valor_total', 'status'
    ]
    template_name = 'website/reserva_form.html' # Você precisará criar este template
    success_url = reverse_lazy('index')
