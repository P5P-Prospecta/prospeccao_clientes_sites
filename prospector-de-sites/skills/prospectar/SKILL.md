---
name: prospectar
description: P5P Prospecta, etapa Achado. Busca no Google Maps, pelo navegador do próprio app, negócios bem avaliados com site ruim e e-mail público, e grava cada um no painel. Use quando o aluno rodar /prospectar ou $prospectar (pode vir com nicho e cidade), ou pedir para achar clientes.
---

# Prospectar (achar clientes no Google Maps)

Antes de tudo, leia `../prospecta-guia/SKILL.md`. Os critérios de qualidade estão na skill `prospeccao-maps` (`../prospeccao-maps/SKILL.md`): leia antes de abrir o navegador.

## Preparação

1. Rode `get-perfil` (skill `supabase-sync`) para ler nichos, cidade padrão e a meta de clientes por busca.
2. Nicho e cidade: use o que o aluno escreveu junto com o comando. Se não escreveu, pergunte qual dos nichos dele usar e confirme a cidade. Ele sempre pode trocar na hora.
3. Rode `list-leads` para saber quem já foi avaliado e não repetir.

## Busca (navegador do próprio app)

Abra o Google Maps no navegador do app (Claude: navegador embutido; Codex: `@Browser`), como manda o guia, e siga o fluxo da skill `prospeccao-maps`:
- buscar "[nicho] em [cidade]";
- **pular anúncios** (resultados marcados "Patrocinado"): eles não contam;
- critério ouro: nota 4,7 ou mais, 40 avaliações ou mais, site próprio no ar porém ruim, e e-mail público. Sem site, site bom ou sem e-mail: descarta e anota o motivo;
- abrir o site de cada candidato e avaliar pelos critérios da skill;
- coletar nome, nota, avaliações, telefone, WhatsApp no formato 55DDDnúmero, e-mail, endereço do site e o motivo objetivo de o site ser ruim.

**Limite fixo:** pare quando avaliar **25 estabelecimentos** OU quando bater a meta de clientes qualificados, o que vier primeiro. Não continue "só mais um pouco" e não troque de nicho sem perguntar ao aluno.

## Gravar (direto no painel)

Grave cada estabelecimento assim que avaliar (não deixe para o fim), com `upsert-lead` (skill `supabase-sync`):
- qualificado: `status: "novo"` e o motivo em `motivo`;
- descartado: `status: "descartado"` e o motivo em `obs`.

## Entrega

1. Uma tabela curta: qualificados (nome, nota, avaliações, motivo) e descartados (nome e motivo).
2. A frase "Painel atualizado: N clientes".
3. Próximo passo, no formato do app: `redesenhar` para os 5 ou mais melhores.
