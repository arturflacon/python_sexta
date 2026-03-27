from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente, Administrador, Chacara, Reserva


class IndexView(TemplateView):
    template_name = "website/index.html"

class ContatoView(TemplateView):
    template_name = "website/contato.html"

class SobreView(TemplateView):
    template_name = "website/sobre.html"


class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'telefone', 'usuario']
    template_name = 'website/cliente_form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastro de Cliente',
        'botao': 'Cadastrar Cliente'
    }

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['nome', 'telefone']
    template_name = 'website/cliente_form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Editar Cliente',
        'botao': 'Salvar Alterações'
    }


class AdministradorCreate(CreateView):
    model = Administrador
    fields = ['nome', 'usuario']
    template_name = 'website/administrador_form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastro de Administrador',
        'botao': 'Cadastrar Administrador'
    }


class ChacaraCreate(CreateView):
    model = Chacara
    fields = [
        'nome', 'descricao', 'preco_diaria', 'tem_estacionamento',
        'tem_piscina', 'tem_churrasqueira', 'num_quartos', 'num_banheiros'
    ]
    template_name = 'website/chacara_form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Cadastro de Chácara',
        'botao': 'Cadastrar Chácara'
    }

class ChacaraUpdate(UpdateView):
    model = Chacara
    fields = [
        'nome', 'descricao', 'preco_diaria', 'tem_estacionamento',
        'tem_piscina', 'tem_churrasqueira', 'num_quartos', 'num_banheiros'
    ]
    template_name = 'website/chacara_form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Editar Chácara',
        'botao': 'Salvar Alterações'
    }

class ChacaraDelete(DeleteView):
    model = Chacara
    template_name = 'website/chacara_confirm_delete.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Excluir Chácara',
        'botao': 'Confirmar Exclusão'
    }


class ReservaCreate(CreateView):
    model = Reserva
    fields = [
        'cliente', 'chacara', 'data_inicio', 'data_fim', 'valor_total', 'status'
    ]
    template_name = 'website/reserva_form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Nova Reserva',
        'botao': 'Confirmar Reserva'
    }

class ResevaUpdate(UpdateView):
    model = Reserva
    fields = [
        'cliente', 'chacara', 'data_inicio', 'data_fim', 'valor_total', 'status'
    ]
    template_name = 'website/reserva_form.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'titulo': 'Editar Reserva',
        'botao': 'Salvar Alterações'
    }
