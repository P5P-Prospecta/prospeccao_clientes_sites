---
name: proposta
description: P5P Prospecta, etapa Proposta. Escreve a proposta por e-mail para os clientes com página no ar (sem preço, com a capa antes e depois como único link) e deixa pronta no Gmail do aluno, como rascunho ou como link "Abrir no Gmail". Use quando o aluno rodar /proposta ou $proposta (pode vir com o nome do cliente ou "todos").
---

# Proposta por e-mail

Antes de tudo, leia `../prospecta-guia/SKILL.md` (parte do Gmail) e a skill `proposta-email` (`../proposta-email/SKILL.md`), que tem a estrutura do e-mail e a checklist contra spam.

1. Rode `get-perfil` (assinatura e modo de envio) e `list-leads publicado` (skill `supabase-sync`).
2. Para quem: o cliente (ou "todos") que o aluno escreveu junto com o comando; senão, todos com status `publicado` que ainda não receberam proposta. Só quem tem e-mail. Sem e-mail: diga que a abordagem vai pelo WhatsApp e entregue o texto adaptado com o link `https://wa.me/[whatsapp]`.
3. Escreva cada e-mail seguindo a skill `proposta-email`, com os dados reais: elogio baseado nas avaliações do Google, o defeito objetivo anotado na prospecção e, como ÚNICO link, a capa publicada (`https://[usuario].github.io/[slug]/proposta.html`). Se a capa não estiver no ar, publique antes (skill `publicar`). NUNCA fale de preço.
4. **Checklist contra spam (obrigatória)**: 1 link só, sem palavras de promoção, sem anexo, assunto em forma de pergunta com até 60 caracteres, primeira linha personalizada. Reescreva até passar em tudo.
5. **Deixar pronto no Gmail**, como manda o guia:
   - com Gmail conectado no app: crie o rascunho (modo rascunho) e avise que está na caixa de rascunhos para revisar;
   - sem Gmail conectado (ou se não criar rascunho): gere o link com `link_gmail.py` (skill `proposta-email`) e entregue "Abrir no Gmail" para cada cliente, com o texto também no chat;
   - modo "enviar direto": só se o app tiver como enviar; senão, faça o rascunho ou o link e avise.
6. **Painel**: `upsert-lead` com `status: "proposta"` e `data_proposta` de hoje (formato AAAA-MM-DD). Grave quando o rascunho ou o link estiver pronto.

## Entrega

Quantas propostas ficaram prontas e para quem, com o link da capa de cada uma. Lembre, no formato do app: `respostas` confere quem respondeu e `followup` cuida de quem está 3 dias ou mais sem responder.
