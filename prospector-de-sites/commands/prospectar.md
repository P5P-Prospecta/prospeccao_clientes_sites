---
description: Busca no Google Maps negócios bem avaliados com sites ruins e gera a lista de leads
argument-hint: "[nicho] [cidade] — opcional, usa os padrões do config"
---

Prospecte leads qualificados seguindo a skill `prospeccao-maps`.

## Preparação

1. Rode `get-perfil` (skill `supabase-sync`) para ler nichos/cidade padrão e a meta de leads por busca.
2. Determine nicho e cidade: use os argumentos `$ARGUMENTS` se informados; senão, pergunte ao usuário qual dos nichos padrão usar (e confirme a cidade). O usuário SEMPRE pode trocar nicho e cidade na hora — nunca trave nos padrões.
3. Rode `list-leads` (skill `supabase-sync`) para saber quais profissionais já foram avaliados — estes devem ser EXCLUÍDOS da nova busca.

## Execução

Use as ferramentas do Claude in Chrome (carregue via ToolSearch se necessário) para abrir o Google Maps e executar o fluxo completo descrito na skill `prospeccao-maps`.

**LIMITE RÍGIDO, NÃO NEGOCIÁVEL**: pare a avaliação de estabelecimentos assim que UMA das duas condições bater — **25 estabelecimentos avaliados** OU **a meta de leads qualificados atingida** (o que vier primeiro). 25 é um teto absoluto, não uma sugestão: ao chegar no 25º estabelecimento avaliado, PARE imediatamente e monte a entrega com o que tiver, mesmo que a meta de leads não tenha sido atingida. Não continue "só mais um pouco", não troque de sub-nicho pra tentar completar a meta sem antes voltar e perguntar ao usuário se ele quer continuar — trocar de nicho reinicia a contagem e é uma decisão que precisa de confirmação explícita, não uma escolha automática no meio da busca.

- Buscar "[nicho] em [cidade]"
- Critério ouro: nota alta (≥ 4.7) + muitas avaliações (≥ 40) + site ATIVO porém ruim + e-mail público. Os três eliminatórios: sem site (ou site fora do ar/diretório de terceiros) → pula; site bom → pula; sem e-mail → pula. Sempre registrar descartados com o motivo e seguir buscando até bater a meta ou o teto de 25
- Para cada candidato, abrir o site em nova aba e avaliar a qualidade seguindo os critérios da skill
- Coletar: nome, nota, nº de avaliações, telefone, **WhatsApp em formato 55DDDnúmero** (link wa.me no site ou celular do perfil do Maps — ver skill), e-mail, URL do site e o motivo objetivo pelo qual o site é ruim

## Saída — direto pro Supabase (sem planilha do Google)

O destino é só o Supabase — não use conector de Google Drive/Sheets, ele não está disponível no Claude Code e travaria essa etapa sem gerar erro claro.

1. **Supabase**: para cada lead avaliado (qualificado E descartado), rode `upsert-lead` (skill `supabase-sync`) assim que ele for avaliado — não espere acumular todos pra gravar no final; isso evita perder trabalho se o processo for interrompido no meio. Leads novos entram com `status: "novo"`, descartados com `status: "descartado"` e o motivo em `obs`.

A entrega final DEVE incluir a confirmação explícita "Dashboard atualizado: [N] leads" (após rodar `upsert-lead` pra todos os leads da rodada). Mostre a tabela ao usuário resumindo os leads qualificados e descartados (com motivo), e sugira o próximo passo: `/redesenhar` para os 5+ melhores leads. O painel web (login) já reflete os dados automaticamente — não precisa de nenhum passo extra do usuário pra ver o resultado.
