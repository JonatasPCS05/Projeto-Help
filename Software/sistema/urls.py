from django.urls import path
from . import views

app_name = 'sistema'

urlpatterns = [
    path('home/', views.home_user, name='homeUser'),
    path('solicitar/', views.solicitar_servico, name='solicitar_servico'),
    path('atualizar/<int:servico_id>/', views.atualizar_servico, name='atualizar_servico'),
    path('deletar/<int:servico_id>/', views.deletar_servico, name='deletar_servico'),
    path('home-autonomo/', views.home_autonomo, name='home_autonomo'),
    path('solicitacoes-gerais/', views.solicitacoes_gerais, name='solicitacoes_gerais'),
]