# Plano de Sprint Curto - UI Bootstrap e Inicio da API

Objetivo: ter uma interface navegavel no runserver para validar fluxo do escritorio, depois iniciar a API sem retrabalho.

## Sprint 1 - Interface Web (2 a 4 dias)

### Meta
Entregar telas funcionais com Bootstrap para advogado e cliente, mesmo com dados ainda simples.

### Escopo
- Layout base com navegacao
- Login visual
- Dashboard inicial
- Lista de processos
- Detalhe de processo
- Formulario simples para cadastro/atualizacao manual

### Arquivos e estrutura sugerida
- templates/base.html
- templates/usuarios/login.html
- templates/usuarios/perfil.html
- templates/processos/lista_tipos.html
- templates/processos/lista_solicitacoes.html
- templates/processos/detalhes_solicitacao.html
- templates/processos/nova_solicitacao.html
- templates/processos/enviar_documento.html

### Passos tecnicos
1. Configurar templates no settings (DIRS apontando para pasta templates).
2. Criar base.html com navbar, container e bloco de mensagens.
3. Criar views web com render() separadas das APIViews.
4. Criar urls web em namespace web (ex.: /web/processos/...).
5. Ligar botoes entre telas para validar navegacao fim-a-fim.
6. Testar no navegador com runserver e ajustar UX minima.

### Criterios de pronto
- Runserver abre sem erro.
- Todas as telas principais carregam.
- Fluxo manual do advogado funciona (criar/atualizar).
- Cliente consegue abrir tela de acompanhamento.

## Sprint 2 - Fundacao da API (3 a 5 dias)

### Meta
Criar primeira versao da API com autenticacao e endpoints essenciais.

### Escopo da API v1
- /api/v1/auth/login/
- /api/v1/auth/logout/
- /api/v1/usuarios/perfil/
- /api/v1/processos/
- /api/v1/processos/{id}/
- /api/v1/processos/{id}/status/

### Ordem de implementacao
1. Definir contratos JSON (request/response) por endpoint.
2. Criar serializers de usuarios.
3. Criar serializers de processos.
4. Implementar views com validacao via serializer.
5. Aplicar permissoes por perfil (advogado x cliente).
6. Criar testes de API (status code, validacao, permissao).
7. Publicar documentacao com OpenAPI/Swagger.

### Regras importantes
- Cliente so acessa dados proprios.
- Advogado pode listar e atualizar processos do escritorio.
- Respostas de erro padronizadas.
- Versionamento desde o inicio (/api/v1).

### Criterios de pronto
- Endpoints essenciais respondem conforme contrato.
- Permissoes funcionando.
- Testes minimos passando.
- Documentacao acessivel para testes.

## Riscos e mitigacoes
- Risco: misturar tela web e API na mesma view.
- Mitigacao: manter views HTML e APIViews separadas.

- Risco: retrabalho ao mudar formato da resposta.
- Mitigacao: fechar contrato JSON antes de codar endpoint.

- Risco: cliente ver dados de outro cliente.
- Mitigacao: testes de permissao obrigatorios em toda rota sensivel.

## Proximo passo pratico
1. Implementar primeiro templates/base.html e login.html.
2. Validar navegacao com runserver.
3. Em seguida iniciar serializers de usuarios para abrir a API v1.
