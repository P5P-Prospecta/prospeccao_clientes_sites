#!/usr/bin/env bash
# P5P Prospecta: instalador para Mac e Linux (Claude e Codex).
# Uso (cole no Terminal ou peça para o app rodar):
#   curl -fsSL https://raw.githubusercontent.com/P5P-Prospecta/prospeccao_clientes_sites/main/instalar.sh | bash
# Rodar de novo atualiza para a versão mais nova.
set -euo pipefail

ZIP_URL="${PROSPECTA_ZIP:-https://github.com/P5P-Prospecta/prospeccao_clientes_sites/archive/refs/heads/main.zip}"
DESTINOS="${PROSPECTA_DESTINOS:-$HOME/.claude/skills;$HOME/.agents/skills}"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo ""
echo "P5P Prospecta: baixando a versão mais nova..."
if [ -f "$ZIP_URL" ]; then cp "$ZIP_URL" "$TMP/prospecta.zip"; else curl -fsSL "$ZIP_URL" -o "$TMP/prospecta.zip"; fi
unzip -q "$TMP/prospecta.zip" -d "$TMP"

GUIA="$(find "$TMP" -path '*/skills/prospecta-guia/SKILL.md' | head -n 1)"
if [ -z "$GUIA" ]; then echo "Não achei as skills do Prospecta no arquivo baixado."; exit 1; fi
ORIGEM="$(dirname "$(dirname "$GUIA")")"
VERSAO="$(grep -o '"version": *"[^"]*"' "$(dirname "$ORIGEM")/.claude-plugin/plugin.json" 2>/dev/null | head -n 1 | sed 's/.*"\([^"]*\)"$/\1/' || true)"

IFS=';' read -r -a LISTA <<< "$DESTINOS"
for DEST in "${LISTA[@]}"; do
  [ -z "$DEST" ] && continue
  mkdir -p "$DEST"
  N=0
  for S in "$ORIGEM"/*/; do
    NOME="$(basename "$S")"
    rm -rf "$DEST/$NOME"
    cp -R "$S" "$DEST/$NOME"
    find "$DEST/$NOME" -type d -name '__pycache__' -prune -exec rm -rf {} +
    N=$((N + 1))
  done
  echo "  ok: $N skills em $DEST"
done

echo "Conferindo o Python..."
if command -v python3 >/dev/null 2>&1 && python3 --version 2>&1 | grep -q "Python 3"; then
  echo "  ok: $(python3 --version 2>&1)"
else
  echo "  Falta o Python 3. No Mac, instale em https://www.python.org/downloads/ (ou rode: xcode-select --install)."
fi

if [ -f "$HOME/.claude/plugins/installed_plugins.json" ] && grep -q 'prospector-de-sites@' "$HOME/.claude/plugins/installed_plugins.json"; then
  echo ""
  echo "Aviso: o Claude ainda tem o Prospecta antigo instalado como plugin. Para tirar, digite no Claude:"
  echo "  /plugin uninstall prospector-de-sites@p5p-prospecta"
fi

echo ""
echo "Pronto! P5P Prospecta $VERSAO instalado no Claude e no Codex."
echo "Agora feche e abra o app e rode:"
echo "  no Claude: /setup"
echo '  no Codex:  $setup'
echo ""
