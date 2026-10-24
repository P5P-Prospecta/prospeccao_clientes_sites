---
name: P5P Prospecta
description: Painel web do P5P Prospecta (Método P5P, Fábrica Digital). Superfície de trabalho do sistema "A Linha de Produção", registrada a partir do build em painel-web/index.html.
colors:
  ink: "#0A0A0A"
  ink-2: "#111111"
  ink-3: "#151515"
  ink-4: "#1C1C1C"
  line: "#2A2A2A"
  line-2: "#3A3A3A"
  fg: "#F5F5F5"
  soft: "#B8B8B8"
  note: "#8A8A8A"
  lime: "#CCFF00"
  lime-hover: "#DBFF4D"
  amber: "#FFB547"
  danger: "#FF6A5C"
typography:
  display:
    fontFamily: "'Chakra Petch', system-ui, sans-serif"
    fontSize: "clamp(30px, 6vw, 60px)"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "'Chakra Petch', system-ui, sans-serif"
    fontSize: "28px"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "0.01em"
  title:
    fontFamily: "'Chakra Petch', system-ui, sans-serif"
    fontSize: "18px"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "0.02em"
  station:
    fontFamily: "'Chakra Petch', system-ui, sans-serif"
    fontSize: "12px"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "0.05em"
  brand:
    fontFamily: "'Chakra Petch', system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0.06em"
  body:
    fontFamily: "'Sora', system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.55
  client-name:
    fontFamily: "'Sora', system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 600
    lineHeight: 1.35
  label:
    fontFamily: "'Sora', system-ui, sans-serif"
    fontSize: "13px"
    fontWeight: 500
    lineHeight: 1.3
  button:
    fontFamily: "'Sora', system-ui, sans-serif"
    fontSize: "14px"
    fontWeight: 600
    lineHeight: 1
  command:
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontSize: "13px"
    fontWeight: 500
    lineHeight: 1.4
  figure:
    fontFamily: "'JetBrains Mono', ui-monospace, monospace"
    fontSize: "22px"
    fontWeight: 600
    lineHeight: 1.2
    fontFeature: "'tnum'"
rounded:
  xs: "3px"
  sm: "5px"
  md: "6px"
  lg: "8px"
  xl: "10px"
spacing:
  bar: "60px"
  bar-sm: "56px"
  tabs: "48px"
  gutter: "24px"
  gutter-sm: "16px"
  page-max: "1440px"
  film: "62px"
  drawer: "560px"
components:
  button-primary:
    backgroundColor: "{colors.lime}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.lg}"
    padding: "0 16px"
    height: "40px"
  button-primary-hover:
    backgroundColor: "{colors.lime-hover}"
  button-default:
    backgroundColor: "{colors.ink-3}"
    textColor: "{colors.fg}"
    typography: "{typography.button}"
    rounded: "{rounded.lg}"
    padding: "0 16px"
    height: "40px"
  button-default-hover:
    backgroundColor: "{colors.ink-4}"
  button-ghost:
    textColor: "{colors.soft}"
    rounded: "{rounded.lg}"
    padding: "0 16px"
    height: "40px"
  button-ghost-hover:
    backgroundColor: "{colors.ink-3}"
    textColor: "{colors.fg}"
  button-danger:
    textColor: "{colors.danger}"
    rounded: "{rounded.lg}"
    padding: "0 16px"
    height: "40px"
  button-sm:
    rounded: "{rounded.md}"
    padding: "0 12px"
    height: "32px"
  button-copy-done:
    backgroundColor: "{colors.lime}"
    textColor: "{colors.ink}"
  command:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.fg}"
    typography: "{typography.command}"
    rounded: "{rounded.md}"
    padding: "5px 10px"
  input:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.fg}"
    rounded: "{rounded.lg}"
    padding: "0 12px"
    height: "42px"
  segmented:
    backgroundColor: "{colors.ink-2}"
    rounded: "{rounded.lg}"
    padding: "3px"
  segmented-option:
    textColor: "{colors.soft}"
    rounded: "{rounded.md}"
    padding: "0 12px"
    height: "32px"
  segmented-option-selected:
    backgroundColor: "{colors.line}"
    textColor: "{colors.fg}"
  panel:
    backgroundColor: "{colors.ink-2}"
    textColor: "{colors.fg}"
    rounded: "{rounded.xl}"
  film:
    backgroundColor: "{colors.lime}"
    textColor: "{colors.ink}"
    typography: "{typography.station}"
    height: "{spacing.film}"
  station-cell:
    backgroundColor: "{colors.ink-2}"
    rounded: "{rounded.sm}"
    size: "20px"
  station-cell-done:
    backgroundColor: "{colors.lime}"
  station-cell-current:
    backgroundColor: "{colors.ink}"
  stalled-tag:
    textColor: "{colors.amber}"
    rounded: "{rounded.sm}"
    padding: "0 8px"
    height: "24px"
  tab-count:
    backgroundColor: "{colors.ink-4}"
    textColor: "{colors.soft}"
    rounded: "{rounded.xs}"
    padding: "3px 6px"
  toast:
    backgroundColor: "{colors.ink-4}"
    textColor: "{colors.fg}"
    rounded: "{rounded.lg}"
    padding: "12px 16px"
  drawer:
    backgroundColor: "{colors.ink-2}"
    textColor: "{colors.fg}"
    width: "{spacing.drawer}"
