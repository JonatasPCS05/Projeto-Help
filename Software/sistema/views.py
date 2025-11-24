from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Servico
from .forms import ServicoForm

#Create your views here
@login_required
def home_user(request):
    servicos = Servico.objects.filter(usuario=request.user).order_by('-data_solicitacao')
    return render(request, 'sistema/homeUser.html', {'servicos': servicos})

@login_required
def solicitar_servico(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            servico = form.save(commit=False)
            servico.usuario = request.user
            servico.save()
            messages.success(request, 'Serviço solicitado com sucesso!')
            return redirect('sistema:homeUser')
    else:
        form = ServicoForm()
    
    return render(request, 'sistema/criarServico.html', {'form': form, 'titulo': 'Solicitar Serviço'})

@login_required
def atualizar_servico(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id, usuario=request.user)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sua solicitação foi atualizada.')
            return redirect('sistema:homeUser')
    else:
        form = ServicoForm(instance=servico)

    return render(request, 'sistema/criarServico.html', {'form': form, 'titulo': 'Atualizar Solicitação'})

@login_required
def deletar_servico(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id, usuario=request.user)
    if request.method == 'POST':
        servico.delete()
        messages.success(request, 'Sua solicitação foi excluída com sucesso.')
        return redirect('sistema:homeUser')
    
    return render(request, 'sistema/confirmarDelete.html', {'servico': servico})

@login_required
def home_autonomo(request):
    # mostra os serviços que esse autônomo já aceitou
    servicos = Servico.objects.filter(usuario=request.user)
    return render(request, 'sistema/home_autonomo.html', {'servicos': servicos})

@login_required
def solicitacoes_gerais(request):
    # mostra todos os serviços pendentes
    servicos = Servico.objects.all().order_by('-data_solicitacao')
    return render(request, 'sistema/solicitacoes_gerais.html', {'servicos': servicos})
