from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('cadastro/', views.CadastroUsuarioView.as_view(), name='cadastro'),
    path('login/', views.LoginUsuarioView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('perfil/', views.PerfilView.as_view(), name='perfil'),
    path('web/login/', views.login_web_view, name='web_login'),
    path('web/perfil/', views.perfil_web_view, name='web_perfil'),
]