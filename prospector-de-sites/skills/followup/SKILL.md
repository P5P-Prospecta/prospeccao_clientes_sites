---
name: followup
description: P5P Prospecta, lembrete gentil. Escreve um follow-up (só um por cliente, nunca repete) para propostas sem resposta há 3 dias ou mais e deixa pronto no Gmail do aluno. Use quando o aluno rodar /followup ou $followup (pode vir com o nome do cliente).
---

# Follow-up (lembrete gentil)

Antes de tudo, leia `../prospecta-guia/SKILL.md` e a skill `proposta-email` (`../proposta-email/SKILL.md`).

1. **Confira as respostas ANTES**: faça a conferência da skill `respostas` para não lembrar quem já respondeu (quem respondeu vira `respondeu` e sai da lista).
2. Quem recebe: `list-leads proposta` (skill `supabase-sync`), com `data_proposta` há 3 dias ou mais e SEM follow-up anterior (procure "follow-up" no campo `obs`). Se o aluno escreveu um nome junto com o comando, só esse cliente, mas respeite a regra de um follow-up por cliente.
3. Escreva cada follow-up, no máximo 4 linhas, tom de quem lembra com gentileza e nunca cobra:
   - lembrança leve do primeiro e-mail ("te escrevi semana passada sobre o site");
   - uma pergunta só: "conseguiu ver a página que preparei?" e o mesmo link da capa (único link);
   - sem preço, sem urgência, sem "última chance"; passe pela checklist contra spam da skill `proposta-email`.
4. Deixe pronto no Gmail como manda o guia (rascunho pelo Gmail conectado, ou link "Abrir no Gmail" com `link_gmail.py`). **Um follow-up por cliente, para sempre.**
5. **Painel**: `upsert-lead` acrescentando em `obs` "Follow-up enviado em [data]" (mantenha o que já estava).

## Entrega

Follow-ups prontos, quem respondeu nesse meio tempo (comemore!) e quem já recebeu follow-up e segue sem resposta: sugira tentar o WhatsApp ou descartar no painel. Pode oferecer deixar `respostas` automático todo dia, se o app tiver tarefas agendadas.
