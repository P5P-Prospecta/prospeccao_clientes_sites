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

## 5. Acesso só para quem comprou o Método P5P (Hotmart)

Desde a versão 3.1.0 o banco só abre os dados para quem tem acesso ativo na tabela `acessos`. Quem já tinha conta antes continua entrando (entra como `conta_existente`). Quem comprou o Método P5P é liberado pelo webhook da Hotmart, pelo e-mail da compra; reembolso e chargeback bloqueiam.

Uma vez só:

1. **Banco**: rode `sql/02-acesso-pela-compra.sql` no SQL Editor do projeto `jzlkqzamkgxxlbmpfisq` (ou pelo Supabase CLI com um token de acesso desse projeto). Pode rodar de novo sem estragar nada.
2. **Função**: publique o webhook, sem exigir login do Supabase:
   ```
   npx supabase functions deploy hotmart-webhook --project-ref jzlkqzamkgxxlbmpfisq --no-verify-jwt --use-api
   ```
3. **Secret**: em Edge Functions > Secrets, crie `HOTMART_HOTTOK` com o mesmo Hottok da Hotmart (o mesmo que já está no webhook da Fábrica de Copy). Opcional: `HOTMART_PRODUTOS` (padrão `8355172`, o Método P5P).
4. **Hotmart**: Ferramentas > Webhook > novo webhook com a URL `https://jzlkqzamkgxxlbmpfisq.supabase.co/functions/v1/hotmart-webhook`, produto MÉTODO P5P, eventos compra aprovada, compra completa, reembolso e chargeback, versão 2.0.0.
5. **Teste**: "Enviar teste" na Hotmart manda produto 0 e e-mail @example.com, então o resultado esperado é "outro produto" na tabela `hotmart_eventos` (prova que o Hottok bateu).

Para liberar alguém na mão (comprou com outro e-mail, cortesia):
```sql
insert into public.acessos (email, origem) values ('email@da.pessoa', 'manual')
on conflict (email) do update set status = 'ativo', atualizado_em = now();
```
Para bloquear: `update public.acessos set status = 'bloqueado' where email = 'email@da.pessoa';`
