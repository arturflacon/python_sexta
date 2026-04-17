from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import (
    CreateView, DeleteView, DetailView, FormView,
    ListView, TemplateView, UpdateView,
)

from .forms import ReservaClienteForm, SignupForm
from .models import Administrador, Chacara, Cliente, Reserva


# ---------------------------------------------------------------------------
# Mixins
# ---------------------------------------------------------------------------

class AdminRequiredMixin(UserPassesTestMixin):
    """Permite acesso apenas a usuários com perfil Administrador."""

    def test_func(self):
        return self.request.user.is_authenticated and hasattr(self.request.user, 'administrador')


# ---------------------------------------------------------------------------
# Páginas públicas
# ---------------------------------------------------------------------------

class IndexView(TemplateView):
    template_name = 'website/index.html'


class ContatoView(TemplateView):
    template_name = 'website/contato.html'


class SobreView(TemplateView):
    template_name = 'website/sobre.html'


class CalendarioReservasView(ListView):
    model = Reserva
    template_name = 'website/calendario_reservas.html'
    context_object_name = 'reservas'

    def get_queryset(self):
        return Reserva.objects.filter(status=Reserva.STATUS_CONFIRMADA).order_by('data_inicio')


class ChacaraListView(ListView):
    model = Chacara
    template_name = 'website/chacara_list.html'
    context_object_name = 'chacaras'


class ChacaraDetailView(DetailView):
    model = Chacara
    template_name = 'website/chacara_detail.html'
    context_object_name = 'chacara'


# ---------------------------------------------------------------------------
# Cadastro / auth
# ---------------------------------------------------------------------------

class SignupView(FormView):
    template_name = 'website/registro.html'
    form_class = SignupForm
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Cadastro de Cliente', 'botao': 'Criar conta'}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


# ---------------------------------------------------------------------------
# Área do cliente (autenticado)
# ---------------------------------------------------------------------------

class ReservaCreate(LoginRequiredMixin, CreateView):
    model = Reserva
    form_class = ReservaClienteForm
    template_name = 'website/reserva_form.html'
    success_url = reverse_lazy('minhas_reservas')
    extra_context = {'titulo': 'Fazer Pedido de Reserva', 'botao': 'Enviar Pedido'}

    def form_valid(self, form):
        reserva = form.save(commit=False)
        reserva.cliente = get_object_or_404(Cliente, usuario=self.request.user)
        reserva.status = Reserva.STATUS_PENDENTE
        reserva.full_clean()
        return super().form_valid(form)


class MinhasReservasListView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = 'website/reserva_list.html'
    context_object_name = 'reservas'

    def get_queryset(self):
        try:
            cliente = self.request.user.cliente
        except Cliente.DoesNotExist:
            return Reserva.objects.none()
        return Reserva.objects.filter(cliente=cliente)


# ---------------------------------------------------------------------------
# Área administrativa (Administrador)
# ---------------------------------------------------------------------------

class PedidosPendentesListView(AdminRequiredMixin, ListView):
    model = Reserva
    template_name = 'website/pedidos_pendentes.html'
    context_object_name = 'reservas'

    def get_queryset(self):
        return Reserva.objects.filter(status=Reserva.STATUS_PENDENTE).order_by('data_pedido')


class AprovarReservaView(AdminRequiredMixin, View):
    def post(self, _request, pk):
        reserva = get_object_or_404(Reserva, pk=pk)
        reserva.status = Reserva.STATUS_CONFIRMADA
        reserva.data_decisao = timezone.now()
        reserva.save()
        return redirect('pedidos_pendentes')


class RecusarReservaView(AdminRequiredMixin, View):
    def post(self, _request, pk):
        reserva = get_object_or_404(Reserva, pk=pk)
        reserva.status = Reserva.STATUS_RECUSADA
        reserva.data_decisao = timezone.now()
        reserva.save()
        return redirect('pedidos_pendentes')


class ReservaUpdateView(AdminRequiredMixin, UpdateView):
    model = Reserva
    fields = ['chacara', 'data_inicio', 'data_fim', 'observacoes', 'status']
    template_name = 'website/reserva_form.html'
    success_url = reverse_lazy('pedidos_pendentes')
    extra_context = {'titulo': 'Editar Reserva', 'botao': 'Salvar Alterações'}


class ReservaDeleteView(AdminRequiredMixin, DeleteView):
    model = Reserva
    template_name = 'website/reserva_confirm_delete.html'
    success_url = reverse_lazy('pedidos_pendentes')
    extra_context = {'titulo': 'Excluir Reserva'}


# ---------------------------------------------------------------------------
# CRUD de Chácara (admin)
# ---------------------------------------------------------------------------

CHACARA_FIELDS = [
    'nome', 'descricao', 'preco_diaria',
    'tem_estacionamento', 'tem_piscina', 'tem_churrasqueira',
    'num_quartos', 'num_banheiros',
]


class ChacaraCreate(AdminRequiredMixin, CreateView):
    model = Chacara
    fields = CHACARA_FIELDS
    template_name = 'website/chacara_form.html'
    success_url = reverse_lazy('chacara_list')
    extra_context = {'titulo': 'Cadastrar Chácara', 'botao': 'Cadastrar'}


class ChacaraUpdate(AdminRequiredMixin, UpdateView):
    model = Chacara
    fields = CHACARA_FIELDS
    template_name = 'website/chacara_form.html'
    success_url = reverse_lazy('chacara_list')
    extra_context = {'titulo': 'Editar Chácara', 'botao': 'Salvar Alterações'}


class ChacaraDelete(AdminRequiredMixin, DeleteView):
    model = Chacara
    template_name = 'website/chacara_confirm_delete.html'
    success_url = reverse_lazy('chacara_list')
    extra_context = {'titulo': 'Excluir Chácara', 'botao': 'Confirmar Exclusão'}


# ---------------------------------------------------------------------------
# CRUD de Cliente (admin ou próprio usuário)
# ---------------------------------------------------------------------------

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['nome', 'telefone', 'usuario']
    template_name = 'website/cliente_form.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Cadastro de Cliente', 'botao': 'Cadastrar Cliente'}


class ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['nome', 'telefone']
    template_name = 'website/cliente_form.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Editar Cliente', 'botao': 'Salvar Alterações'}


class AdministradorCreate(AdminRequiredMixin, CreateView):
    model = Administrador
    fields = ['nome', 'usuario']
    template_name = 'website/administrador_form.html'
    success_url = reverse_lazy('index')
    extra_context = {'titulo': 'Cadastro de Administrador', 'botao': 'Cadastrar Administrador'}
