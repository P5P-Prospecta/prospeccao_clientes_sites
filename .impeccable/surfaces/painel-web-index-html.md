---
version: 1
slug: "painel-web-index-html"
primary_target: "painel-web/index.html"
related_targets: []
---

# P5P Prospecta, painel web (painel-web/index.html)

Scope: o painel inteiro (entrar, Linha de produção, Funil, Clientes, Antes e depois, Dinheiro, Configurações e a gaveta de detalhes do cliente). Modo: Operate. Mundo visual herdado da Fábrica Digital ("A Linha de Produção", DESIGN.md das páginas de venda e da Fábrica de Copy).

Público e tarefa: alunos do Método P5P que vendem sites para negócios locais. Ao abrir o painel precisam saber o que fazer agora com cada cliente: qual comando colar no Claude Code, quem está parado, quem já pode pagar. Estados que importam: etapa de cada cliente (novo, redesenhado, publicado, proposta, respondeu, fechado, pago, descartado), dias parado na etapa, follow-up feito ou não, contrato pendente/enviado/assinado, pago, manutenção, acesso não liberado.

Restrições: HTML estático único com Supabase JS; não muda o banco nem os nomes dos campos (só lê e grava os mesmos); o painel não roda comandos, entrega o comando pronto. Proposta sem preço, nada inventado. Sem travessão no texto visível.

## Direction contract

THESIS: O painel é a esteira do aluno: cada cliente é uma linha que atravessa as sete estações (achado, refeito, no ar, proposta, respondeu, fechado, pago), a estação atual acesa e, logo embaixo, o próximo passo com o comando pronto para copiar. Recusa o CRM de cartões soltos em colunas como tela principal e as abas que só listam links.

OWN-WORLD: Preto #0A0A0A, painéis #111111 e #151515, filetes #2A2A2A e #3A3A3A, texto #F5F5F5 e #B8B8B8, notas #8A8A8A; verde-limão #CCFF00 como campo inteiro (estação concluída, botão principal, aba ativa, comando copiado); âmbar #FFB547 só para "parado"; vermelho #FF6A5C só para erro e descartado. Chakra Petch caixa alta em títulos, nomes de estação e marca; Sora na interface; JetBrains Mono em comandos, números e datas. Cantos de 6 a 10px, plano, sem brilho nem degradê, ícones de traço.

STORY: O aluno entra, vê quantos clientes ativos tem e quantos estão parados, lê de cima para baixo (parados primeiro, depois os mais perto de virar dinheiro), copia o comando do próximo passo e cola no Claude Code; quando o cliente responde, fecha e paga, marca no próprio painel. As outras abas servem a mesma linha: Funil para arrastar, Clientes para procurar, Antes e depois para mostrar a prova, Dinheiro para ver o que entrou e o que falta.

FIRST VIEWPORT: Linha de produção, 1440 x 900. Barra de 60px: marca "P5P PROSPECTA" à esquerda, e-mail e Sair à direita. Abas logo abaixo (Linha de produção ativa com filete verde). Título "Linha de produção" com dois números em mono: ativos e parados (âmbar). Busca e filtro Ativos/Todos/Descartados à direita. A matriz ocupa a largura: coluna do cliente (nome, nicho e cidade, nota) e sete casas de estação; casas concluídas em verde chapado, a atual com aro; embaixo de cada linha, o próximo passo em uma frase e o comando em mono com botão Copiar; selo âmbar "parado há N dias" quando passa do prazo da etapa.

FORM: Linha de produção em matriz (clientes x estações), posição 4 da lista ordenada; seed 40f42f33 (escolhido pelo usuário). Interação-assinatura: copiar o comando do próximo passo (a casa atual pisca verde e o botão vira "Copiado"), e clicar na linha abre a gaveta do cliente com a linha do tempo, o antes e depois e os campos de dinheiro. No celular a matriz vira uma mini esteira de sete casas por cliente, com o próximo passo embaixo.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

## Unresolved

- Autoria e licença da base do plugin (README credita Helio Arreche).
- Acesso pela compra do P5P: depende de acesso ao projeto Supabase do Prospecta.

## Adaptações registradas no build (24/10/2026)

- Aba "Clientes" fundida na Linha de produção: a busca (nome, nicho, cidade) e o filtro Ativos / Pagos / Descartados / Todos fazem o papel de procurar cliente. "Pagos" entrou no filtro porque Pago é a sétima estação e some dos ativos.
- Botão "Atualizar" no topo (busca de novo os clientes; o painel também busca sozinho quando a aba do navegador volta ao foco, depois de rodar um comando no Claude Code). Enquanto busca, os furos da película correm.
- Mover de estação (gaveta, funil, Marcar fechado/pago, Descartar) grava na hora e o recado traz "Desfazer" por 6 segundos.
- Acesso pela compra do Método P5P: tela "Acesso não liberado" quando tem_acesso() devolve falso. Se a checagem falhar (rede, ou a regra ainda não publicada), o painel deixa passar de propósito: quem protege os dados é o banco (RLS), e a tela é só o aviso.
- Antes e depois: site antigo em http não aparece dentro de página https (bloqueio do navegador); o quadro mostra o aviso e o link. Para site que recusa ser exibido em quadro, há sempre "Não apareceu? Abrir o site antigo em outra aba".
- Tela de entrar: o quadro PAGO ocupa duas colunas como destino (contorno, sem fundo).
