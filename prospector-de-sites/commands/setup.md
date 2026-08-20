---
description: Configura o plugin — login no Supabase, assinatura, preferências e conexão com o GitHub (roda uma vez)
---

Configure o ambiente do Prospector de Sites. Siga esta ordem:

## 1. Pasta de trabalho

Verifique se há uma pasta do usuário conectada. Se não houver, peça para conectar uma pasta (ex.: "Clientes") usando a ferramenta de solicitação de pasta — é nela que fica o `prospector-config.json` com a identidade de login e os arquivos temporários de trabalho (sites sendo criados antes de publicar).

## 2. Login no Supabase (obrigatório, primeiro passo de verdade)

Pergunte se o aluno já criou a conta dele no painel web do Prospector de Sites (fora do chat, no navegador). Se ainda não criou, oriente a fazer isso agora antes de continuar — é lá que o cadastro (email + senha) acontece, nunca pelo chat.

Com a conta já criada, rode o login seguindo a skill `supabase-sync`:
```
python3 [caminho da skill]/references/supabase_client.py login CAMINHO/prospector-config.json "email-do-aluno" "senha-do-aluno"
```
Isso salva só um token de acesso renovável no `prospector-config.json` — a senha não fica guardada em lugar nenhum depois deste comando. Se der erro, confirme que o e-mail/senha batem com o cadastro feito no painel web.

## 3. Verificar perfil existente

Rode `get-perfil` (skill `supabase-sync`). Se já vier preenchido, mostre um resumo (sem exibir o token do GitHub) e pergunte o que o usuário quer atualizar. Se vier vazio, colete os dados abaixo.

## 4. Dados do usuário (perguntar via AskUserQuestion / formulário)

Colete:

- **Assinatura da proposta**: nome completo, como quer se apresentar (ex.: "Designer de páginas de alta conversão") e WhatsApp/telefone de contato.
- **Nichos padrão de prospecção**: sugira nutricionistas, psicólogos, advogados e psiquiatras como ponto de partida, mas deixe o usuário editar livremente.
- **Cidade/região padrão**.
- **Leads qualificados por busca**: padrão 10.
- **Modo de envio da proposta**: padrão "criar rascunho no Gmail para revisão" (recomendado). Alternativa: enviar direto.

Salve tudo de uma vez com `set-perfil` (skill `supabase-sync`): `nome`, `apresentacao`, `whatsapp`, `nichos`, `cidade`, `leads_por_busca`, `envio_modo`.

## 5. Conexão com o GitHub (hospedagem gratuita via GitHub Pages)

Pergunte se o usuário já tem conta no GitHub.

- **Se ainda não tem**: oriente a criar uma gratuita em https://github.com/signup e depois voltar pra continuar o setup.
- **Se já tem**: NÃO colete o token pelo chat de forma que fique exposto na conversa — peça que ele gere e informe apenas quando estiver pronto para colar diretamente no comando:
  1. Acesse https://github.com/settings/tokens → **Generate new token** → **Tokens (classic)**.
  2. Dê um nome (ex.: "prospector-de-sites"), marque só o escopo `repo` e gere.
  3. Copie o token (só aparece uma vez).

  Assim que o aluno colar o token e o usuário do GitHub, salve com `set-perfil`: `{"github_usuario": "...", "github_token": "...", "github_privado": false}`. Nunca exiba, imprima ou registre o token de volta em nenhuma saída. Repositórios ficam públicos por padrão (`github_privado: false`) — necessário para o GitHub Pages funcionar em contas gratuitas; se o usuário tiver conta paga (Pro/Team/Enterprise) e preferir repositórios privados, pode trocar para `true`.

## 6. Testar a conexão com o GitHub

Teste seguindo a skill `deploy-github-pages`: publique uma página `teste.html` simples num repositório `prospector-teste` (buscando `github_usuario`/`github_token` via `get-perfil`) e informe a URL pública ao usuário. Se o teste falhar, diagnostique (token inválido/expirado, escopo errado, nome de usuário) antes de concluir.

## 7. Entregar o manual

Copie `manual.html` da pasta do plugin para a pasta conectada (sobrescrevendo versões antigas). A publicação em si (skill `deploy-github-pages`) não precisa de nenhum instalador — roda direto pela API do GitHub em qualquer `/publicar`. Apresente o `manual.html` ao usuário com a frase: "Esse é o seu manual — guarda ele que responde 90% das dúvidas."

## 8. Encerrar

Confirme o que foi salvo e explique o ciclo (guiando SEMPRE o próximo passo ao fim de cada comando): `/prospectar` → `/redesenhar` → `/publicar` → `/proposta`, com `/editor` opcional para ajustes manuais e o painel web (com login) como painel de controle de tudo — leads, funil, contratos e financeiro.
