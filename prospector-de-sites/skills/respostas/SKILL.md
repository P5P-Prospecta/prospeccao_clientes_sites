---
name: respostas
description: P5P Prospecta, etapa Respondeu. Confere no Gmail do aluno quem respondeu às propostas e atualiza o painel. Use quando o aluno rodar /respostas ou $respostas (pode vir com o nome do cliente), ou perguntar se algum cliente respondeu.
---

# Respostas (quem respondeu)

Antes de tudo, leia `../prospecta-guia/SKILL.md` (parte "Ler respostas dos clientes").

1. Rode `list-leads proposta` (skill `supabase-sync`): os clientes com proposta enviada (ou só o cliente que o aluno escreveu junto com o comando).
2. Para cada um, procure no Gmail conversas com o e-mail do cliente desde a `data_proposta`, na ordem do guia:
   - ferramenta de Gmail do app (busca do tipo `from:[email] after:[data]` e também a conversa da proposta);
   - sem ferramenta: Gmail aberto no navegador do app (o aluno faz login ali uma vez);
   - sem nenhum dos dois: pergunte ao aluno, cliente por cliente, se ele respondeu e o que disse.
3. Classifique:
   - **Respondeu** (existe mensagem DO cliente): `upsert-lead` com `status: "respondeu"` e um resumo curto em `obs`, por exemplo "Respondeu 09/07: gostou, pediu valores". Mantenha o que já estava em `obs` e acrescente.
   - **Sem resposta**: deixe como `proposta` (o painel mostra quando passa de 3 dias).
4. Resuma para o aluno: quem respondeu (com o essencial de cada resposta), quem segue sem resposta e há quantos dias, e o que fazer: responder o cliente; para os parados há 3 dias ou mais, `followup` (no formato do app).

## Regras

- NUNCA marque `fechado`: fechamento envolve preço e acordo, só o aluno confirma (no painel, ou contando aqui; aí grave `status: "fechado"` e `valor`).
- Não responda e-mails sozinho: só leia e classifique. Se o aluno quiser, escreva um rascunho de resposta.
- Na primeira vez, ofereça deixar isso automático todo dia de manhã, se o app tiver tarefas agendadas ou automações (só com o ok do aluno).
