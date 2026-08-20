---
name: supabase-sync
description: Esta skill deve ser usada para LER e GRAVAR dados de leads e do perfil do aluno no Supabase — substitui o antigo dashboard local em SQLite. Acione sempre que qualquer comando do plugin mudar dados de leads (/prospectar, /redesenhar, /publicar, /proposta, /contrato, /respostas, /followup), ou quando precisar ler o perfil/config do aluno (nichos, assinatura, dados do GitHub).
---

# Sincronização com Supabase (banco compartilhado da turma)

Todos os alunos usam o MESMO projeto Supabase — os dados de cada um ficam isolados por login (RLS: cada aluno só enxerga as próprias linhas). O painel web (hospedado separadamente) lê o mesmo banco, então tudo que os comandos gravam aqui aparece automaticamente lá pro aluno ver.

## Login (uma vez, no /setup)

O aluno já criou a conta dele (email + senha) no painel web antes de chegar aqui — o /setup só faz o Claude Code "logar" com essa mesma conta:

```bash
python3 [caminho da skill]/references/supabase_client.py login CAMINHO/prospector-config.json "email@aluno.com" "senha-dele"
```

Isso salva um `refresh_token` dentro de `prospector-config.json`, bloco `supabase`. **Nunca peça a senha de novo depois disso** — o script renova o acesso sozinho a cada chamada, usando esse token guardado. Se o login falhar, confirme que o aluno já criou a conta pelo painel web antes (é lá que o cadastro acontece, não pelo chat).

## Ler o perfil do aluno (assinatura, nichos, GitHub etc.)

```bash
python3 [caminho]/references/supabase_client.py get-perfil CAMINHO/prospector-config.json
```

Devolve um JSON com `nome`, `apresentacao`, `whatsapp`, `nichos`, `cidade`, `leads_por_busca`, `envio_modo`, `github_usuario`, `github_token`, `github_privado`. Use esses valores em vez de procurar um bloco `github`/`assinatura` dentro do `prospector-config.json` local — a fonte da verdade agora é o Supabase.

## Salvar/atualizar o perfil

```bash
python3 [caminho]/references/supabase_client.py set-perfil CAMINHO/prospector-config.json '{"nome":"...", "github_usuario":"...", "github_token":"..."}'
```

Manda só os campos que mudaram — os outros continuam como estavam salvos.

## Ler leads

```bash
python3 [caminho]/references/supabase_client.py list-leads CAMINHO/prospector-config.json [status]
```

Sem o segundo argumento, lista todos. Com um status (`novo`, `redesenhado`, `publicado`, `proposta`, `respondeu`, `fechado`, `descartado`), filtra.

## Salvar/atualizar um lead

```bash
python3 [caminho]/references/supabase_client.py upsert-lead CAMINHO/prospector-config.json '{"slug":"clinica-vida", "nome":"Clínica Vida", "status":"redesenhado", ...}'
```

`slug` é a chave — se já existir um lead com esse slug pra esse aluno, atualiza; se não, cria. Sempre inclua todos os campos que você tem no momento (o comando não apaga campos que você não mandar, mas é mais seguro mandar o registro completo quando estiver com ele em mãos).

## Como os comandos devem usar isso (SEMPRE)

- `/prospectar` → `upsert-lead` pra cada lead novo (`status: novo`) e cada descartado (`status: descartado`, motivo em `obs`). NUNCA sobrescreva um lead cujo status já avançou — antes de gravar, dê um `list-leads` e confira o status atual daquele slug.
- `/redesenhar` → `upsert-lead` com `status: redesenhado`.
- `/publicar` → `upsert-lead` com `status: publicado` e `url_nova`.
- `/proposta` → `upsert-lead` com `status: proposta` e `data_proposta`.
- `/respostas` → `upsert-lead` com `status: respondeu` quando detectar resposta.
- `/followup` → não muda status, só registra em `obs` que o follow-up foi enviado (pra nunca repetir).
- `/contrato` → `upsert-lead` com `contrato_status`, `contrato_em`, `pago`, `manutencao`, `doc_cliente`, `end_cliente` conforme o estágio.

Status possíveis: `novo | redesenhado | publicado | proposta | respondeu | fechado | descartado`. `contrato_status`: `pendente | enviado | assinado`.

## O que NÃO existe mais

Não há mais `prospector.db`, `dashboard.html` nem `iniciar-dashboard.bat/.command` locais — o painel de controle agora é o site web (com login) que o aluno acessa no navegador, fora do Claude Code. Se o aluno pedir "quero ver meu funil/kanban", oriente-o a abrir o painel web — não tente recriar isso localmente.
