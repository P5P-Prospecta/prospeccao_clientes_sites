---
name: contrato
description: P5P Prospecta, etapa Fechado. Gera o contrato de prestação de serviço do cliente que fechou (folha para imprimir e Word travado) e deixa o e-mail pronto no Gmail do aluno. Use quando o aluno rodar /contrato ou $contrato (pode vir com o nome do cliente), ou disser que um cliente fechou.
---

# Contrato

Antes de tudo, leia `../prospecta-guia/SKILL.md` e a skill `contrato-servico` (`../contrato-servico/SKILL.md`).

1. Cliente: o nome que o aluno escreveu junto com o comando; senão, liste os clientes com status `fechado` ou `respondeu` e pergunte qual.
2. Junte o que o Prospecta JÁ tem: nome do cliente, cidade, valor fechado, link da página publicada, escopo (página refeita e publicação) e os dados do prestador (campo `contratante` do `prospector-config.json`; se não existir, pergunte UMA vez e salve ali).
3. Dados do cliente: veja `doc_cliente` e `end_cliente` no banco. Pergunte só o que faltar. Se o aluno colar a mensagem do cliente com CPF ou endereço, extraia e grave no banco (`doc_cliente`, `end_cliente`). Confirme também forma de pagamento, prazo de entrega e manutenção mensal (valor).
4. Gere as duas versões:
   - **Folha para imprimir**: `../contrato-servico/references/contrato-template.html`, trocando TODOS os `{{...}}`. Salve em `sites/[slug]/contrato-[slug].html`. Para PDF: abrir no navegador, Ctrl+P, Salvar como PDF.
   - **Word travado** (o que vai para o cliente): monte um `dados.json` com as mesmas chaves e `MANUTENCAO`/`VALOR_MANUTENCAO` e rode `python <skills>/contrato-servico/references/gerar-docx.py dados.json sites/[slug]/contrato-[slug].docx` (Windows `python`, Mac `python3`). Precisa do pacote `python-docx`: se faltar, instale com `python -m pip install python-docx`. O cliente só consegue preencher os campos em amarelo (CPF, endereço, data, assinatura).
5. **E-mail do contrato**, como manda o guia: rascunho pelo Gmail conectado ou link "Abrir no Gmail" com `link_gmail.py`. Assunto: "Contrato de prestação de serviço: nova página [nome do negócio]". Corpo curto: agradecer, resumir o combinado (escopo, valor, prazo), pedir para ler, preencher os campos destacados e devolver respondendo o e-mail. O arquivo Word vai anexado: se a ferramenta não anexar (ou no link "Abrir no Gmail"), diga ao aluno o caminho do `.docx` para ele anexar antes de enviar.
6. **Painel**: `upsert-lead` com `status: "fechado"` (se ainda não estava), `valor`, `contrato_status: "enviado"`, `contrato_em` (hoje) e `manutencao` (se contratada). Quando o aluno contar que o cliente assinou: `contrato_status: "assinado"`. Quando contar que recebeu: `pago: true`. Ele também pode marcar isso no painel, na ficha do cliente.

## Devolução assinada

Quando o cliente devolver o contrato assinado, salve como `sites/[slug]/contrato-[slug]-assinado.docx` (ou .pdf) e grave `contrato_status: "assinado"`.

## Regras

- O contrato é MINUTA BASE: o aviso de revisão jurídica do rodapé nunca sai.
- Valor, prazo e forma de pagamento vêm do aluno ou do banco: nunca invente.
