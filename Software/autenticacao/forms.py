from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.html import format_html

class RegisterForms(UserCreationForm):
    email = forms.EmailField(
        label='E-mail',
        help_text='Digite um e-mail válido.',
        required=True
    )
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Nome de usuário',
            'password1': 'Senha',
            'password2': 'Confirme a senha',
        }
        help_texts = {
            'username': 'Escolha um nome único.',
            'password1': 'Sua senha deve ter pelo menos 8 caracteres.',
        }
        error_messages = {
            'username': {
                'unique': "Esse nome de usuário já está em uso!",
            }
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        help_text_list = [
            "Pelo menos 8 caracteres.",
            "Pelo menos 1 maiúscula.",
            "Pelo menos 1 minúscula.",
            "Pelo menos 1 número.",
            "Pelo menos 1 caractere especial."
        ]

        self.fields['password1'].help_text = format_html(
        "<p>Regras:</p><ul>{}</ul>",
        format_html("".join(f"<li>{item}</li>" for item in help_text_list))
        )

        self.fields['password2'].help_text = ""
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


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