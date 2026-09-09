# Roadmap do Projeto Gerencia Adv

Este roadmap prioriza validacao rapida do fluxo do escritorio com interface web e, na sequencia, evolucao segura para API.

## Fase 1 - Fundacao tecnica

Objetivo: garantir base estavel para desenvolver sem bloqueios.

### Tarefas
- Confirmar ambiente virtual e dependencias
- Revisar configuracao do projeto (apps, banco, static, media)
- Rodar migracoes e check do Django
- Padronizar estrutura de pastas dos apps atuais

### Resultado esperado
- Projeto sobe com runserver sem erro
- Configuracao pronta para evoluir telas e API

## Fase 2 - Interface web MVP com Bootstrap

Objetivo: permitir uso real no navegador antes da API completa.

### Tarefas
- Criar layout base com Bootstrap
- Criar paginas de login e perfil
- Criar paginas de processos (lista, detalhe, nova solicitacao, envio de documento)
- Criar navegacao entre telas
- Exibir mensagens de sucesso e erro

### Resultado esperado
- Advogado consegue operar fluxo manual no sistema
- Cliente consegue visualizar acompanhamento basico
- Time valida usabilidade cedo, sem depender da API pronta

## Fase 3 - Fluxo manual operacional

Objetivo: transformar o sistema em ferramenta util para rotina do escritorio.

### Tarefas
- Ajustar formularios para cadastro manual de processos
- Criar atualizacao manual de status
- Exibir historico basico de alteracoes
- Garantir vinculo cliente-processo

### Resultado esperado
- Escritorio consegue cadastrar e atualizar casos manualmente
- Cliente acompanha o andamento dentro da plataforma

## Fase 4 - API v1 (primeira API)

Objetivo: publicar endpoints essenciais sem retrabalho.

### Tarefas
- Definir contratos JSON de request/response
- Criar serializers de usuarios
- Criar serializers de processos
- Implementar endpoints de autenticacao e perfil
- Implementar endpoints de listagem, detalhe e atualizacao de status
- Aplicar permissoes por perfil (advogado e cliente)

### Resultado esperado
- API v1 funcional com autenticacao
- Cliente acessa apenas os proprios dados
- Advogado gerencia o conjunto de processos do escritorio

## Fase 5 - Qualidade e seguranca

Objetivo: reduzir risco antes de escalar uso.

### Tarefas
- Criar testes minimos de views web e API
- Criar testes de permissao e validacao
- Padronizar tratamento de erros
- Documentar API com OpenAPI/Swagger

### Resultado esperado
- Confianca para evoluir sem quebrar fluxo principal
- API documentada para consumo por front ou app mobile

## Fase 6 - Integracoes e automacao juridica

Objetivo: reduzir trabalho manual do advogado.

### Tarefas
- Integrar provedor de acompanhamento processual
- Integrar notificacoes (email/WhatsApp)
- Avaliar assinatura eletronica
- Criar trilha de auditoria das atualizacoes

### Resultado esperado
- Menos atualizacao manual repetitiva
- Melhor comunicacao com cliente
- Operacao mais escalavel

## Ordem sugerida de implementacao

1. Fundacao tecnica
2. Interface web MVP com Bootstrap
3. Fluxo manual operacional
4. API v1
5. Qualidade e seguranca
6. Integracoes e automacao juridica

## Criterio de sucesso do MVP

O MVP esta pronto quando:

1. O advogado cadastra e atualiza processos manualmente no sistema
2. O cliente autentica e acompanha os proprios processos
3. O projeto roda sem erros de configuracao
4. A API v1 possui os endpoints essenciais com permissao correta
