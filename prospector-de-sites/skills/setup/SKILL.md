---
name: setup
description: P5P Prospecta, primeira etapa (roda uma vez). Configura o Prospecta no Claude ou no Codex do aluno: confere o Python, a pasta de trabalho, faz o login com a conta do painel, preenche o perfil, conecta o GitHub e mostra como usar o Gmail. Use quando o aluno rodar /setup ou $setup, ou disser "configurar o Prospecta".
---

# Setup do P5P Prospecta

Antes de tudo, leia as regras comuns em `../prospecta-guia/SKILL.md` (ao lado desta pasta). Siga esta ordem e explique cada passo em uma frase. Se algo já estiver pronto, diga e pule.

## 1. Python

Confira o Python como manda o guia (`python --version` no Windows, `python3 --version` no Mac). Se faltar, ofereça instalar (Windows: `winget install -e --id Python.Python.3.12`) e peça para o aluno fechar e abrir o app. Sem Python o Prospecta não grava nada.

## 2. Pasta de trabalho

Use a pasta aberta no app. Se não houver, peça para o aluno criar `Documentos/Clientes` e abrir essa pasta no app (no Claude, na aba Code; no Codex, como projeto). É nela que ficam o `prospector-config.json` e os sites dos clientes.

## 3. Conta no painel

Pergunte se o aluno já tem conta no painel. Se não tiver, mande este link e espere ele voltar:
https://prospeccao-clientes-sites.pages.dev/?criar
Ele cria a conta lá, no navegador, **com o mesmo e-mail da compra do Método P5P** (o acesso é liberado por esse e-mail). Se esquecer a senha, o painel tem "Esqueci minha senha".

## 4. Login

Peça o e-mail e a senha da conta do painel e rode (Windows com `python`, Mac com `python3`):
```
python <skills>/supabase-sync/references/supabase_client.py login <pasta de trabalho>/prospector-config.json "email" "senha"
```
Só um token renovável fica salvo; a senha não fica em lugar nenhum. Não repita a senha na conversa.
- Erro de senha: confira se o e-mail e a senha são os do painel.
- Aviso de acesso não liberado: o e-mail não é o da compra do Método P5P. Oriente a criar a conta no painel com o e-mail da compra ou falar com o suporte na área de membros, e pare aqui.

## 5. Perfil

Rode `get-perfil` (skill `supabase-sync`). Mostre um resumo (sem o token do GitHub) e preencha só o que faltar, uma pergunta por vez:
- nome completo, como se apresenta (ex.: "Faço sites para clínicas") e WhatsApp: vão na assinatura da proposta;
- nichos que quer procurar (sugira nutricionistas, psicólogos, advogados e dentistas; o aluno escolhe);
- cidade padrão;
- clientes por busca (padrão 10);
- modo de envio da proposta: rascunho para revisar (recomendado) ou enviar direto.

Salve com `set-perfil`. Diga que tudo isso também pode ser mudado no painel, em Configurações.

## 6. GitHub (onde as páginas ficam no ar, de graça)

Se `get-perfil` já mostra usuário e token do GitHub, pule para o passo 7. Senão:
1. Se o aluno não tem conta: https://github.com/signup (gratuita).
2. Gerar o token: https://github.com/settings/tokens > Generate new token > **Tokens (classic)** > nome "prospecta" > marcar só **repo** > gerar > copiar.
3. **O token não vai no chat.** O aluno abre o painel, Configurações > GitHub, preenche o usuário, cola o token e clica em Salvar conexão.
4. Rode `get-perfil` de novo para confirmar que o token está salvo (sem mostrar o token).

## 7. Teste da publicação

Publique uma página simples ("Funcionou!") no repositório `prospector-teste`, seguindo a skill `deploy-github-pages`, e mostre o link ao aluno. Se falhar, leia o erro e resolva antes de seguir (token vencido, sem a opção repo, usuário errado).

## 8. Gmail

Explique em 2 linhas: a proposta sai pelo Gmail do próprio aluno.
- Se o app tiver o Gmail conectado, os rascunhos são criados sozinhos (Claude: em Configurações, Conectores, ligar o Gmail; Codex: na aba Plugins, adicionar o Gmail).
- Se não quiser conectar, tudo bem: o Prospecta entrega um link "Abrir no Gmail" já preenchido, e ele só clica em Enviar.

## Skill de páginas

Confira se a skill de páginas do curso está instalada (pasta `impeccable` em `~/.claude/skills` no Claude ou `~/.agents/skills` no Codex). Se estiver, diga que o `redesenhar` vai usar ela. Se não estiver, diga em uma linha que é opcional e que a Aula 1.3 do Método P5P instala: com ela as páginas dos clientes saem ainda melhores.

## 9. Manual

Copie `manual.html` (está nesta pasta da skill `setup`) para a pasta de trabalho e mostre ao aluno: "Esse é o seu manual, ele responde a maioria das dúvidas."

## 10. Encerrar

Confirme o que ficou pronto e explique o caminho de cada cliente, no formato do app (Claude com `/`, Codex com `$`):
prospectar > redesenhar > publicar > proposta > respostas e followup > contrato. O `editor` serve para ajustar uma página à mão.
Diga que, sempre que não souber o que fazer, é só rodar `proximo`, e que o painel (https://prospeccao-clientes-sites.pages.dev, aba Linha de produção) mostra o próximo passo de cada cliente com o comando pronto para copiar.
Sugira começar agora com `prospectar`.
