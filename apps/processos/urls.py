from django.urls import path
from . import views

app_name = 'processos'

urlpatterns = [
    path('', views.ListaTiposProcessoView.as_view(), name='lista_tipos_processos'),
    path('solicitacoes/', views.ListaSolicitacoesView.as_view(), name='lista_solicitacoes'),
    path('solicitacoes/nova/', views.CriarSolicitacaoView.as_view(), name='criar_solicitacao'),
    path('solicitacoes/<int:solicitacao_id>/', views.DetalhesSolicitacaoView.as_view(), name='detalhes_solicitacao'),
    path('solicitacoes/<int:solicitacao_id>/documentos/', views.EnviarDocumentoView.as_view(), name='enviar_documento'),
    path('solicitacoes/<int:solicitacao_id>/status/', views.AtualizarStatusView.as_view(), name='atualizar_status'),
]