# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Alunos do Método P5P (Fábrica Digital) que querem vender sites para negócios locais. Não são técnicos nem vendedores experientes. Usam o painel no computador para acompanhar os clientes e, às vezes, no celular para ver o que está pendente. O trabalho pesado (achar clientes, refazer sites, publicar, mandar proposta) é feito por comandos no Claude Code; o painel é onde eles enxergam o funil e decidem o próximo passo.

O autor, Diogo Antonio (@diogobuilder_oficial), também usa a própria conta para testar.

## Product Purpose

O P5P Prospecta é o sistema de prospecção do Método P5P: um plugin do Claude Code mais um painel web (CRM). O ciclo: achar no Google Maps negócios bem avaliados com site ruim e e-mail público, refazer a página com o conteúdo real do cliente, publicar de graça no GitHub Pages, mandar a proposta por e-mail com a página-capa, acompanhar respostas, fazer o follow-up, gerar o contrato e registrar o pagamento e a manutenção.

Sucesso: o aluno sabe, ao abrir o painel, o que fazer agora para transformar prospecção em cliente pagando, sem lembrar a ordem dos comandos.

## Positioning

"Da criação da página até encontrar quem precisa dela." A proposta mostra o antes e depois do site do próprio cliente, já publicado, em vez de um orçamento genérico. Roda na conta do Claude do próprio aluno: sem mensalidade.

## Operating Context

- Comandos no Claude Code: /setup, /prospectar, /redesenhar, /editor, /publicar, /proposta, /respostas, /followup, /contrato.
- Status do lead: novo, redesenhado, publicado, proposta, respondeu, fechado, descartado. Contrato: pendente, enviado, assinado. Campos de dinheiro: valor do site, manutenção mensal, pago.
- Banco Supabase compartilhado da turma, cada aluno vê só os próprios dados (RLS).
- Requisitos do aluno: Claude Code, extensão Claude in Chrome, conector do Gmail, conta gratuita no GitHub.

## Capabilities and Constraints

- Painel: HTML estático único (`painel-web/index.html`) com Supabase JS, publicado no Cloudflare Pages (prospeccao-clientes-sites.pages.dev). Sem build.
- O painel não roda os comandos: ele mostra o estado e entrega o comando certo para o aluno colar no Claude Code.
- Proposta nunca fala preço; follow-up educado, sem urgência; nada de dado inventado sobre o cliente.
- Em aberto (23/10/2026): autoria e licença da base do plugin (README e manual creditam Helio Arreche); se o acesso continua limitado aos 100 primeiros membros.

## Brand Commitments

- Nomes: "P5P Prospecta", "Método P5P", "Fábrica Digital". Faz parte da Fábrica Digital; identidade visual da marca (verde-limão `#CCFF00` sobre preto `#0A0A0A`, Chakra Petch, Sora, JetBrains Mono, "Linha de Produção"), já aplicada na Fábrica de Copy.
- Texto em português do Brasil simples; nunca travessão em texto visível; nunca inventar dados.

## Evidence on Hand

- A arte antiga `painel-web/img/login-hero.png` continua no repositório, mas o painel novo não usa (tinha números de enfeite que pareciam dados).
- Não há depoimentos, números de clientes fechados nem prints reais de alunos. Não fabricar.

## Product Principles

- Todo cliente tem um próximo passo visível, com o comando pronto.
- O que está parado aparece antes do que está andando.
- O antes e depois é a prova: mostrar, não só linkar.
- Dinheiro claro: o que entrou, o que falta receber, o que se repete todo mês.
