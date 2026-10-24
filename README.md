# P5P Prospecta: Prospector de Sites v3.2.0

**Roda no app do Claude e no app do Codex.** O ciclo completo de prospecção e venda de sites, com CRM incluso:

**Achou, refez, publicou, ofertou, acompanhou, fechou, contrato.**

Usa o navegador que já vem dentro do app (sem extensão no Chrome). Sem mensalidade: o único custo é a sua conta do Claude ou do ChatGPT.

## Como instalar (uma vez, vale para Claude e Codex)

Cole na conversa do app, ou direto no PowerShell / Terminal:

**Windows**
```
irm https://raw.githubusercontent.com/P5P-Prospecta/prospeccao_clientes_sites/main/instalar.ps1 | iex
```

**Mac**
```
curl -fsSL https://raw.githubusercontent.com/P5P-Prospecta/prospeccao_clientes_sites/main/instalar.sh | bash
```

O instalador copia as skills para `~/.claude/skills` (Claude) e `~/.agents/skills` (Codex) e confere o Python. Depois feche e abra o app e rode `/setup` (Claude) ou `$setup` (Codex). Para atualizar, rode o mesmo comando de novo.

## As etapas

| Claude | Codex | O que acontece |
|---|---|---|
| `/setup` | `$setup` | Configura uma vez: login do painel, perfil, GitHub (com teste de publicação), Gmail e o manual |
| `/prospectar` | `$prospectar` | Google Maps pelo navegador do app: nota 4,7 ou mais, site fraco e e-mail público; pula anúncios; grava direto no painel |
| `/redesenhar` | `$redesenhar` | Refaz as páginas com fotos, logo e conteúdo REAIS, mais editor visual e comparador antes e depois |
| `/editor` | `$editor` | Edita texto e imagem da página no navegador, sem código |
| `/publicar` | `$publicar` | Publica no GitHub Pages direto pela API, com a capa da proposta e cadeado automático |
| `/proposta` | `$proposta` | E-mail com elogio real, checklist contra spam e a capa como único link: rascunho no Gmail ou link "Abrir no Gmail" |
| `/respostas` | `$respostas` | Confere no Gmail quem respondeu e move o cliente no painel |
| `/followup` | `$followup` | 3 dias ou mais sem resposta: lembrete gentil, um por cliente |
| `/contrato` | `$contrato` | Fechou? Folha A4 para imprimir e Word travado |
| `/proximo` | `$proximo` | O que fazer agora com cada cliente (parados primeiro) e o comando certo |

## CRM (painel web)

Linha de produção (cada cliente nas 7 estações, com o próximo passo e o comando pronto para copiar no formato do seu app), funil com arrastar e soltar, antes e depois lado a lado e dinheiro (recebido, a receber e manutenção mensal), num painel web com login: **[prospeccao-clientes-sites.pages.dev](https://prospeccao-clientes-sites.pages.dev)**. Acesso liberado pelo e-mail da compra do Método P5P.

## Requisitos

App do Claude (aba Code) ou app do Codex · conta gratuita no GitHub · Gmail · Python (o instalador confere) · Windows ou Mac.

## Instalação antiga (plugin do Claude Code)

Quem usa o Claude Code no terminal ainda pode instalar como plugin: `/plugin marketplace add P5P-Prospecta/prospeccao_clientes_sites` e `/plugin install prospector-de-sites@p5p-prospecta`. Não use as duas formas juntas: se já tem o plugin, rode `/plugin uninstall prospector-de-sites@p5p-prospecta` antes do instalador.

## Manual

O setup entrega o [manual completo do aluno](prospector-de-sites/skills/setup/manual.html): passo a passo de tudo, escrito para quem nunca usou nada parecido, incluindo o que fazer quando dá erro.

---

Feito por **Helio Arreche** · [YouTube](https://youtube.com/@helioarreche) · [Instagram @helioarreche](https://instagram.com/helioarreche) · Série completa do plugin no canal 🎬
