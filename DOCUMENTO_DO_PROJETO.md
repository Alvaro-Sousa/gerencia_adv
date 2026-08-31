# Sistema de Gestão Jurídica para Advogado Individual

## 1. Visão Geral do Projeto

Este projeto consiste em um sistema de gestão de processos jurídicos voltado para advogado individual. A ideia principal é criar uma plataforma onde clientes possam solicitar a abertura de processos, enviar documentos necessários e acompanhar o andamento de seus casos, enquanto o advogado pode gerenciar tudo de forma centralizada.

O sistema busca resolver um problema comum: a dificuldade de organizar documentos, informações e atualizações de status de cada processo, evitando retrabalho e comunicação fragmentada entre cliente e advogado.

### Objetivo principal
Centralizar o atendimento jurídico, facilitando:
- o cadastro de clientes;
- a solicitação de processos;
- o envio de documentos obrigatórios;
- o acompanhamento de status;
- a gestão dos casos pelo advogado.

---

## 2. Funcionalidades do MVP

O MVP será a primeira versão funcional do sistema, com foco nas funções essenciais.

### Para o cliente
- Criar conta;
- Fazer login;
- Visualizar os tipos de processos disponíveis;
- Solicitar abertura de um processo;
- Enviar documentos exigidos;
- Acompanhar o status do processo;
- Ver histórico de solicitações.

### Para o advogado
- Criar conta profissional;
- Fazer login;
- Visualizar solicitações recebidas;
- Analisar documentos enviados;
- Atualizar status do processo;
- Consultar histórico dos processos;
- Visualizar informações completas de cada cliente.

### Funcionalidades básicas de suporte
- Autenticação de usuários;
- Controle de perfis de acesso;
- Armazenamento de documentos;
- Registro de status por processo.

---

## 3. Estrutura do Banco de Dados

Abaixo está uma proposta inicial de estrutura para o banco de dados.

### Tabelas principais

#### users
Armazena os usuários da plataforma.

Campos sugeridos:
- id
- name
- email
- password
- role (`client` ou `lawyer`)
- created_at
- updated_at

#### process_types
Armazena os tipos de processos que o advogado atende.

Campos sugeridos:
- id
- title
- description
- active
- created_at
- updated_at

#### required_documents
Armazena os documentos obrigatórios para cada tipo de processo.

Campos sugeridos:
- id
- process_type_id
- document_name
- description
- required
- created_at
- updated_at

#### process_requests
Armazena as solicitações feitas pelos clientes.

Campos sugeridos:
- id
- client_id
- process_type_id
- status
- notes
- created_at
- updated_at

#### process_documents
Armazena os documentos enviados para cada solicitação.

Campos sugeridos:
- id
- process_request_id
- document_name
- file_url
- uploaded_at

#### process_status_history
Armazena o histórico de mudanças de status.

Campos sugeridos:
- id
- process_request_id
- old_status
- new_status
- changed_by
- created_at

---

## 4. Fluxo de Telas

A experiência do usuário pode ser organizada da seguinte forma.

### Telas do cliente
1. Tela inicial
2. Cadastro
3. Login
4. Dashboard do cliente
5. Lista de tipos de processos
6. Detalhes do processo
7. Formulário de solicitação
8. Upload de documentos
9. Acompanhamento do status
10. Histórico de solicitações

### Telas do advogado
1. Login
2. Dashboard do advogado
3. Lista de solicitações recebidas
4. Detalhes da solicitação
5. Visualização de documentos
6. Alteração de status
7. Histórico do processo
8. Gestão de tipos de processo e documentos

### Fluxo principal
Cliente → escolhe o tipo de processo → envia dados e documentos → advogado recebe → advogado analisa → advogado atualiza status → cliente acompanha.

---

## 5. Arquitetura do Sistema

A arquitetura inicial pode seguir uma estrutura simples e escalável.

### Frontend
Responsável pela interface do sistema.

Pode conter:
- páginas públicas;
- autenticação;
- dashboard do cliente;
- dashboard do advogado;
- formulários;
- upload de documentos;
- acompanhamento de status.

### Backend
Responsável pelas regras de negócio.

Pode conter:
- autenticação e autorização;
- gestão de usuários;
- gestão de processos;
- upload e armazenamento de documentos;
- atualização de status;
- histórico de alterações.

### Banco de dados
Responsável por armazenar:
- usuários;
- tipos de processos;
- documentos obrigatórios;
- solicitações;
- arquivos enviados;
- histórico de status.

### Possível divisão de camadas
- **Presentation Layer**: interface do usuário
- **Application Layer**: regras e fluxos
- **Domain Layer**: entidades e lógica principal
- **Infrastructure Layer**: banco, storage e integração externa

---

## Próximos passos sugeridos

1. Definir o nome do projeto;
2. Escolher as tecnologias;
3. Criar o MVP;
4. Desenhar as telas principais;
5. Estruturar o banco de dados;
6. Iniciar o desenvolvimento por autenticação e cadastro de processos.

---

## Resumo final

Este sistema tem como proposta ser uma plataforma simples e organizada para conectar cliente e advogado, centralizando solicitações, documentos e status dos processos em um só lugar.
