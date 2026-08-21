# Prospector de Sites — Log do Projeto

> Este arquivo é um log vivo da sessão de trabalho neste repositório. Mantenha atualizado a cada mudança relevante — é a fonte de verdade sobre decisões, achados e pendências deste projeto.

## O que é

Plugin do Claude Code (`prospector-de-sites/`) para prospecção semi-automática de clientes de web design: acha negócios bem avaliados no Google Maps com sites ruins, redesenha, publica no GitHub Pages e envia proposta por e-mail. Vendido/distribuído pra uma turma de alunos via marketplace do Claude Code — todos compartilham o mesmo projeto Supabase, isolados por RLS (login próprio de cada aluno).

## Repo e estrutura

- **Local**: `C:\Users\Itamar\Documents\NOVOS SISTEMAS\PROSPECTOR DE SISTES\PROSPECTOR-DE-SITES-supabase\PROSPECTOR-DE-SITES-main`
- **GitHub**: repo privado `sistemaconnectfood/prospeccao_clientes_sites` (renomeado de `arrecheneto-plugins`), branch `main`.
- Conteúdo: `.claude-plugin/marketplace.json` (raiz) + `prospector-de-sites/` (o plugin: `commands/*.md`, `skills/*/SKILL.md`, `skills/supabase-sync/references/supabase_client.py`) + `painel-web/index.html` (frontend estático, Supabase JS client) + `sql/schema.sql`.
- Instalar: `/plugin marketplace add sistemaconnectfood/prospeccao_clientes_sites` → `/plugin install prospector-de-sites@prospeccao_clientes_sites`.
- **Importante ao editar**: editar sempre este repo fonte, nunca a pasta de cache do plugin instalado (`~/.claude/plugins/cache/.../prospector-de-sites/<versão>/`) — ela é sobrescrita a cada `/plugin update`/reinstalação e não é rastreada aqui. Depois de commitar+pushar aqui, `/plugin marketplace update <nome>` só atualiza o índice do marketplace; pra puxar o conteúdo novo de fato é preciso `/plugin uninstall` + `/plugin install` (ou `/plugin update`) do plugin em si.

## Frontend (painel-web)

Deployado no Cloudflare Pages, projeto `prospeccao-clientes-sites`, live em https://prospeccao-clientes-sites.pages.dev — deploy via `wrangler pages deploy painel-web --project-name=prospeccao-clientes-sites --branch=main` (conta Cloudflare `das.automacao.ia@gmail.com`, `wrangler login`). Redeploy com o mesmo comando após editar `painel-web/index.html`.

## Backend (Supabase)

Projeto `jzlkqzamkgxxlbmpfisq`. Chave anon é pública por design (protegida por RLS). Auth por email/senha (`sb.auth.signInWithPassword`/`signUp`).

Tabelas:
- **`perfis`**: `user_id`, `nome`, `apresentacao`, `whatsapp`, `nichos` (array), `cidade`, `leads_por_busca` (padrão 10), `envio_modo`, `github_usuario`, `github_token`, `github_privado`.
- **`leads`** (schema real confirmado via `list-leads`, não documentado em nenhum SQL no repo até agora — **conferir aqui antes de assumir nomes de coluna**): `id`, `user_id`, `slug`, `nome`, `nicho`, `cidade`, `nota`, `avaliacoes`, `email`, `telefone`, `whatsapp`, `site_antigo` (⚠️ não `site_atual`), `motivo`, `status`, `url_nova`, `data_proposta`, `valor`, `obs`, `contrato_status` (default `pendente`), `contrato_em`, `manutencao`, `pago` (default `false`), `doc_cliente`, `end_cliente`, `criado_em`, `atualizado_em`. Status: `novo | redesenhado | publicado | proposta | respondeu | fechado | descartado`.

## ⚠️ Gotcha — `upsert-lead` do `supabase_client.py` não faz upsert de verdade em slug já existente

`upsert_lead()` faz um POST simples com header `Prefer: resolution=merge-duplicates`, mas **sem `?on_conflict=`** na URL — o PostgREST não infere sozinho qual constraint usar (`leads_user_id_slug_key`), então um slug repetido dá **409 duplicate key** em vez de atualizar. Confirmado reproduzindo o erro em 2026-08-20.

