from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from .forms import RegisterForms, LoginForm
from django.contrib.auth import logout

def cadastro(request):
    form_action = request.path

    if request.method == 'POST':
        form = RegisterForms(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, f'Bem-vindo, {user.username}! Cadastro realizado com sucesso.')
            return redirect('sistema:homeUser')
    else:
        form = RegisterForms()

    return render(request, 'autenticacao/cadastro.html', {
        'form': form,
        'form_action': form_action,
    })


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