from django.urls import path
from .views import (
    IndexView, ContatoView, SobreView, 
    ClienteCreate, AdministradorCreate, ChacaraCreate, ReservaCreate,
    ClienteUpdate, ChacaraUpdate, ReservaUpdate, ChacaraDelete, 
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    
    # Rotas de criação
    path('cliente/create/', ClienteCreate.as_view(), name='cliente_create'),
    path('cliente/<int:pk>/update/', ClienteUpdate.as_view(), name='cliente_update'),
    path('chacara/<int:pk>/delete/', ChacaraDelete.as_view(), name='chacara_delete'),
    path('administrador/create/', AdministradorCreate.as_view(), name='administrador_create'),
    path('chacara/create/', ChacaraCreate.as_view(), name='chacara_create'),
    path ('chacara/<int:pk>/update/', ChacaraUpdate.as_view(), name='chacara_update'),
    path('reserva/create/', ReservaCreate.as_view(), name='reserva_create'),
    path('reserva/<int:pk>/update/', ReservaUpdate.as_view(), name='reserva_update'),
]
