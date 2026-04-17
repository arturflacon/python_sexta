from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (
    # Públicas
    IndexView, ContatoView, SobreView,
    CalendarioReservasView,
    ChacaraListView, ChacaraDetailView,
    # Auth / cadastro
    SignupView,
    # Cliente autenticado
    ReservaCreate, MinhasReservasListView,
    # Admin — reservas
    PedidosPendentesListView, AprovarReservaView, RecusarReservaView,
    ReservaUpdateView, ReservaDeleteView,
    # Admin — chácara
    ChacaraCreate, ChacaraUpdate, ChacaraDelete,
    # Admin — outros
    AdministradorCreate,
    # Cliente
    ClienteCreate, ClienteUpdate,
)

urlpatterns = [
    # --- Páginas públicas ---
    path('', IndexView.as_view(), name='index'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('disponibilidade/', CalendarioReservasView.as_view(), name='calendario_reservas'),

    # --- Auth ---
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/', SignupView.as_view(), name='signup'),

    # --- Chácaras (públicas) ---
    path('chacaras/', ChacaraListView.as_view(), name='chacara_list'),
    path('chacaras/<int:pk>/', ChacaraDetailView.as_view(), name='chacara_detail'),

    # --- Chácaras (admin) ---
    path('chacaras/nova/', ChacaraCreate.as_view(), name='chacara_create'),
    path('chacaras/<int:pk>/editar/', ChacaraUpdate.as_view(), name='chacara_update'),
    path('chacaras/<int:pk>/excluir/', ChacaraDelete.as_view(), name='chacara_delete'),

    # --- Reservas (cliente) ---
    path('reservas/nova/', ReservaCreate.as_view(), name='reserva_create'),
    path('reservas/minhas/', MinhasReservasListView.as_view(), name='minhas_reservas'),

    # --- Reservas (admin) ---
    path('reservas/pendentes/', PedidosPendentesListView.as_view(), name='pedidos_pendentes'),
    path('reservas/<int:pk>/aprovar/', AprovarReservaView.as_view(), name='reserva_aprovar'),
    path('reservas/<int:pk>/recusar/', RecusarReservaView.as_view(), name='reserva_recusar'),
    path('reservas/<int:pk>/editar/', ReservaUpdateView.as_view(), name='reserva_update'),
    path('reservas/<int:pk>/excluir/', ReservaDeleteView.as_view(), name='reserva_delete'),

    # --- Clientes ---
    path('cliente/cadastro/', ClienteCreate.as_view(), name='cliente_create'),
    path('cliente/<int:pk>/editar/', ClienteUpdate.as_view(), name='cliente_update'),

    # --- Admin ---
    path('administrador/cadastro/', AdministradorCreate.as_view(), name='administrador_create'),
]