---

# Design System: P5P Prospecta

> Escopo: este documento registra o painel como ele foi entregue em `painel-web/index.html` (HTML único, CSS e JS no próprio arquivo, tokens no `:root`). Ele **estende** o sistema "A Linha de Produção" da Fábrica Digital (DESIGN.md das páginas de venda em `LP SERVIÇOS/Nova pasta/PAGINA NOVA DO CURSO FABRICA DIGITAL  - AULA/DESIGN.md` e DESIGN.md da Fábrica de Copy em `sistema gerador de prompt para pagina de vendas/DESIGN.md`), que continuam sendo a fonte da identidade: paleta, famílias tipográficas, a película verde com furos como assinatura e o vocabulário plano. O que é próprio do painel está marcado como "específico do painel": a matriz clientes x estações, o âmbar de "parado", o comando para copiar, o recado com Desfazer, o funil de colunas e o antes e depois.

## Overview

**Creative North Star: "A Esteira do Aluno"**

Cada cliente é uma linha que atravessa as sete estações (Achado, Refeito, No ar, Proposta, Respondeu, Fechado, Pago). No alto da matriz corre a película verde da marca, com furos pretos em cima e embaixo e o nome das estações em Chakra Petch caixa alta; embaixo dela, uma linha por cliente, com casas quadradas ligadas por um trilho: as estações feitas em verde chapado, a atual com aro duplo, as que faltam em filete. Logo abaixo de cada linha fica o próximo passo numa frase e o comando pronto, em mono, com o botão Copiar. O painel não roda nada: entrega o comando.

Fora da película, o painel é preto de fábrica e denso como uma ferramenta: painéis um degrau acima do chão, filetes de 1px, interface em Sora 14px, títulos em Chakra Petch caixa alta. O verde-limão só aparece como campo inteiro (película, estação feita, botão principal, aba ativa, comando copiado, casa do "Pago"). O âmbar é exclusivo de "parado" e o vermelho é exclusivo de erro e de descartar. Nada brilha, nada tem degradê, nada flutua: não há nenhuma sombra com desfoque.

O painel não usa nenhuma imagem raster. A arte antiga `painel-web/img/login-hero.png` continua no repositório, mas não é mais referenciada pelo build; a tela de entrar é a própria película. Ícones são SVG de traço inline.

**Key Characteristics:**
- A película é estado, não enfeite: diz em que estação cada cliente está e, enquanto o painel busca dados, os furos correm.
- Três cores com papel único: verde para feito e ação principal, âmbar para parado, vermelho para erro e descarte.
- Plano total: profundidade por degrau de cinza e por anéis chapados, nunca por sombra com desfoque.
- Todo cliente tem o próximo passo escrito e, quando existe, o comando pronto para copiar.
- Mono só no que se conta, mede ou é comando; frases e rótulos em Sora.
- Mover de estação grava na hora e o recado oferece "Desfazer".

