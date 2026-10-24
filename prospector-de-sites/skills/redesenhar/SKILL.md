---
name: redesenhar
description: P5P Prospecta, etapa Refeito. Refaz os sites dos clientes achados (lote de 5 ou mais) com estética premium, usando o conteúdo, o logo e as fotos reais de cada um, com a skill de páginas do curso (impeccable) quando estiver instalada, e gera o editor e o comparador antes e depois. Use quando o aluno rodar /redesenhar ou $redesenhar (pode vir com nomes de clientes e com "caprichado").
---

# Redesenhar (refazer os sites)

Antes de tudo, leia `../prospecta-guia/SKILL.md` e a skill `redesign-premium` (`../redesign-premium/SKILL.md`). Ela é obrigatória: leia ANTES de escrever qualquer HTML.

## Escolher os clientes

1. Rode `get-perfil` e `list-leads novo` (skill `supabase-sync`).
2. Se o aluno escreveu nomes junto com o comando, use esses. Senão, pegue os clientes com status `novo` mais bem avaliados: **mínimo de 5 por lote** (se houver menos, use todos e avise que rodar `prospectar` de novo aumenta o lote).
3. Confirme a lista com o aluno antes de começar. Diga em uma linha qual modo vai usar (rápido ou caprichado, abaixo).

## Skill de páginas do curso (impeccable)

O aluno instala a skill de páginas na Aula 1.3 do Método P5P. Confira se ela existe: uma pasta `impeccable` com `SKILL.md` ao lado das skills do Prospecta (`../impeccable/`), ou em `~/.claude/skills/impeccable` (Claude) ou `~/.agents/skills/impeccable` (Codex).
- O verificador dela é o programa `scripts/impeccable` dentro dessa pasta (no Windows, `scripts/impeccable.cmd`).
- Se ela NÃO estiver instalada, siga só a skill `redesign-premium`, como sempre, e diga ao aluno em uma linha que a Aula 1.3 deixa as páginas ainda melhores.

### Modo rápido (padrão, para o lote todo)

Sem perguntas ao aluno. Para cada cliente:
1. Antes de escrever o HTML, leia `reference/craft-floor.md` da skill de páginas (as regras de qualidade e o que é proibido) e siga junto com a `redesign-premium`.
2. Depois de salvar a página, rode o verificador nela:
   ```
   <pasta da impeccable>/scripts/impeccable detect --json <pasta de trabalho>/sites/[slug]/[slug].html
   ```
   (Windows: `<pasta da impeccable>\scripts\impeccable.cmd detect --json ...`). Corrija o que ele apontar e rode de novo uma vez.
3. **A identidade do cliente vence**: se o verificador reclamar de algo que é do próprio cliente (cor, logo, foto, texto real), mantenha e siga. O que nunca muda: nada inventado, logo e fotos reais, botões para o contato real.
4. Não crie `PRODUCT.md`, `DESIGN.md` nem `.impeccable/` no modo rápido.

### Modo caprichado (só quando o aluno pedir)

Quando o aluno escrever "caprichado" junto com um cliente (ex.: `/redesenhar Clínica Vida caprichado` ou `$redesenhar Clínica Vida caprichado`), faça SÓ esse cliente neste modo, um por vez:
1. Junte primeiro o conteúdo real (passo 1 de "Para cada cliente").
2. Use a skill de páginas no processo completo dela (no Claude, a skill `impeccable`; no Codex, `$impeccable`), com a pasta `sites/[slug]/` como projeto (os arquivos dela, como `PRODUCT.md` e `DESIGN.md`, ficam ali dentro). Passe como pedido fixo: é a página de vendas desse negócio local; tudo vem do conteúdo coletado; logo, fotos e cores do cliente são obrigatórios e mandam na identidade; nada inventado (serviço, número, depoimento, preço); botões para o WhatsApp real; um arquivo único `sites/[slug]/[slug].html`, responsivo.
3. O aluno responde às perguntas dela. Avise antes que esse modo demora mais e usa mais do plano dele.
4. Depois, continue normalmente com o editor, o comparador e o painel (passos 3 a 5 abaixo).

## Para cada cliente

1. **Conteúdo real**: abra o site original no navegador do próprio app (Claude: navegador embutido; Codex: `@Browser`). Leia todo o conteúdo: textos, serviços, formação, endereço, telefone, WhatsApp, e-mail, redes, horários e cores. Pegue os endereços reais do logo e das fotos (rode JavaScript na página para coletar `img.currentSrc` de todas as imagens; role até o fim antes, por causa das imagens que carregam depois). Tire um print do site original para referência.
2. **Página nova**: aplique a skill `redesign-premium` inteira, junto com a skill de páginas no modo escolhido. Nada inventado. Logo e fotos originais OBRIGATÓRIOS (se o cliente não tem logo, use o nome em tipografia, nunca invente logo).
3. **Salvar** na pasta de trabalho:
   - `sites/[slug]/[slug].html`: a página final (arquivo único, responsivo);
   - `sites/[slug]/[slug]-editor.html`: a mesma página com a camada de edição (script em `../redesign-premium/references/editor-visual.md`). Gere sempre.
4. **Comparador (obrigatório)**: crie ou atualize `comparar.html` na raiz da pasta de trabalho a partir de `../redesign-premium/references/comparador-template.html` (troque `__CLIENTES__` pelo array JSON, formato no rodapé do modelo). Se já existir, leia o array e acrescente os novos no topo, sem perder os antigos.
5. **Painel**: `upsert-lead` com `status: "redesenhado"`.

## Conferência antes de entregar (obrigatória)

- Existem, para CADA cliente do lote, `[slug].html` e `[slug]-editor.html`, e o `comparar.html` tem todos. Se faltar algum, gere agora.
- Abra cada página no navegador do app, no tamanho de computador e de celular, e procure texto de exemplo esquecido, link quebrado, seção vazia, rolagem para o lado e contraste ruim. Todos os botões levam ao WhatsApp ou contato REAL do cliente.
- Com a skill de páginas instalada: o verificador rodou em cada página.

## Entrega (nesta ordem)

1. Mostre o `comparar.html` primeiro (abra no navegador do app ou apresente o arquivo), depois a página e o editor de cada cliente.
2. Uma linha por cliente dizendo o que melhorou.
3. A frase "Painel atualizado: N clientes refeitos".
4. Como usar: `comparar.html` mostra o antes e depois; `[slug]-editor.html` serve para trocar textos e fotos; para um cliente especial, dá para pedir o modo caprichado; próximo passo, no formato do app: `publicar`.
