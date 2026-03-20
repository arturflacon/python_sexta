
from django.urls import path
from .views import IndexView, ContatoView, SobreView, ClienteCreate, AdministradorCreate, ChacaraCreate, ReservaCreate

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("contato/", ContatoView.as_view(), name="contato"),
    path("sobre/", SobreView.as_view(), name="sobre"),
    path("cliente/create/", ClienteCreate.as_view(), name="cliente-create"),
    path("administrador/create/", AdministradorCreate.as_view(), name="administrador-create"),
    path("chacara/create/", ChacaraCreate.as_view(), name="chacara-create"),
    path("reserva/create/", ReservaCreate.as_view(), name="reserva-create"),
]
