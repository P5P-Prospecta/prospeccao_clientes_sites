---
name: deploy-github-pages
description: Esta skill deve ser usada ao publicar páginas via GitHub Pages — cria (ou reaproveita) um repositório por cliente, sobe os arquivos pela API do GitHub, ativa o GitHub Pages e devolve a URL pública. Acione quando o usuário disser "publicar", "subir o site", "colocar no ar", "deploy", "github", "github pages" ou rodar /publicar ou o teste de conexão do /setup.
---

# Deploy via GitHub Pages (gratuito)

Publicar cada cliente em `https://[usuario-github].github.io/[slug]/` (ou `https://[dominio-custom]/` se o cliente tiver domínio próprio configurado), sem depender de hospedagem paga nem de nenhum programa instalado no computador do usuário.

Diferente da HostGator, a API do GitHub (`api.github.com`) é acessível diretamente de onde o Claude roda — então a publicação é feita **na hora, no próprio comando**, sem fila, sem publicador local, sem espera de ~90s.

## Credenciais

Tudo vem de `prospector-config.json` (bloco `github`): `usuario` (login/organização do GitHub), `token` (Personal Access Token com escopo `repo`), `privado` (true/false — repositórios privados também publicam Pages normalmente em contas Pro/Team/Enterprise; em conta free, Pages só funciona com repositório público, então o padrão é `false`).

**O token vive SÓ nesse arquivo, no computador do usuário — nunca é digitado no chat, nunca é exibido em nenhuma saída, log ou comando mostrado ao usuário.** Se o token estiver vazio, oriente o usuário a gerar um em https://github.com/settings/tokens (Personal access tokens → Tokens (classic) → escopo `repo`) e colar no `prospector-config.json` diretamente (nunca pelo chat).

## Publicação (método único — direto pela API, sem passos alternativos)

Use o script `references/publicar-github.py` (Python padrão, sem dependências externas — roda igual em Windows/Mac/Linux):

```bash
python3 references/publicar-github.py CAMINHO/prospector-config.json [slug] \
  "CAMINHO/sites/[slug]/[slug].html:index.html" \
  "CAMINHO/sites/[slug]/proposta.html:proposta.html"
```

O script, em ordem:
1. Cria o repositório `[slug]` na conta/organização do `usuario` (se já existir, reaproveita).
2. Sobe cada arquivo indicado (`local:caminho-no-repo`) via API de Contents — cria ou atualiza (detecta o SHA atual antes de sobrescrever).
3. Ativa o GitHub Pages nesse repositório (branch `main`, raiz `/`).
4. Imprime a URL pública final (`https://[usuario].github.io/[slug]/`) e a da capa (`.../proposta.html`), já testadas com `HEAD`.

Se o script falhar (token inválido, limite de repositórios, rede bloqueada), leia a mensagem de erro impressa e diagnostique antes de tentar de novo — nunca reexecute em loop sem entender a causa.

## Domínio próprio (opcional, por cliente)

Se o cliente já tem domínio e quer usar no site novo: crie um arquivo `CNAME` (sem extensão) na raiz do repositório contendo só o domínio (ex.: `site.clientex.com.br`) e oriente o usuário a criar, no DNS do domínio, um registro `CNAME` apontando para `[usuario].github.io`. O script aceita esse arquivo como mais um item da lista de upload (`CAMINHO/CNAME:CNAME`). Sem isso, a URL padrão do GitHub Pages já funciona sozinha, com HTTPS automático.

## Verificação (obrigatória, após publicar)

1. O GitHub Pages pode levar até ~1 minuto para o site ficar no ar na primeira publicação de um repositório novo (builds seguintes são quase instantâneos). Se a URL ainda não responder, aguarde e teste de novo antes de reportar erro.
2. HTTPS é automático e obrigatório no GitHub Pages — nunca há link `http://` a se preocupar aqui.
3. Atualize com `upsert-lead` (skill `supabase-sync`): `status: "publicado"` e `url_nova`.

## Teste de conexão do /setup

Publique um `teste.html` simples ("Funcionou!") num repositório `prospector-teste` seguindo o mesmo fluxo; se der certo, a URL confirma que token e usuário estão corretos.
