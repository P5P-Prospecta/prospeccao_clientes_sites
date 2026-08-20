#!/usr/bin/env python3
"""
Publica um cliente no GitHub Pages: cria/reaproveita o repositório,
sobe os arquivos indicados e ativa o Pages. Só usa a biblioteca padrão
do Python (urllib), então roda em qualquer máquina com Python 3
instalado, sem precisar instalar nada extra.

Uso:
    python3 publicar-github.py CAMINHO/prospector-config.json SLUG \
        "local/arquivo1.html:index.html" \
        "local/arquivo2.html:proposta.html" \
        ["local/CNAME:CNAME"]

O token e o usuário do GitHub vêm do bloco "github" do config:
    {
      "github": {
        "usuario": "seu-usuario-ou-org",
        "token": "ghp_xxx...",
        "privado": false
      }
    }
"""

import sys
import os
import json
import base64
import time
import urllib.request
import urllib.error

API = "https://api.github.com"


def carregar_config(caminho_config):
    with open(caminho_config, "r", encoding="utf-8") as f:
        config = json.load(f)
    gh = config.get("github") or {}
    usuario = gh.get("usuario", "").strip()
    token = gh.get("token", "").strip()
    privado = bool(gh.get("privado", False))
    if not usuario or not token:
        print("[ERRO] Preencha 'github.usuario' e 'github.token' em "
              "prospector-config.json antes de publicar. O token nunca "
              "deve ser digitado no chat — só editado direto no arquivo.")
        sys.exit(1)
    return usuario, token, privado


def chamada(metodo, path, token, body=None, aceitar_404=False):
    url = path if path.startswith("http") else API + path
    dados = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=dados, method=metodo)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    if dados is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            corpo = resp.read()
            return resp.status, (json.loads(corpo) if corpo else {})
    except urllib.error.HTTPError as e:
        corpo = e.read()
        if e.code == 404 and aceitar_404:
            return 404, {}
        detalhe = corpo.decode("utf-8", "ignore")
        print(f"[ERRO HTTP {e.code}] {metodo} {path} -> {detalhe}")
        raise


def garantir_repo(usuario, token, slug, privado):
    status, dados = chamada("GET", f"/repos/{usuario}/{slug}", token, aceitar_404=True)
    if status == 200:
        print(f"[ok] Repositório '{slug}' já existe, reaproveitando.")
        return dados["owner"]["login"]

    # tenta como usuário pessoal primeiro; se 'usuario' for uma org, o endpoint muda
    status, dados = chamada("GET", f"/orgs/{usuario}", token, aceitar_404=True)
    eh_organizacao = status == 200

    payload = {
        "name": slug,
        "private": privado,
        "auto_init": True,  # já cria o branch main com um commit inicial
        "description": f"Site publicado via Prospector de Sites — {slug}",
    }
    endpoint = f"/orgs/{usuario}/repos" if eh_organizacao else "/user/repos"
    status, dados = chamada("POST", endpoint, token, body=payload)
    print(f"[ok] Repositório '{slug}' criado.")
    return dados["owner"]["login"]


def subir_arquivo(usuario_repo, token, slug, caminho_local, caminho_remoto):
    with open(caminho_local, "rb") as f:
        conteudo_b64 = base64.b64encode(f.read()).decode("ascii")

    sha_atual = None
    status, dados = chamada(
        "GET", f"/repos/{usuario_repo}/{slug}/contents/{caminho_remoto}",
        token, aceitar_404=True,
    )
    if status == 200:
        sha_atual = dados.get("sha")

    payload = {
        "message": f"Publica {caminho_remoto} ({slug})",
        "content": conteudo_b64,
        "branch": "main",
    }
    if sha_atual:
        payload["sha"] = sha_atual

    chamada(
        "PUT", f"/repos/{usuario_repo}/{slug}/contents/{caminho_remoto}",
        token, body=payload,
    )
    print(f"[ok] Enviado: {caminho_remoto}")


def ativar_pages(usuario_repo, token, slug):
    status, _ = chamada("GET", f"/repos/{usuario_repo}/{slug}/pages", token, aceitar_404=True)
    if status == 200:
        print("[ok] GitHub Pages já estava ativo.")
        return
    payload = {"source": {"branch": "main", "path": "/"}}
    chamada("POST", f"/repos/{usuario_repo}/{slug}/pages", token, body=payload)
    print("[ok] GitHub Pages ativado.")


def testar_url(url, tentativas=6, espera=10):
    for i in range(tentativas):
        req = urllib.request.Request(url, method="HEAD")
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                if resp.status < 400:
                    return True
        except urllib.error.HTTPError as e:
            if e.code < 400:
                return True
        except Exception:
            pass
        if i < tentativas - 1:
            time.sleep(espera)
    return False


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)

    caminho_config = sys.argv[1]
    slug = sys.argv[2]
    pares_arquivo = sys.argv[3:]

    usuario, token, privado = carregar_config(caminho_config)
    usuario_repo = garantir_repo(usuario, token, slug, privado)

    tem_cname = False
    for par in pares_arquivo:
        if ":" not in par:
            print(f"[ERRO] Formato inválido (esperado local:remoto): {par}")
            sys.exit(1)
        local, remoto = par.split(":", 1)
        if not os.path.isfile(local):
            print(f"[ERRO] Arquivo local não encontrado: {local}")
            sys.exit(1)
        subir_arquivo(usuario_repo, token, slug, local, remoto)
        if remoto.strip().upper() == "CNAME":
            tem_cname = True

    ativar_pages(usuario_repo, token, slug)

    url_base = f"https://{usuario_repo}.github.io/{slug}/"
    print(f"\nAguardando o primeiro build do GitHub Pages...")
    ok = testar_url(url_base)
    if ok:
        print(f"[ok] Site no ar: {url_base}")
    else:
        print(f"[aviso] Ainda não respondeu — normal no 1º deploy de um repo novo. "
              f"Tente novamente em 1-2 minutos: {url_base}")

    if tem_cname:
        print("[info] CNAME enviado — falta o usuário criar o registro CNAME "
              "no DNS do domínio apontando para "
              f"{usuario_repo}.github.io antes do domínio próprio funcionar.")


if __name__ == "__main__":
    main()
