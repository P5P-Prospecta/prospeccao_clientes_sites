# 🎯 P5P Prospecta — Prospector de Sites v3.0.0

**Plugin para Claude Code que roda o ciclo completo de prospecção e venda de sites — com CRM incluso:**

**Achou → Refez → Publicou → Ofertou → Acompanhou → Fechou → Contrato.**

De graça, sem mensalidade — o único custo é a sua conta do Claude.

## O que o plugin faz

| Comando | O que acontece |
|---|---|
| `/setup` | Configura tudo uma vez (login, assinatura, nichos, GitHub) e entrega o manual + o painel |
| `/prospectar` | Varre o Google Maps: negócios nota ≥ 4.7 com site fraco E e-mail público → grava direto no Supabase |
| `/redesenhar` | Recria as páginas com estética premium (fotos/logo/conteúdo REAIS) + editor visual + comparador antes/depois |
| `/editor` | Edita texto e imagem da página no navegador, sem código |
| `/publicar` | Publica no GitHub Pages SOZINHO (direto pela API, sem instalar nada) + página-capa da proposta + HTTPS automático |
| `/proposta` | E-mail com rapport real, checklist anti-spam e a capa personalizada como link |
| `/respostas` | Lê seu Gmail e move o card sozinho quando o cliente responde (agende diário!) |
| `/followup` | 3+ dias sem resposta? Gera o lembrete gentil — 1 por lead, nunca repete |
| `/contrato` | Fechou? Folha A4 imprimível + Word TRAVADO (cliente só preenche onde você deixar) |

## 📊 CRM (painel web)

Kanban com drag & drop, funil, clientes, comparador, follow-ups, contratos e painel financeiro (recebido, a receber, MRR e projeção 12 meses) — tudo num painel web com login (Supabase): **[prospeccao-clientes-sites.pages.dev](https://prospeccao-clientes-sites.pages.dev)**. Sem instalar nada.

## Como instalar

**No Claude Code:**
```
/plugin marketplace add P5P-Prospecta/prospeccao_clientes_sites
/plugin install prospector-de-sites@arrecheneto-plugins
```
Depois rode `/setup` e siga o manual (link abaixo).

## 🔄 Já tem o plugin e não atualiza?

Re-adicionar o link NÃO atualiza (fica em cache). Faça:
```
/plugin marketplace update arrecheneto-plugins
```
e reinicie o app — a versão certa é a **3.0.0** (confira em Gerenciar plugins). Se não subir: desinstale o plugin → remova o marketplace → feche o app → adicione e instale de novo. A atualização é automática (autoUpdate ativado).

## Requisitos

Claude Code · extensão Claude in Chrome · conector do Gmail · conta gratuita no GitHub · Windows ou Mac.

## Manual

O `/setup` entrega o [manual completo do aluno](prospector-de-sites/manual.html) — passo a passo de tudo, escrito pra quem nunca usou nada parecido, incluindo o que fazer quando dá erro.

---

Feito por **Helio Arreche** · [YouTube](https://youtube.com/@helioarreche) · [Instagram @helioarreche](https://instagram.com/helioarreche) · Série completa do plugin no canal 🎬
