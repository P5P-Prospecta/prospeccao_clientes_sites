# Prospector de Sites v3.2.0 (P5P Prospecta)

Prospecção de clientes com sites ruins: acha, redesenha, publica e oferta. Roda no app do Claude e no app do Codex, pelo navegador do próprio app.

## Como está organizado

Tudo são skills, em `skills/`. Cada etapa é uma skill que o aluno chama pelo nome (`/nome` no Claude, `$nome` no Codex):

- **Etapas:** `setup`, `prospectar`, `redesenhar`, `editor`, `publicar`, `proposta`, `respostas`, `followup`, `contrato`, `proximo`.
- **Apoio:** `prospecta-guia` (regras comuns: pasta de trabalho, Python, navegador do app, Gmail, segurança), `prospeccao-maps`, `redesign-premium`, `deploy-github-pages`, `proposta-email`, `contrato-servico`, `supabase-sync`.
- **Scripts** (só biblioteca padrão do Python): `supabase-sync/references/supabase_client.py` (login, perfil, clientes, próximos passos), `deploy-github-pages/references/publicar-github.py`, `proposta-email/references/link_gmail.py` (link "Abrir no Gmail"), `contrato-servico/references/gerar-docx.py` (precisa de `python-docx`).
- **Manual do aluno:** `skills/setup/manual.html`.

## Instalação

O instalador da raiz do repositório (`instalar.ps1` no Windows, `instalar.sh` no Mac) copia todas as pastas de `skills/` para `~/.claude/skills` e `~/.agents/skills`. Rodar de novo atualiza. Também continua instalável como plugin do Claude Code (`.claude-plugin/plugin.json`).

## O ciclo

1. `setup`: roda uma vez (login do painel, perfil, GitHub com teste, Gmail, manual).
2. `prospectar [nicho] [cidade]`: Google Maps pelo navegador do app, pula anúncios, grava cada cliente no painel (meta padrão 10, teto de 25 avaliados).
3. `redesenhar`: refaz as páginas dos 5 ou mais melhores com o conteúdo, logo e fotos reais.
4. `editor [cliente]`: versão editável no navegador, com exportação.
5. `publicar [cliente|todos]`: GitHub Pages em `[usuario].github.io/[slug]/`, com a capa `proposta.html`.
6. `proposta [cliente|todos]`: e-mail sem preço, checklist contra spam, rascunho no Gmail conectado ou link "Abrir no Gmail".
7. `respostas`: quem respondeu (Gmail do app, Gmail no navegador do app, ou perguntando ao aluno).
8. `followup [cliente]`: um lembrete gentil por cliente, depois de 3 dias.
9. `contrato [cliente]`: minuta em folha A4 e Word travado.
10. `proximo`: o que fazer agora com cada cliente.

## Onde ficam os dados

`prospector-config.json` na pasta de trabalho (token renovável do login e cache local) e o banco do painel (clientes, perfil, GitHub), visível em https://prospeccao-clientes-sites.pages.dev.