## Colors

A paleta da marca com uma escada de quatro pretos para dar camadas à tela de trabalho, mais dois sinais de cor com papel único: âmbar e vermelho.

### Primary
- **Verde-Limão de Esteira** (`lime`): película das estações, cabeçalho das colunas do Funil, metade verde da tela de entrar, casa de estação feita e o trilho até a atual, aro da estação atual, botão principal, filete de 3px da aba ativa, botão Copiar depois de copiar, caixa marcada, item escolhido no Antes e depois, rótulo "Depois", estado "pago" e GitHub conectado, ponto do recado, foco visível, seleção de texto e cursor dos campos. Também sublinha links e o "Desfazer". O hover do botão clareia para `lime-hover`.

### Secondary
- **Âmbar de Parado** (`amber`): específico do painel. Só para "parado": o selo "parado há N dias" (contorno âmbar a 50%), a contagem de parados no resumo e na aba (fundo âmbar a 12%), o aro e o trilho da estação atual de um cliente parado.

### Tertiary
- **Vermelho de Parada** (`danger`): só para erro e descartar. Botão Descartar, aviso de erro (contorno a 45%), mensagem de erro do formulário e o ponto do recado de erro.

### Neutral
- **Preto de Fábrica** (`ink`): chão, barra do topo, campos, comando, fichas do Funil, furos da película, letra sobre verde.
- **Painel** (`ink-2`): matriz, colunas do Funil, blocos de Configurações, tabela do Dinheiro, gaveta, segmentado.
- **Painel Ativo** (`ink-3`): botão padrão, hover de linha, coluna do Funil com ficha por cima, rodapé da tabela.
- **Painel Alto** (`ink-4`): hover do botão, contagem da aba, recado, item escolhido no Antes e depois.
- **Filete** (`line`) e **Filete Forte** (`line-2`): bordas de painel e divisões entre linhas; contorno de campos, botões, comando e casas que faltam. Hover de borda clareia para `#4A4A4A`.
- **Texto** (`fg`), **Texto de Apoio** (`soft`), **Nota** (`note`): corpo e nomes; frases do próximo passo e rótulos; nicho, cidade, e-mail, seta do passo, placeholder.

### Named Rules
**A Regra do Campo Inteiro.** Herdada da marca. O verde entra como superfície completa ou como contorno chapado, nunca como halo, brilho ou degradê, e nunca como letra sobre fundo claro.

**A Regra das Três Vozes.** Específica do painel. Verde é feito ou ação; âmbar é só "parado"; vermelho é só erro e descartar. Nenhuma das três cores empresta o papel da outra, e nenhum estado novo ganha uma quarta cor: se não é feito, parado ou erro, é cinza.

## Typography

**Display Font:** Chakra Petch (com system-ui, sans-serif), pesos 500, 600 e 700
**Body Font:** Sora (com system-ui, sans-serif), pesos 400, 500 e 600
**Label/Mono Font:** JetBrains Mono (com ui-monospace, monospace), pesos 400, 500 e 600

**Character:** Chakra Petch em caixa alta é placa de máquina (marca, títulos, estações); Sora faz todo o trabalho da interface; JetBrains Mono conta, mede e carrega o comando que vai para o Claude Code.

### Hierarchy
- **Display** (700, `clamp(30px, 6vw, 60px)`, 1, caixa alta, 15ch): só a frase da metade verde da tela de entrar.
- **Headline** (700, 28px; 24px no celular, 1.05, caixa alta): título de cada aba ("Linha de produção", "Funil"). Entrar usa 26px.
- **Title** (700, 18px a 22px, 1.1, caixa alta): título de bloco em Configurações e do "Como começar".
- **Station** (700, 12px a 13px, `letter-spacing: 0.05em`, caixa alta): nomes de estação na película, no cabeçalho do Funil, nos degraus da gaveta, na etapa do passo no celular, nos rótulos "Antes" e "Depois" e nos títulos de seção da gaveta (13px, `soft`).
- **Brand** (700, 15px, `letter-spacing: 0.06em`, caixa alta): "Prospecta" ao lado do selo P5P.
- **Body** (400, 14px, 1.55): toda a interface. Nome do cliente em Sora 600 de 15px; título da gaveta em Sora 600 de 20px.
- **Label** (500, 13px): rótulos de campo, cabeçalho da matriz e da tabela. Botões em Sora 600 de 14px (13px no pequeno).
- **Command** (500, 13px, 1.4): o comando para colar no Claude Code.
- **Figure** (600, 22px; 18px no celular, algarismos tabulares): totais do Dinheiro. Contagens, datas, valores, nota do Google e campos numéricos também em mono tabular.

