---
name: prospecta-guia
description: Regras comuns de todas as etapas do P5P Prospecta (setup, prospectar, redesenhar, editor, publicar, proposta, respostas, followup, contrato, proximo) no Claude e no Codex. Leia antes de rodar qualquer etapa do Prospecta. Diz onde ficam os scripts, como chamar o Python, qual navegador usar, como criar e ler e-mails e como sugerir o próximo passo.
---

# P5P Prospecta: regras comuns (Claude e Codex)

O P5P Prospecta roda igual no app do Claude (aba Code) e no app do Codex (ChatGPT). Cada etapa é uma skill. Estas regras valem para todas.

## Quem é o aluno

Aluno do Método P5P, sem experiência técnica. Fale em português do Brasil simples, frases curtas, uma pergunta por vez. Nunca mostre JSON, comandos longos ou caminhos de arquivo sem necessidade. Explique o que vai fazer antes de fazer algo demorado.

## Como o aluno chama as etapas

- No **Claude**: `/setup`, `/prospectar`, `/redesenhar`, `/editor`, `/publicar`, `/proposta`, `/respostas`, `/followup`, `/contrato`, `/proximo`.
- No **Codex**: as mesmas, com `$` no lugar da barra: `$prospectar`, `$publicar` etc.
- Ao sugerir o próximo passo, escreva no formato do app em que você está rodando.
- Se o aluno escreveu algo junto com o comando (ex.: `/prospectar nutricionistas Recife` ou `$publicar Clínica Vida`), use isso como o pedido dele.

## Onde ficam os arquivos

- **Pasta de trabalho**: a pasta aberta no app (no Claude, a pasta escolhida na aba Code; no Codex, o projeto aberto). Nela ficam o `prospector-config.json` (login e cache local) e a pasta `sites/` com as páginas dos clientes. Se não houver pasta aberta, peça para o aluno criar `Documentos/Clientes` e abrir essa pasta no app.
- **Pasta das skills**: este arquivo fica em `<skills>/prospecta-guia/SKILL.md`. As outras skills do Prospecta ficam ao lado, na mesma pasta `<skills>`. Exemplos:
  - script do banco: `<skills>/supabase-sync/references/supabase_client.py`
  - script de publicação: `<skills>/deploy-github-pages/references/publicar-github.py`
  - link do Gmail: `<skills>/proposta-email/references/link_gmail.py`
  - contrato em Word: `<skills>/contrato-servico/references/gerar-docx.py`
- Se não souber o caminho de `<skills>`, procure o arquivo `supabase_client.py` em `~/.claude/skills`, `~/.agents/skills`, `~/.claude/plugins` e `~/.codex`.

## Python

Os scripts do Prospecta usam o Python que vem com o computador, sem instalar pacotes (só o contrato em Word pede `python-docx`).
- **Windows**: use `python` (não `python3`). Confira com `python --version`: tem que aparecer "Python 3". Se não aparecer, ofereça instalar com `winget install -e --id Python.Python.3.12` e peça para o aluno fechar e abrir o app depois.
- **Mac e Linux**: use `python3`.

## Navegador (Google Maps, sites dos clientes, Gmail no navegador)

Use SEMPRE o navegador do próprio app, nesta ordem:
1. **Navegador do app.** No Claude: o navegador embutido do app (painel Browser; ferramentas com `Claude_Browser` no nome, como navigate, get_page_text, read_page, find, computer e javascript_tool). No Codex: o navegador do app (`@Browser`).
2. Só se o app não tiver navegador próprio (por exemplo, no terminal), use a extensão de navegador que o aluno tiver (Claude in Chrome ou a extensão do ChatGPT).
3. Sem navegador nenhum: avise o aluno e pare. Nunca invente dado de cliente.

Dicas:
- Na primeira vez em cada site o app pode pedir permissão. Explique que é normal e peça para o aluno clicar em Permitir.
- Google Maps e sites dos clientes não precisam de login.
- Para ler, prefira o texto da página (ferramentas de leitura de texto ou da estrutura da página). Print só para conferir a aparência.
- Se aparecer captcha ou pedido de login inesperado, pare e avise o aluno.

## Gmail

**Criar e-mail (proposta, follow-up, contrato):**
1. Se o app tiver o Gmail conectado (Claude: conector do Gmail, ferramenta de criar rascunho; Codex: plugin Gmail), crie o RASCUNHO e avise o aluno para revisar e enviar.
2. Se não tiver, ou se a ferramenta não criar rascunho: gere o link "Abrir no Gmail" com o script `link_gmail.py` (skill `proposta-email`). Entregue o link ao aluno: um clique abre o Gmail já preenchido com destinatário, assunto e texto; ele revisa e clica em Enviar. Mostre também o texto no chat.
3. Envio é sempre 1 a 1, feito pela conta Gmail do aluno. Nunca dispare em massa.

**Ler respostas dos clientes:**
1. Ferramenta de Gmail do app (Claude: busca de conversas do conector; Codex: plugin Gmail).
2. Sem ferramenta: abra https://mail.google.com no navegador do app (o aluno faz login ali uma vez) e pesquise `from:email-do-cliente`.
3. Se nada disso funcionar: pergunte ao aluno se o cliente respondeu e o que disse.

## Skill de páginas do curso (impeccable)

O aluno instala a skill de páginas `impeccable` na Aula 1.3 do Método P5P (no Claude e no Codex). O `redesenhar` usa essa skill quando ela existe: no modo rápido (padrão), só as regras de qualidade e o verificador automático, sem perguntas; no modo caprichado (quando o aluno pede), o processo completo dela para um cliente. Sem a skill instalada, tudo funciona igual, só com a `redesign-premium`.

## Perguntas ao aluno

Uma pergunta por vez. Se o app tiver caixa de perguntas com opções (no Claude, AskUserQuestion), use. Senão, pergunte no texto e dê as opções numeradas.

## Mostrar arquivos

Quando gerar páginas (site novo, editor, comparador, contrato), mostre ao aluno: se o app tiver como apresentar o arquivo, use; senão, abra no navegador do app ou diga o nome do arquivo e a pasta.

## Tarefas automáticas

Se o app tiver tarefas agendadas ou automações (Claude: tarefas agendadas; Codex: automações), pode oferecer rodar `respostas` todo dia de manhã. Só crie com o ok do aluno.

## Segurança

- Token do GitHub e senhas nunca aparecem em nenhuma resposta, log ou comando mostrado. A senha do aluno só entra no comando de login do `setup`.
- Nunca marque um cliente como fechado ou pago por conta própria: só quando o aluno disser.
- Nunca invente dado de cliente (nota, serviço, depoimento, contato, preço).

## Painel

Tudo que as etapas gravam aparece no painel: https://prospeccao-clientes-sites.pages.dev (mesmo e-mail e senha). A aba Linha de produção mostra o próximo passo de cada cliente, com o comando pronto para copiar.

## Texto que o cliente final vê

E-mails, páginas, capa da proposta e contrato: português correto, tom humano, sem travessão (use vírgula, dois-pontos ou ponto).
