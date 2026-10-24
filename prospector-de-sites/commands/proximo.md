---
description: Mostra o que fazer agora com cada cliente (parados primeiro) e o comando certo para cada um
---

Mostre ao aluno o próximo passo de cada cliente. É a mesma lista da aba "Linha de produção" do painel web, só que aqui no chat.

## Passos

1. Rode o `proximos` da skill `supabase-sync` (no Windows, troque `python3` por `python` se precisar):
   ```
   python3 [caminho da skill supabase-sync]/references/supabase_client.py proximos CAMINHO/prospector-config.json
   ```
2. Mostre o resultado em português simples, do jeito que veio: primeiro os parados, depois os que estão andando. Não mostre JSON nem caminho de arquivo.
3. Se a lista vier vazia, explique o começo: `/setup` (se ainda não fez) e depois `/prospectar`.
4. Pergunte se o aluno quer rodar agora o primeiro comando da lista. Se ele disser que sim, siga o comando correspondente (por exemplo, o `/followup` daquele cliente). Não rode nada sem o ok dele.
5. Lembre que o painel web mostra a mesma lista, com um botão de copiar em cada comando: https://prospeccao-clientes-sites.pages.dev

## Regras

- Este comando só lê: não muda o status de ninguém.
- Fechado, contrato assinado e pagamento dependem do aluno. Ele marca no painel ou conta aqui; se contar aqui, registre com `upsert-lead` (skill `supabase-sync`): `status: "fechado"` e `valor`, `contrato_status: "assinado"`, ou `pago: true`.
- Nunca invente dado de cliente nem valor.