### Named Rules
**A Regra do Mono que Conta.** Herdada da Fábrica de Copy. Mono só no que se conta ou se mede (ativos, parados, dias, valores, datas, nota) e no comando. Frases, rótulos, selos e títulos ficam em Sora ou Chakra Petch. O selo "parado há 6 dias" é Sora.

**A Regra da Placa de Estação.** Nome de estação é sempre Chakra Petch caixa alta, em qualquer lugar onde aparece.

**A Regra da Caixa Alta no CSS.** Herdada. Títulos escritos em sentence-case no código; a caixa alta vem do estilo.

## Layout

Página até 1440px, com margem de 24px (16px até 860px). Pilha fixa no topo: barra de 60px (56px no celular) com o selo e a marca à esquerda, e-mail, Atualizar e Sair à direita; abas de 48px logo abaixo. A barra e as abas grudam no topo, e o cabeçalho da matriz (película) gruda logo abaixo delas.

Cada aba abre com título e resumo à esquerda e as ferramentas (busca de 240px e segmentado) à direita, na mesma linha.

**Linha de produção:** matriz numa grade de `minmax(280px, 2.3fr)` para o cliente e sete colunas de `minmax(60px, 1fr)` para as estações; o próximo passo ocupa a largura toda embaixo de cada linha. Até 860px a película some, o nome vai para cima e as sete casas ocupam a largura toda como mini esteira; a etapa atual aparece escrita ao lado da seta do passo.

**Funil:** colunas de no mínimo 160px lado a lado, com rolagem lateral só dentro do Funil.

**Antes e depois:** lista de 280px fixa à esquerda e duas telas lado a lado; até 1100px a lista vira um seletor e, até 860px, as telas empilham.

**Dinheiro:** tabela com totais em mono separados por filete; até 860px cada linha vira um registro com o rótulo à esquerda e o valor à direita.

**Gaveta:** painel de 560px que entra pela direita (largura toda no celular), com topo, corpo rolável e pé com Salvar.

Pontos de quebra observados: 640px (rótulos curtos nas abas), 860px (celular), 1024px (divisão da tela de entrar), 1100px (Antes e depois e Configurações em uma coluna). Nenhuma tela rola para o lado.

## Elevation & Depth

Plano total. O painel não tem nenhuma sombra com desfoque. Profundidade vem da escada de pretos (`ink` a `ink-4`), de filetes de 1px e do fundo escurecido atrás da gaveta (preto a 60%, sem desfoque).

### Shadow Vocabulary
- **Anel de foco do campo** (`box-shadow: 0 0 0 1px var(--lime)`): soma 1px à borda verde do campo com foco.
- **Aro da estação atual** (`border: 2px solid var(--lime); outline: 1px solid var(--lime); outline-offset: 3px`): aro duplo chapado; âmbar quando o cliente está parado.

### Named Rules
**A Regra do Plano Total.** Herdada da Fábrica de Copy. Toda marca de destaque é anel ou contorno chapado, sem deslocamento e sem desfoque. Se um elemento novo pede sombra, ele pede um degrau de cinza ou um campo verde.

## Shapes

Cantos de ferramenta, pouco arredondados: 10px em painéis (matriz, colunas, blocos, tabela, telas); 8px em botões, campos, segmentado, aviso e recado; 6px em botão pequeno, comando, segmentos e selo da marca; 5px em casas de estação, selo de parado e caixas de marcar; 3px a 4px em contagens e rótulos de tela. Sem pílula.

