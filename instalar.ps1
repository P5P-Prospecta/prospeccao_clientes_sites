# P5P Prospecta: instalador para Windows (Claude e Codex).
# Uso (cole no PowerShell ou peca para o app rodar):
#   irm https://raw.githubusercontent.com/P5P-Prospecta/prospeccao_clientes_sites/main/instalar.ps1 | iex
# Rodar de novo atualiza para a versao mais nova.
# Este arquivo fica sem acentos de proposito: o PowerShell antigo do Windows le melhor assim.

& {
    $ErrorActionPreference = 'Stop'
    try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 } catch {}

    $repoZip = 'https://github.com/P5P-Prospecta/prospeccao_clientes_sites/archive/refs/heads/main.zip'
    if ($env:PROSPECTA_ZIP) { $repoZip = $env:PROSPECTA_ZIP }

    # Pastas de skills: Claude (~/.claude/skills) e Codex (~/.agents/skills)
    $destinos = @((Join-Path $HOME '.claude\skills'), (Join-Path $HOME '.agents\skills'))
    if ($env:PROSPECTA_DESTINOS) { $destinos = $env:PROSPECTA_DESTINOS.Split(';') | Where-Object { $_ } }

    $tmp = Join-Path ([IO.Path]::GetTempPath()) ('prospecta-' + [Guid]::NewGuid().ToString('N'))
    New-Item -ItemType Directory -Force -Path $tmp | Out-Null
    try {
        Write-Host ''
        Write-Host 'P5P Prospecta: baixando a versao mais nova...'
        $zip = Join-Path $tmp 'prospecta.zip'
        if (Test-Path $repoZip) { Copy-Item $repoZip $zip } else { Invoke-WebRequest -Uri $repoZip -OutFile $zip -UseBasicParsing }
        Expand-Archive -Path $zip -DestinationPath $tmp -Force

        $origem = Get-ChildItem -Path $tmp -Directory -Recurse -Filter 'skills' |
            Where-Object { Test-Path (Join-Path $_.FullName 'prospecta-guia\SKILL.md') } | Select-Object -First 1
        if (-not $origem) { throw 'Nao achei as skills do Prospecta dentro do arquivo baixado.' }

        $versao = ''
        $manifesto = Join-Path $origem.Parent.FullName '.claude-plugin\plugin.json'
        if (Test-Path $manifesto) { $versao = ((Get-Content $manifesto -Raw -Encoding UTF8) | ConvertFrom-Json).version }

        $skills = Get-ChildItem -Path $origem.FullName -Directory
        foreach ($destino in $destinos) {
            New-Item -ItemType Directory -Force -Path $destino | Out-Null
            foreach ($s in $skills) {
                $alvo = Join-Path $destino $s.Name
                if (Test-Path $alvo) { Remove-Item -Recurse -Force $alvo }
                Copy-Item -Recurse -Path $s.FullName -Destination $alvo
                Get-ChildItem -Path $alvo -Recurse -Directory -Filter '__pycache__' | Remove-Item -Recurse -Force
            }
            Write-Host ('  ok: ' + $skills.Count + ' skills em ' + $destino)
        }

        # Python: os scripts do Prospecta precisam dele
        Write-Host 'Conferindo o Python...'
        $py = $null
        foreach ($c in @('python', 'py')) {
            try {
                $v = (& $c --version) 2>&1 | Out-String
                if ($v -match 'Python 3') { $py = $v.Trim(); break }
            } catch {}
        }
        if ($py) {
            Write-Host ('  ok: ' + $py)
        } elseif (Get-Command winget -ErrorAction SilentlyContinue) {
            Write-Host '  Falta o Python. Instalando pelo winget (leva 1 ou 2 minutos)...'
            winget install -e --id Python.Python.3.12 --silent --accept-package-agreements --accept-source-agreements
        } else {
            Write-Host '  Falta o Python. Baixe em https://www.python.org/downloads/ e marque "Add python.exe to PATH".'
        }

        # Aviso: Prospecta antigo instalado como plugin do Claude
        $plugins = Join-Path $HOME '.claude\plugins\installed_plugins.json'
        if ((Test-Path $plugins) -and ((Get-Content $plugins -Raw) -match 'prospector-de-sites@')) {
            Write-Host ''
            Write-Host 'Aviso: o Claude ainda tem o Prospecta antigo instalado como plugin. Para tirar, digite no Claude:'
            Write-Host '  /plugin uninstall prospector-de-sites@p5p-prospecta'
        }

        Write-Host ''
        Write-Host ('Pronto! P5P Prospecta ' + $versao + ' instalado no Claude e no Codex.')
        Write-Host 'Agora feche e abra o app e rode:'
        Write-Host '  no Claude: /setup'
        Write-Host '  no Codex:  $setup'
        Write-Host ''
    } finally {
        Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue
    }
}
