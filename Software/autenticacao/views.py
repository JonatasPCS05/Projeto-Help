from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from .forms import LoginForm, EmailForm, PasswordForm, NameForm
from django.contrib.auth import logout
from formtools.wizard.views import SessionWizardView
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import SolicitarAutonomoForm

class UserRegisterWizard(SessionWizardView):
    form_list = [EmailForm, PasswordForm, NameForm]
    template_name = "autenticacao/cadastro.html"

    def done(self, form_list, **kwargs):
        form_data = self.get_all_cleaned_data()
        user = User.objects.create_user(
            username=form_data["email"],
            email=form_data["email"],
            password=form_data["password1"],
            first_name=form_data["first_name"],
            last_name=form_data["last_name"],
        )
        return render(self.request, 'autenticacao/login.html', {"user": user})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Login realizado com sucesso!')
                return redirect('sistema:homeUser')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
    else:
        form = LoginForm()

    return render(request, 'autenticacao/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu do sistema.')
    return redirect('home:home')

@login_required
def solicitar_autonomo(request):
    if request.method == 'POST':
        form = SolicitarAutonomoForm(request.POST)
        if form.is_valid():
            mensagem = form.cleaned_data['mensagem']
            send_mail(
                subject='Solicitação de conta Autônomo',
                message=f"O usuário {request.user.username} ({request.user.email}) solicitou se tornar autônomo.\n\nMensagem:\n{mensagem}",
                from_email='seuemail@gmail.com',
                recipient_list=['jonatascontateste01@gmail.com'],
            )
            messages.success(request, 'Sua solicitação foi enviada com sucesso!')
            return redirect('sistema:homeUser')
    else:
        form = SolicitarAutonomoForm()
    return render(request, 'autenticacao/solicitar_autonomo.html', {'form': form})
