from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

def dashboard_web_view(request):
    return render(request, 'processos/dashboard.html')

def lista_solicitacoes_web(request):
    return render(request, 'processos/lista_solicitacoes.html')

def nova_solicitacao_web(request):
    return render(request, 'processos/nova_solicitacao.html')

def detalhe_solicitacao_web(request, solicitacao_id):
    return render(request, 'processos/detalhes_solicitacao.html')

def perfil_web_view(request):
    return render(request, 'usuarios/perfil.html')



class ListaTipoProcessoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response(status=status.HTTP_200_OK)

class ListaSolicitacoesView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response(status=status.HTTP_200_OK)

class CriarSolicitacaoView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        return Response(status=status.HTTP_201_CREATED)
    
class DetalhesSolicitacaoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, solicitacao_id):
        return Response(status=status.HTTP_200_OK)

class EnviarDocumentoView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, solicitacao_id):
        return Response(status=status.HTTP_201_CREATED)
    
class AtualizarStatusView(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, solicitacao_id):
        return Response(status=status.HTTP_200_OK)
# Create your views here.
