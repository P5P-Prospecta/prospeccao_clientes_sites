---
name: proximo
description: P5P Prospecta, o que fazer agora. Lista cada cliente com a estação em que está, o que falta fazer e o comando certo, com os parados primeiro (a mesma lista da Linha de produção do painel). Use quando o aluno rodar /proximo ou $proximo, ou perguntar "o que eu faço agora?" sobre os clientes.
---

# Próximo passo de cada cliente

Antes de tudo, leia `../prospecta-guia/SKILL.md`.

1. Rode (Windows com `python`, Mac com `python3`; no Codex acrescente `--app codex` para os comandos saírem com `$`):
   ```
   python <skills>/supabase-sync/references/supabase_client.py proximos <pasta de trabalho>/prospector-config.json
   python <skills>/supabase-sync/references/supabase_client.py proximos <pasta de trabalho>/prospector-config.json --app codex
   ```
2. Mostre o resultado em português simples, do jeito que veio: primeiro os parados, depois os que estão andando. Sem JSON e sem caminho de arquivo.
3. Lista vazia: explique o começo (`setup`, se ainda não fez, e depois `prospectar`).
4. Pergunte se o aluno quer rodar agora o primeiro comando da lista. Se sim, siga a skill daquele comando. Não rode nada sem o ok dele.
5. Lembre que o painel mostra a mesma lista com botão de copiar: https://prospeccao-clientes-sites.pages.dev

## Regras

- Só lê: não muda o status de ninguém.
- Fechado, contrato assinado e pagamento dependem do aluno. Se ele contar aqui, grave com `upsert-lead`: `status: "fechado"` e `valor`, `contrato_status: "assinado"` ou `pago: true`.
