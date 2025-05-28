from django.shortcuts import render
from autenticacao.forms import RegisterForms

# Create your views here.
def login(request):
    return render(request, 'autenticacao/login.html')

def cadastro(request):
    form = RegisterForms()

    if request.method == 'POST':
        form = RegisterForms(request.POST)

        if form.is_valid():
            form.save()

    return render(request, 'autenticacao/cadastro.html', {'form': form})