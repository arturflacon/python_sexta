from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .models import Cliente, Administrador, Chacara, Reserva


class IndexView(TemplateView):
    template_name = "website/modelo.html"

class ContatoView(TemplateView):
    template_name = "website/contato.html"

class SobreView(TemplateView):
    template_name = "website/sobre.html"

