---
name: editor
description: P5P Prospecta, ajuste manual. Gera o editor visual de uma página já refeita, para o aluno trocar textos e fotos no navegador e exportar a página final. Use quando o aluno rodar /editor ou $editor (pode vir com o nome do cliente).
---

# Editor visual de uma página

Antes de tudo, leia `../prospecta-guia/SKILL.md`.

1. Cliente: use o nome que o aluno escreveu junto com o comando. Se não escreveu, liste as pastas em `sites/` e pergunte qual página editar.
2. Leia `sites/[slug]/[slug].html`.
3. Crie (ou refaça) `sites/[slug]/[slug]-editor.html`: uma cópia da página com a camada de edição antes de `</body>`. O script completo está em `../redesign-premium/references/editor-visual.md`: use exatamente como está.
4. Mostre o arquivo ao aluno (abra no navegador do app ou apresente o arquivo) e explique em 3 linhas:
   - abra o arquivo no navegador e clique em qualquer texto para editar;
   - clique em qualquer imagem para trocar por uma do computador;
   - o botão "Exportar página" baixa a página final limpa, sem o editor.
5. Quando o aluno disser que terminou e salvar o arquivo exportado, troque `sites/[slug]/[slug].html` pelo conteúdo exportado antes de publicar. Próximo passo, no formato do app: `publicar`.
