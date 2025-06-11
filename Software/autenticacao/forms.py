from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegisterForms(UserCreationForm):
    email = forms.EmailField(
        label='E-mail',
        help_text='Digite um e-mail válido.',
        required=True
    )
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)


# Formulário de Login que vamos adicionar
class LoginForm(forms.Form):
    username = forms.CharField(
        label='Nome de Usuário',
        widget=forms.TextInput()
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput()
    )