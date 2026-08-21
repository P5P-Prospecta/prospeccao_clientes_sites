---
name: prospeccao-maps
description: Esta skill deve ser usada ao prospectar clientes no Google Maps — buscar negócios bem avaliados com sites ruins, qualificar leads, avaliar qualidade de sites de terceiros e montar a planilha de leads. Acione quando o usuário disser "prospectar", "buscar clientes", "achar leads", "clientes com site ruim" ou rodar /prospectar.
---

# Prospecção no Google Maps

Encontrar o cliente ouro: negócio que JÁ fatura bem (nota alta, muitas avaliações) mas perde clientes por causa de um site fraco. Não se cria demanda — conserta-se onde o dinheiro está escapando.

## Fluxo (via Claude in Chrome)

1. Abrir `https://www.google.com/maps` e buscar `[nicho] em [cidade]`.
2. Percorrer os resultados um a um, em ordem. Para cada estabelecimento:
   - Abrir o perfil e ler nota, nº de avaliações e link do site.
   - **Filtro 1 — potencial financeiro**: nota ≥ 4.7 E avaliações ≥ 40. Reprovou → próximo.
   - **Filtro 2 — TEM site**: o lead PRECISA ter um site ativo e acessível — a oferta é "uma versão muito melhor do SEU site", e o conteúdo/fotos vêm de lá. Sem site, site fora do ar ou "site" que é só diretório de terceiros/linktree → descartar (registrar o motivo) e seguir.
   - **Filtro 3 — site ruim**: abrir o site em nova aba e avaliar pelos critérios abaixo. Site bom → descartar. Site ativo porém ruim → candidato (falta só o e-mail).
3. **PARE ao atingir 25 estabelecimentos avaliados — teto rígido, não sugestão.** Também pare antes disso se bater a meta de leads qualificados (config, padrão 10), o que vier primeiro. Ao chegar no 25º estabelecimento avaliado, encerre a busca imediatamente e entregue o que tiver, mesmo que a meta de leads não tenha sido atingida — não amplie a busca, não troque de sub-nicho, não continue "só mais um pouco" sem antes voltar e perguntar ao usuário. Trocar de nicho no meio da busca reinicia a contagem e exige confirmação explícita do usuário primeiro.
4. Pular estabelecimentos que já estão no Supabase (rode `list-leads` no início e confira pelo nome/slug — avaliados em buscas anteriores).

## Critérios de site ruim (guardar o motivo específico)

Qualifica como lead se o site (ativo) tiver 2 ou mais destes problemas:

- Layout datado (aparência de template de 10+ anos, fontes de sistema, imagens esticadas/pixeladas)
- Sem CTA claro de agendamento/contato (nenhum botão de WhatsApp ou agenda visível na primeira dobra)
- Domínio gratuito ou hospedado em plataforma alheia (Google Sites, Wix grátis, subdomínio de terceiros com marca da plataforma)
- Não responsivo (quebra no mobile)
- Conteúdo desorganizado: serviços escondidos, sem hierarquia, texto corrido sem seções
- Sem prova social (nenhuma avaliação/depoimento, apesar da nota alta no Google)

O motivo anotado deve ser objetivo e verificável — ele será citado na proposta. Ex.: "domínio redireciona para Google Sites gratuito, template básico, sem CTA de agendamento".

## Coleta por lead

Nome, nota, nº de avaliações, telefone, WhatsApp, e-mail, URL do site, motivo.

**WHATSAPP: capture SEMPRE, separado do telefone.** Fontes, na ordem: botão/link de WhatsApp no site do lead (procure `wa.me/`, `api.whatsapp.com` ou ícone de WhatsApp — extraia o número do link); telefone celular do perfil do Maps (números com 9º dígito são celular no Brasil — assuma WhatsApp). Registre no formato internacional `55 + DDD + número` (ex.: `5511999990000`), pronto pra `wa.me`. O WhatsApp alimenta os botões do dashboard e o plano B de abordagem quando o e-mail não responde.

**E-MAIL É OBRIGATÓRIO.** A proposta vai por e-mail — lead sem e-mail público não fecha o ciclo. Procure nesta ordem: site (rodapé e página de contato), links `mailto:`, home do site da clínica onde atende, busca no Google por "[nome] + email/contato". Se NÃO encontrar e-mail: **descarte o lead, registre na lista de descartados (com o contato que existir, ex. WhatsApp/Instagram) e continue buscando o próximo** até bater a meta. Atenção: "site" que aponta para diretório de terceiros (localtreino, acheioprofissional etc.) não conta como site próprio — descarta pelo Filtro 2.

## Saída — direto pro Supabase

Não use conector de Google Drive/Sheets — ele não está disponível no Claude Code. Grave cada lead (qualificado e descartado) via `upsert-lead` (skill `supabase-sync`) assim que for avaliado, não só no final:

```
slug, nome, nota, avaliacoes, email, telefone, whatsapp, site_antigo, motivo, status
```

## Boas práticas

- Trabalhar por região dá vantagem: menos concorrência na oferta e conhecimento local.
- Enquanto o navegador trabalha, não interromper o fluxo com perguntas — só reportar a tabela final.
- Se o Google Maps pedir login/captcha, pausar e avisar o usuário.