Workaround usado nesta sessão (não commitado no repo — script solto no scratchpad da sessão): fazer um `GET` filtrando por `user_id`+`slug` primeiro; se existir, `PATCH` no mesmo filtro; se não, `POST`. Se for mexer nisso de novo, considerar corrigir direto no `supabase_client.py` (adicionar `?on_conflict=user_id,slug` na URL do POST) em vez de reimplementar o wrapper toda vez.

## ⚠️ Gotcha — `python3`/`py` não estão no PATH do Git Bash desta máquina

Só existe o stub da Microsoft Store em `AppData\Local\Microsoft\WindowsApps` (abre a loja se rodado sem argumento). O Python real está em `C:\Users\Itamar\AppData\Local\Programs\Python\Python312\python.exe` (instalado via winget, só não foi adicionado ao PATH do Git Bash). Chamar `supabase_client.py` sempre pelo caminho completo desse executável, não por `python3`/`py`.

## 🆕 Removida dependência de Google Sheets/Drive (2026-08-20/21, commit `a71eaf5`)

O conector do Google Drive **não está disponível no Claude Code** — a instrução antiga (`/prospectar` deveria salvar os leads numa planilha do Google via `create_file`) travava sem erro claro. Todos os comandos/skills (`prospectar`, `redesenhar`, `publicar`, `proposta`, `respostas`, `followup`, `deploy-github-pages`, `proposta-email`, `prospeccao-maps`) foram reescritos pra ler/gravar leads **só no Supabase** via `upsert-lead`/`list-leads` (skill `supabase-sync`), sem depender de `leads.md` local nem de planilha. A skill `prospeccao-maps` também ganhou um teto rígido explícito: parar a avaliação assim que bater **25 estabelecimentos avaliados** (não é mais só uma sugestão) OU a meta de leads qualificados, o que vier primeiro — sem trocar de nicho no meio pra tentar completar a meta sem perguntar antes.

Pendência conhecida: o commit foi feito sem `user.name`/`user.email` configurados globalmente no git local, então ficou assinado como "Itamar de Souza <itamar@intranet.fenix>" — perguntar ao usuário se quer configurar isso antes do próximo commit.

## Estado dos dados de teste (conta `das.automacao.ia@gmail.com`)

Perfil do aluno de teste: nichos padrão `nutricionistas`, `psicologos`, `advogados`, `psiquiatras`, `leads_por_busca: 10`, `cidade` ainda **não definida** no perfil (perguntar toda vez que faltar).

Rodadas de prospecção já rodadas (tudo gravado em `leads` via Supabase):
- **Rodada 1 — Recife-PE, nichos clínicas/consultórios** (odontologia, estética, fisioterapia, psicologia): 43 avaliados, **2 qualificados**: `denise-alcantara-fisioterapia` (Clínica de Fisioterapia Denise Alcântara, site com layout datado + seções quebradas) e `casa-da-psique-psicologia` (Clínica de Psicologia - Casa da Psiquê, tema WordPress datado sem SSL). Ambos com status `novo`, aguardando `/redesenhar`.
- **Rodada 2 — Recife-PE, psiquiatras**: 21 avaliados, **0 qualificados** — mercado saturado (quem se destaca já tem site bom, ou usa só agregador tipo Doctoralia sem site próprio). Achado curioso: um candidato (Dr. João Carlos Leitão) tinha um site secundário com bugs reais (rolagem do mouse quebrada, textão desorganizado) mas foi descartado porque ele já tem um site principal moderno em paralelo — não faz sentido pitchar redesign pra quem já investiu nisso.

**Próximo passo combinado com o usuário**: rodar `/redesenhar` nos 2 leads qualificados da Rodada 1, e/ou tentar mais um nicho (nutricionistas/advogados) ou outra cidade antes disso.

## Referências

[[feedback_wants_direct_links]] — sempre dar a URL direta (pages.dev, GitHub) em vez de só passo a passo. [[feedback_respond_in_pt_br]] aplica. [[feedback_supabase_missing_rls_update_policy_silent]] — atenção geral a esse padrão de falha silenciosa em qualquer tabela nova. Docs de uso completas (não deste log de desenvolvimento) ficam em `prospector-de-sites/README.md` e `COMO-PUBLICAR.md`.
