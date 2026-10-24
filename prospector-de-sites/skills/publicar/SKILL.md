---
name: publicar
description: P5P Prospecta, etapa No ar. Publica as páginas refeitas no GitHub Pages do aluno (de graça, com cadeado), junto com a capa da proposta, e grava o link no painel. Use quando o aluno rodar /publicar ou $publicar (pode vir com o nome do cliente ou "todos").
---

# Publicar (colocar a página no ar)

Antes de tudo, leia `../prospecta-guia/SKILL.md`. A publicação segue a skill `deploy-github-pages`.

1. Rode `get-perfil` (skill `supabase-sync`). Se faltar usuário ou token do GitHub, pare e mande o aluno rodar `setup` (no formato do app) ou preencher em Configurações > GitHub no painel.
2. O que publicar: o cliente (ou "todos") que o aluno escreveu junto com o comando. Se não escreveu, rode `list-leads redesenhado` e pergunte.
3. **Capa da proposta**: preencha `../proposta-email/references/capa-proposta-template.html` com os dados do cliente e a assinatura do perfil e salve em `sites/[slug]/proposta.html`. É ela que vai no e-mail.
4. **Publicar**: grave `github_usuario`, `github_token` e `github_privado` do perfil no bloco `github` do `prospector-config.json` (é só um cache local para o script ler). Para cada cliente (Windows com `python`, Mac com `python3`):
   ```
   python <skills>/deploy-github-pages/references/publicar-github.py <pasta de trabalho>/prospector-config.json [slug] "<pasta de trabalho>/sites/[slug]/[slug].html:index.html" "<pasta de trabalho>/sites/[slug]/proposta.html:proposta.html"
   ```
   O script cria o repositório, sobe os arquivos, liga o GitHub Pages e testa o endereço sozinho.
5. Pegue no resultado do script os endereços finais (`https://[usuario].github.io/[slug]/` e `.../proposta.html`). Se o primeiro acesso ainda não respondeu, espere 1 a 2 minutos e teste de novo antes de avisar.
6. **Painel**: `upsert-lead` com `status: "publicado"` e `url_nova`.

## Entrega

Para cada cliente: o link da página nova e o link da capa, os dois conferidos no ar. Próximo passo, no formato do app: `proposta`.
