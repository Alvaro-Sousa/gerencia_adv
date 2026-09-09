from django.urls import path
from . import views

app_name = 'processos'

urlpatterns = [
    path('', views.ListaTipoProcessoView.as_view(), name='lista_tipos_processos'),
    path('web/dashboard/', views.dashboard_web_view, name='dashboard_web'),
    path('solicitacoes/', views.ListaSolicitacoesView.as_view(), name='lista_solicitacoes'),
    path('solicitacoes/nova/', views.CriarSolicitacaoView.as_view(), name='criar_solicitacao'),
    path('solicitacoes/<int:solicitacao_id>/', views.DetalhesSolicitacaoView.as_view(), name='detalhes_solicitacao'),
    path('solicitacoes/<int:solicitacao_id>/documentos/', views.EnviarDocumentoView.as_view(), name='enviar_documento'),
    path('solicitacoes/<int:solicitacao_id>/status/', views.AtualizarStatusView.as_view(), name='atualizar_status'),
    path('web/solicitacoes/', views.lista_solicitacoes_web, name='web_lista_solicitacoes'),
    path('web/solicitacoes/nova/', views.nova_solicitacao_web, name='web_nova_solicitacao'),
    path('web/solicitacoes/<int:solicitacao_id>/', views.detalhe_solicitacao_web, name='web_detalhe_solicitacao'),
]