A forma recorrente é o furo da película: retângulos pretos desenhados com padrão repetido de cor chapada (`repeating-linear-gradient`). Na película da matriz, furos de 10px a cada 24px numa faixa de 6px, a 6px da borda; no cabeçalho do Funil, 9px a cada 21px; na tela de entrar, 16px a cada 36px numa faixa de 10px, que fica vertical a partir de 1024px.

O trilho que liga as casas é um filete de 2px; vira verde até a estação atual.

## Components

### Matriz da linha de produção (componente-assinatura, específico do painel)
Painel de 10px com a película no cabeçalho: faixa verde de 62px, sete nomes de estação em Station preta, duas fileiras de furos. Cada cliente é uma linha separada por filete, com hover em painel ativo e clicável para abrir a gaveta.
- **Casa que falta:** quadrado de 20px, cantos de 5px, filete forte de 1.5px, fundo de painel.
- **Feita:** verde chapado, com trilho verde.
- **Atual:** fundo preto, borda verde de 2px e contorno verde de 1px a 3px de distância.
- **Parada:** a casa atual e o trilho até ela ficam em âmbar.
- **Fora (descartado):** a linha a 55% de opacidade.
- **Próximo passo:** seta em traço na cor de nota, selo de parado se houver, frase em `soft`, comando e Copiar (ou um botão de ação, como "Marcar assinado").
- **Busca:** enquanto o painel busca dados, os furos correm (800ms, linear, contínuo).

### Comando para copiar (específico do painel)
Caixa preta com filete forte, cantos de 6px, `padding: 5px 10px`, JetBrains Mono 500 de 13px, quebra em qualquer ponto. Ao lado, botão pequeno "Copiar" com ícone. Ao copiar, o botão vira verde chapado com visto e "Copiado" por 1,6s, a casa atual da linha pisca verde (900ms) e o recado diz "Comando copiado. Cole no Claude Code."

### Selo de parado (específico do painel)
24px (22px na ficha do Funil), cantos de 5px, contorno âmbar a 50%, letra âmbar em Sora 600 de 12px: "parado há N dias".

### Recado com Desfazer (específico do painel)
Barra flutuante embaixo, centralizada (largura toda no celular; deslocada para o lado da gaveta quando ela está aberta): painel alto, filete forte, cantos de 8px, Sora 500 de 14px, ponto de 10px verde (vermelho no erro). Entra subindo 16px em 200ms. Mover de estação grava na hora e o recado traz "Desfazer", sublinhado em verde, por 6 segundos; os outros recados somem em 2,6s.

### Buttons
- **Shape:** cantos de 8px, altura de 40px, `padding: 0 16px`, Sora 600 de 14px, ícone em traço de 16px.
- **Primary:** verde com letra preta (Entrar, Salvar); hover clareia para `lime-hover`. Na tela de entrar, 46px e largura toda.
- **Padrão:** painel ativo com filete forte; hover em painel alto e borda `#4A4A4A`.
- **Discreto:** transparente, letra de apoio; hover com fundo de painel ativo e filete (Atualizar, Sair).
- **Perigo:** transparente com letra vermelha; hover com vermelho a 8% e contorno a 35% (Descartar).
- **Pequeno:** 32px, `padding: 0 12px`, 13px, cantos de 6px.
- **Desligado:** painel ativo, filete, letra de nota.
- **Focus:** contorno verde de 2px a 2px de distância, em todo elemento focável.

### Controle segmentado
Filtro Ativos / Pagos / Descartados / Todos: caixa de painel com filete forte, cantos de 8px, 3px de padding. Opções de 32px, Sora 600 de 13px em texto de apoio; a escolhida fica em filete (`line`) com letra clara. Não é verde: filtro não é ação nem feito.

### Cards / Containers
- **Corner Style:** 10px.
- **Background:** painel (`ink-2`) sobre o chão preto.
- **Shadow Strategy:** nenhuma (ver Elevation & Depth).
- **Border:** 1px de filete.
- **Internal Padding:** 24px nos blocos (16px a 20px no celular), 14px a 16px nas linhas.

