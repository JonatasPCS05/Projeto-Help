from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Servico
from .forms import ServicoForm, PropostaForm

# --- Views do Cliente ---

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
def ver_proposta(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id, usuario=request.user)
    
    if request.method == 'POST':
        acao = request.POST.get('acao')
        if acao == 'aceitar':
            servico.status = 'pendente'
            servico.save()
            messages.success(request, 'Proposta aceita! O serviço está pendente.')
        elif acao == 'recusar':
            servico.status = 'aberto'
            servico.autonomo = None
            servico.data_visita = None
            servico.valor_hora = None
            servico.save()
            messages.info(request, 'Proposta recusada. O serviço voltou a ficar disponível.')
        elif acao == 'concluir':
            servico.status = 'concluido'
            servico.save()
            messages.success(request, 'Serviço marcado como concluído!')
            
        return redirect('sistema:homeUser')

    return render(request, 'sistema/ver_proposta.html', {'servico': servico})

# --- Views do Autônomo ---

@login_required
def solicitacoes_gerais(request):
    servicos = Servico.objects.filter(status='aberto')\
                              .exclude(usuario=request.user)\
                              .exclude(recusado_por=request.user)
    return render(request, 'sistema/solicitacoes_gerais.html', {'servicos': servicos})

@login_required
def recusar_oportunidade(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    servico.recusado_por.add(request.user)
    messages.info(request, 'Proposta recusada e removida da sua lista.')
    return redirect('sistema:solicitacoes_gerais')

@login_required
def enviar_proposta(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id)
    
    if request.method == 'POST':
        form = PropostaForm(request.POST, instance=servico)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.autonomo = request.user
            obj.status = 'proposta_enviada'
            obj.save()
            messages.success(request, 'Proposta enviada para o cliente!')
            return redirect('sistema:home_autonomo')
    else:
        form = PropostaForm(instance=servico)
    
    return render(request, 'sistema/criarServico.html', {'form': form, 'titulo': 'Enviar Proposta'})

@login_required
def home_autonomo(request):
    servicos = Servico.objects.filter(autonomo=request.user).order_by('-data_solicitacao')
    return render(request, 'sistema/home_autonomo.html', {'servicos': servicos})

@login_required
def deletar_servico(request, servico_id):
    servico = get_object_or_404(Servico, id=servico_id, usuario=request.user)
    if request.method == 'POST':
        servico.delete()
        messages.success(request, 'Solicitação excluída.')
        return redirect('sistema:homeUser')
    return render(request, 'sistema/confirmarDelete.html', {'servico': servico})

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
