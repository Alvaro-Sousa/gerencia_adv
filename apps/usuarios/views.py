from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

# Create your views here.

class CadastroUsuarioView(APIView):
    def post(self, request):
        # adiciona a lógica para criar um novo usuário
        # Por exemplo, você pode validar os dados recebidos no request.data
        # e salvar o usuário no banco de dados
        return Response(status=status.HTTP_201_CREATED)

class LoginUsuarioView(APIView):
    def post(self, request):
        #logica para autenticar o usuário
        return Response(status=status.HTTP_200_OK)

class LogoutView(APIView):
    def post(self, request):
        #deslogar usuário
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PerfilView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # mostra os dados do perfil do usuário
        return Response(status=status.HTTP_200_OK)
    
def login_web_view(request):
    return render(request, 'usuarios/login.html')


def perfil_web_view(request):
    return render(request, 'usuarios/perfil.html')
