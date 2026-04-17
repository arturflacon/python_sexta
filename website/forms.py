from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Cliente, Reserva


class SignupForm(UserCreationForm):
    nome = forms.CharField(
        max_length=255,
        label='Nome Completo',
        help_text='Seu nome completo.',
    )
    telefone = forms.CharField(
        max_length=11,
        label='Telefone',
        help_text='Somente dígitos, ex: 11999998888.',
    )
    email = forms.EmailField(
        required=True,
        label='E-mail',
        help_text='Informe um e-mail válido.',
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Cliente.objects.create(
                usuario=user,
                nome=self.cleaned_data['nome'],
                telefone=self.cleaned_data['telefone'],
            )
        return user


class ReservaClienteForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['chacara', 'data_inicio', 'data_fim', 'observacoes']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'data_fim': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
