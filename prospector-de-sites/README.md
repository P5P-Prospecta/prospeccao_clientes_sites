# Prospector de Sites — v2.2.0

Prospecção semi-automática de clientes com sites ruins: acha, redesenha, publica e oferta.

## O ciclo

1. `/setup` — roda uma vez: assinatura, nichos padrão, conexão com o GitHub (com teste de publicação).
2. `/prospectar [nicho] [cidade]` — busca no Google Maps negócios nota ≥ 4.7 com site fraco e gera `leads.md` com e-mail, motivo e ranking (padrão: 10 leads).
3. `/redesenhar` — recria as páginas dos 5+ melhores leads com estética premium, mantendo o conteúdo, logo e paleta reais do cliente.
4. `/editor [cliente]` — gera versão editável no navegador (textos e imagens) com exportação da página final.
5. `/publicar [cliente|todos]` — sobe no GitHub Pages em `[usuario].github.io/[slug]/`, gera a página-capa de apresentação (antes/depois personalizado, `proposta.html`) — HTTPS já vem automático.
6. `/proposta [cliente|todos]` — escreve o e-mail (rapport, sem preço), passa pela checklist anti-spam e cria o rascunho no Gmail com a página-capa como único link.
7. `/respostas` — verifica no Gmail quem respondeu e atualiza o dashboard sozinho (dica: agende a verificação diária).
8. `/followup [cliente]` — 3+ dias sem resposta? Gera o follow-up gentil (1 por lead, nunca repete) já checando quem respondeu antes.
9. `/contrato [cliente]` — cliente fechou? Gera a minuta do contrato (pronta pra PDF) com os dados do negócio e deixa o rascunho no Gmail.

## Manual e publicação automática

O pacote inclui `manual.html` — o manual completo do usuário, copiado pra pasta no `/setup` e **atualizado a cada versão do plugin**. A publicação é gratuita e automática via GitHub Pages: token gerado uma vez em github.com/settings/tokens e preenchido no `prospector-config.json` (ou pelo dashboard) — o `/publicar` faz o resto sozinho, direto pela API do GitHub, sem instalar nada no computador.

## Dashboard local

O plugin grava tudo num banco Supabase compartilhado da turma — cada aluno só vê os próprios dados (login por e-mail e senha). O painel de controle é um site web à parte: kanban com drag & drop, edição, exclusão, funil, comparador antes/depois integrado, follow-ups, controle de contratos (pendente/enviado/assinado) e painel financeiro (recebido, a receber e MRR das manutenções), tudo salvo no banco.

## Requisitos

- Extensão Claude in Chrome conectada (prospecção no Maps)
- Conector do Gmail (rascunhos de proposta)
- Pasta conectada no Cowork (armazena config, leads e sites)
- Conta gratuita no GitHub (hospedagem via GitHub Pages)

## Onde ficam os dados

Tudo na pasta conectada: `prospector-config.json` (preferências e credenciais — o token do GitHub fica em texto no seu computador), `leads.md` (pipeline) e `sites/[slug]/` (páginas criadas).

## Como atualizar

No chat: `/plugin marketplace update arrecheneto-plugins` e reinicie o app (versão certa: 2.2.0). Da 2.1.0 em diante, atualiza sozinho.
