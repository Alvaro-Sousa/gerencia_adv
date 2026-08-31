from django.db import models

# Create your models here.
class TipoProcesso(models.Model):
    titulo = models.CharField(max_length=150)
    descricao = models.TextField()
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

class DocumentoObrigatorio(models.Model):
    tipo_processo = models.ForeignKey(TipoProcesso,on_delete=models.CASCADE,related_name='documentos_obrigatorios')

    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True, null=True)
    obrigatorio = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class SolicitacaoProcesso(models.Model):
    class Status(models.TextChoices):
        PENDENTE = 'PENDENTE', 'Pendente'
        EM_ANALISE = 'EM_ANALISE', 'EM análise'
        DOCUMENTACAO_PENDENTE = 'DOCUMENTACAO_PENDENTE', 'Documentação pendente'
        EM_ANDAMENTO = 'EM_ANDAMENTO', 'Em andamento'
        CONCLUIDO = 'CONCLUIDO', 'Concluído'
        CANCELADO = 'CANCELADO', 'Cancelado'

    cliente = models.ForeignKey('usuarios.Usuarios',
                                on_delete=models.PROTECT, related_name='solicitacoes',)
    tipo_processo = models.ForeignKey(TipoProcesso, on_delete=models.PROTECT, related_name='solicitacoes')
    status = models.CharField(max_length=25, choices=Status.choices, default=Status.PENDENTE,)

    observacoes = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.tipo_processo} - {self.cliente}'

class DocumentoProcesso(models.Model):
    solicitacao = models.ForeignKey(SolicitacaoProcesso,
                                    on_delete=models.CASCADE, related_name='documentos',)
    nome = models.CharField(max_length=150)
    arquivo = models.FileField(upload_to='documentos_processo/')
    enviado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class HistoricoProcesso(models.Model):
    solicitacao = models.ForeignKey(SolicitacaoProcesso, on_delete=models.CASCADE,
                                    related_name='historico_status')
    status_anterior = models.CharField(max_length=25, blank=True)
    status_novo = models.CharField(max_length=25)
    alterado_por = models.ForeignKey('usuarios.Usuarios',on_delete=models.PROTECT,
                                    related_name='alteracoes_status')
    criado_em = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.solicitacao} - {self.status_novo}'