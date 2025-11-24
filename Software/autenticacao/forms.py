from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmailForm(forms.Form):
    email = forms.EmailField(label="E-mail")

class PasswordForm(forms.Form):
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirme a senha", widget=forms.PasswordInput)

class NameForm(forms.Form):
    first_name = forms.CharField(label="Nome")
    last_name = forms.CharField(label="Sobrenome")


# Formulário de Login que vamos adicionar
class LoginForm(forms.Form):
    username = forms.CharField(
        label='E-mail',
        widget=forms.TextInput()
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput()
    )

class SolicitarAutonomoForm(forms.Form):
    mensagem = forms.CharField(
        label="Por que você quer se tornar autônomo?",
        widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Descreva aqui..."})
    )
