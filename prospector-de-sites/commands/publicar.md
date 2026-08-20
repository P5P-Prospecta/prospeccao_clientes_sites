---
description: Publica as páginas redesenhadas no GitHub Pages e retorna as URLs públicas
argument-hint: "[nome do cliente ou todos]"
---

Publique páginas no GitHub Pages seguindo a skill `deploy-github-pages`.

## Passos

1. Rode `get-perfil` (skill `supabase-sync`). Se `github_usuario` ou `github_token` não estiverem preenchidos, rode `/setup` primeiro — não prossiga sem eles.
2. Determine o que publicar: `$ARGUMENTS` (um cliente ou "todos"), ou liste as páginas com status `redesenhado` em `leads.md` e pergunte.
3. **Gere a página-capa de cada cliente**: preencha `references/capa-proposta-template.html` (skill `proposta-email`) com os dados do lead + assinatura do config e salve como `sites/[slug]/proposta.html`. É ela que vai no e-mail de proposta.
4. **Publique seguindo a skill `deploy-github-pages`**: antes de rodar o script, grave `github_usuario`/`github_token`/`github_privado` do perfil (obtidos no passo 1) no bloco `github` de `prospector-config.json` (é só um cache local temporário pro script ler — a fonte da verdade continua sendo o Supabase). Depois, para cada cliente:
   ```
   python3 [caminho da skill]/references/publicar-github.py CAMINHO/prospector-config.json [slug] \
     "CAMINHO/sites/[slug]/[slug].html:index.html" \
     "CAMINHO/sites/[slug]/proposta.html:proposta.html"
   ```
   O script cria o repositório, sobe os arquivos, ativa o GitHub Pages e testa a URL sozinho — sem etapas manuais do usuário.
5. Colete do output do script as URLs finais (`https://[usuario].github.io/[slug]/` e `.../proposta.html`). Se o script avisar que o primeiro build ainda não respondeu, aguarde ~1-2 minutos e teste de novo antes de reportar.
6. Atualize com `upsert-lead` (skill `supabase-sync`): `status: "publicado"` + `url_nova`.

## Saída

Liste, por cliente: URL da página nova e URL da capa (`.../proposta.html`), ambas confirmadas no ar. Sugira o próximo passo: `/proposta` para enviar os e-mails.
