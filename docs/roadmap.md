# Roadmap do Projeto Gerencia Adv

Este documento organiza as etapas de desenvolvimento do projeto em fases, para servir como base de implementação no VS Code.

---

## Fase 1 — Base do projeto

Objetivo: criar a estrutura inicial do sistema e preparar o ambiente de desenvolvimento.

### Tarefas
- Criar o projeto Django
- Configurar o ambiente virtual
- Instalar dependências iniciais
- Conectar o projeto ao PostgreSQL
- Configurar arquivos estáticos
- Configurar arquivos de mídia
- Organizar a estrutura inicial de pastas

### Resultado esperado
- Projeto Django criado e funcionando
- Banco de dados configurado
- Estrutura pronta para receber os apps

---

## Fase 2 — Usuários e autenticação

Objetivo: permitir que clientes e advogado possam criar conta, entrar no sistema e acessar áreas diferentes.

### Tarefas
- Criar o app `accounts`
- Criar modelo de usuário com perfis
- Implementar cadastro
- Implementar login
- Implementar logout
- Separar permissões entre cliente e advogado
- Criar regras de acesso às páginas

### Resultado esperado
- Usuários conseguem acessar o sistema
- Cada perfil tem acesso ao que lhe pertence

---

## Fase 3 — Processos

Objetivo: estruturar os tipos de processos e as solicitações feitas pelos clientes.

### Tarefas
- Criar o app `processes`
- Cadastrar tipos de processo
- Definir descrição de cada processo
- Criar formulário de solicitação
- Salvar solicitações no banco
- Vincular solicitação ao cliente
- Vincular solicitação ao tipo de processo

### Resultado esperado
- Cliente consegue solicitar um processo dentro da plataforma
- Advogado consegue visualizar as solicitações recebidas

---

## Fase 4 — Documentos

Objetivo: centralizar o envio e armazenamento dos documentos necessários para cada processo.

### Tarefas
- Criar o app `documents`
- Cadastrar documentos obrigatórios por tipo de processo
- Permitir upload de arquivos
- Vincular documentos à solicitação correspondente
- Listar documentos enviados
- Controlar documentos pendentes

### Resultado esperado
- Cliente consegue enviar documentos no sistema
- Advogado consegue acessar tudo em um só lugar

---

## Fase 5 — Painéis e acompanhamento

Objetivo: criar as telas principais para cliente e advogado acompanharem o sistema.

### Tarefas
- Criar o app `dashboard`
- Criar dashboard do cliente
- Criar dashboard do advogado
- Exibir status dos processos
- Permitir atualização de status pelo advogado
- Mostrar histórico de alterações

### Resultado esperado
- Cliente acompanha o andamento do caso
- Advogado controla os processos de forma centralizada

---

## Fase 6 — Melhorias futuras

Objetivo: evoluir o sistema depois do MVP.

### Possíveis melhorias
- Notificações por e-mail
- Filtros de busca avançados
- Comentários internos no processo
- Assinatura digital
- Exportação de relatórios
- API REST com Django REST Framework
- Frontend separado com React ou outra tecnologia

---

## Ordem sugerida de implementação

1. Base do projeto
2. Autenticação
3. Processos
4. Documentos
5. Dashboards
6. Melhorias

---

## Observação

Este documento deve ser usado como guia prático para o desenvolvimento no VS Code, ajudando a manter o projeto organizado por etapas.