### Inputs / Fields
- **Style:** fundo preto, filete forte de 1px, cantos de 8px, altura de 42px, `padding: 0 12px`, Sora 14px; número em mono. Rótulo em Label acima, ajuda em 12px na cor de nota.
- **Hover:** borda `#4A4A4A`.
- **Focus:** borda verde com anel de 1px verde; cursor verde.
- **Caixa de marcar:** 22px, cantos de 5px; marcada em verde com visto preto.

### Funil (específico do painel)
Colunas de painel com cabeçalho de 52px em verde, com duas fileiras de furos, nome da estação em Station e contagem em mono. A coluna de descartados tem cabeçalho cinza (`line`). Fichas pretas de 8px com filete forte, nome em Sora 600 de 14px, valor em mono; arrastar deixa a ficha a 40% e acende a coluna de destino com borda verde.

### Antes e depois (específico do painel)
Duas telas de 10px com barra de 40px: rótulo em Station ("Depois" em verde chapado, "Antes" em painel alto) e endereço em mono de 12px na cor de nota. O site aparece num quadro 16:10 em escala; se não puder aparecer, mostra o aviso e o link para abrir em outra aba.

### Gaveta do cliente
Painel lateral de 560px, entra em 300ms com `cubic-bezier(.2,.8,.2,1)`. Seções separadas por filete, título de seção em Station 13px na cor de apoio. Linha do tempo vertical em degraus: casas de 18px ligadas por trilho de 2px, mesma lógica de feita, atual e falta da matriz.

### Navigation
Abas de texto em Sora 600 de 14px, cor de apoio; a ativa fica clara com filete verde de 3px embaixo (cantos de 3px em cima). Contagem ao lado em mono 11px sobre painel alto (âmbar a 12% para parados). No celular as abas rolam na horizontal, com rótulos curtos abaixo de 640px e a borda direita esmaecendo enquanto há mais abas.

### Tela de entrar (específica do painel)
Metade verde com a marca, a frase em Display e, a partir de 1024px, o texto de apoio e as estações em quadros pretos de 6px (nome em Station, comando em mono); "Pago" ocupa duas colunas como destino, só com contorno preto de 2px e sem fundo. Formulário de 400px à direita.

### Ícones
SVG próprio em traço de 1.75, grade de 24px, pontas e junções arredondadas, `currentColor`, 16px. Sem emoji, sem caractere usado como ícone e sem fonte de ícones.

## Do's and Don'ts

### Do:
- **Do** usar a película com furos para mostrar sequência e estado; os furos correm enquanto algo está sendo buscado.
- **Do** colocar só preto sobre o verde: furos, letra, contorno.
- **Do** reservar o âmbar para "parado" e o vermelho para erro e descartar.
- **Do** dar a todo cliente um próximo passo escrito e, quando existir, o comando em mono com Copiar.
- **Do** gravar a mudança de estação na hora e oferecer "Desfazer" no recado por 6 segundos.
- **Do** escrever nomes de estação em Chakra Petch caixa alta.
- **Do** pôr em JetBrains Mono tabular só números, datas, valores e comandos.
- **Do** manter cantos de 10px em painéis, 8px em botões e campos, 6px em comando e botão pequeno, 5px em casas e selos.
- **Do** separar linhas com filetes de 1px em vez de caixas.
- **Do** respeitar o movimento reduzido: furos, pisca e transições ficam parados.

### Don't:
- **Don't** usar sombra com desfoque, brilho ou halo; anéis chapados são o limite.
- **Don't** usar texto em degradê nem preenchimento em degradê. O padrão repetido dos furos e a máscara que esmaece a borda das abas no celular não são degradê decorativo.
- **Don't** usar verde como letra sobre fundo claro, nem verde apagado para estado desligado.
- **Don't** usar âmbar ou vermelho fora do papel de cada um.
- **Don't** usar roxo ou azul em lugar nenhum.
- **Don't** usar JetBrains Mono em frases, rótulos, selos ou títulos.
- **Don't** usar botão em formato de pílula.
- **Don't** colocar rótulo pequeno (eyebrow ou kicker) acima dos títulos.
- **Don't** usar emoji ou caractere como ícone.
- **Don't** usar travessão em texto visível.
- **Don't** usar imagem raster no painel; a arte `img/login-hero.png` ficou fora do build.
