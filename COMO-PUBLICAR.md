# Como publicar tudo — guia só pra você (professor)

Isso não vai pro aluno. É o passo a passo de infraestrutura, uma vez só.

## 1. Banco de dados (Supabase) — feito ✓

Você já criou o projeto e rodou (ou vai rodar) `sql/schema.sql` no SQL Editor do Supabase. Se ainda não rodou: Supabase → SQL Editor → New query → cole o conteúdo de `sql/schema.sql` → Run.

## 2. Painel web (`painel-web/index.html`)

É um arquivo único, sem build, sem instalação — já tem a URL e a chave do seu Supabase embutidas. Três formas de colocar no ar, escolha uma:

- **Cloudflare Pages**: cloudflare.com → Pages → Upload assets → arraste a pasta `painel-web`. Pronto, ganha um link tipo `prospector-fabrica-digital.pages.dev`.
- **GitHub Pages**: suba a pasta `painel-web` num repositório seu (pode ser o mesmo do plugin, numa branch/pasta separada) e ative o Pages nas configurações do repositório.
- **Vercel/Netlify**: mesma lógica — arrastar e soltar a pasta funciona em qualquer um dos três.

Depois de publicado, esse é o link que você manda pro aluno usar no navegador (e é o mesmo e-mail/senha que ele cria lá que vai usar no `/setup` do Claude Code).

## 3. Plugin (pasta `prospector-de-sites/`)

Hoje mora em `P5P-Prospecta/prospeccao_clientes_sites`, **público** (pra qualquer aluno instalar sozinho, sem você precisar adicionar cada um como colaborador). O aluno instala com:

```
/plugin marketplace add P5P-Prospecta/prospeccao_clientes_sites
/plugin install prospector-de-sites@p5p-prospecta
```

(o nome depois do `@` é o que está em `.claude-plugin/marketplace.json`, campo `name` — `p5p-prospecta`, alinhado com o repo `P5P-Prospecta`.)

## 4. Testando a volta toda

1. Crie uma conta de teste no painel web.
2. No Claude Code, instale o plugin e rode `/setup` com esse e-mail/senha.
3. Rode `/prospectar` com um nicho qualquer.
4. Abra o painel web de novo (ou dê refresh) — os leads devem aparecer na tabela.

Se aparecerem, a integração está funcionando ponta a ponta.
