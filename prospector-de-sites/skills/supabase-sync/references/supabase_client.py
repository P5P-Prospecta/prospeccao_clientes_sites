#!/usr/bin/env python3
"""
Cliente do Supabase pro Prospector de Sites. Só usa a biblioteca padrão
do Python (urllib) — sem instalar nada. Guarda só o "refresh token" no
config (nunca a senha), e renova o token de acesso sozinho a cada uso.

Uso:
  python3 supabase_client.py login CAMINHO/prospector-config.json EMAIL SENHA
  python3 supabase_client.py get-perfil CAMINHO/prospector-config.json
  python3 supabase_client.py set-perfil CAMINHO/prospector-config.json '{"nome":"..."}'
  python3 supabase_client.py list-leads CAMINHO/prospector-config.json [status]
  python3 supabase_client.py upsert-lead CAMINHO/prospector-config.json '{"slug":"...", ...}'

O projeto (URL e chave "anon") é o mesmo pra toda a turma — só a
identidade de login (email/senha do aluno) muda, e o RLS do banco
garante que cada aluno só enxerga os próprios dados.
"""

import sys
import json
import urllib.request
import urllib.error

# Mesmo projeto Supabase para todos os alunos — a chave "anon" é pública
# por design (protegida pelas políticas de RLS do banco).
SUPABASE_URL = "https://jzlkqzamkgxxlbmpfisq.supabase.co"
SUPABASE_ANON_KEY = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imp6bGtxemFta2d4eGxibXBmaXNxIiwicm9sZSI6"
    "ImFub24iLCJpYXQiOjE3ODcyNjQxODQsImV4cCI6MjEwMjg0MDE4NH0."
    "csGO129p80m2dP-6iLQkzT7PnEOal2ZgheOKi9o_u-s"
)


def _ler_config(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def _salvar_config(caminho, cfg):
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(cfg, f, ensure_ascii=False, indent=2)


def _chamada(metodo, path, body=None, token=None, headers_extra=None):
    url = SUPABASE_URL + path
    dados = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=dados, method=metodo)
    req.add_header("apikey", SUPABASE_ANON_KEY)
    req.add_header("Authorization", f"Bearer {token or SUPABASE_ANON_KEY}")
    req.add_header("Content-Type", "application/json")
    if headers_extra:
        for k, v in headers_extra.items():
            req.add_header(k, v)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            corpo = resp.read()
            return resp.status, (json.loads(corpo) if corpo else {})
    except urllib.error.HTTPError as e:
        corpo = e.read().decode("utf-8", "ignore")
        print(f"[ERRO HTTP {e.code}] {metodo} {path} -> {corpo}")
        raise


def login(caminho_config, email, senha):
    status, dados = _chamada(
        "POST", "/auth/v1/token?grant_type=password",
        body={"email": email, "password": senha},
    )
    cfg = _ler_config(caminho_config)
    cfg["supabase"] = {
        "refresh_token": dados["refresh_token"],
        "user_id": dados["user"]["id"],
        "email": email,
    }
    _salvar_config(caminho_config, cfg)
    print(f"[ok] Login feito. Aluno: {email} (id {dados['user']['id']})")


def _access_token(caminho_config):
    cfg = _ler_config(caminho_config)
    sb = cfg.get("supabase") or {}
    refresh_token = sb.get("refresh_token")
    if not refresh_token:
        print("[ERRO] Ainda não fez login. Rode: "
              "python3 supabase_client.py login CONFIG EMAIL SENHA")
        sys.exit(1)
    status, dados = _chamada(
        "POST", "/auth/v1/token?grant_type=refresh_token",
        body={"refresh_token": refresh_token},
    )
    # o Supabase troca o refresh token a cada uso — salva o novo sempre
    sb["refresh_token"] = dados["refresh_token"]
    sb["user_id"] = dados["user"]["id"]
    cfg["supabase"] = sb
    _salvar_config(caminho_config, cfg)
    return dados["access_token"], sb["user_id"]


def get_perfil(caminho_config):
    token, user_id = _access_token(caminho_config)
    status, dados = _chamada(
        "GET", f"/rest/v1/perfis?user_id=eq.{user_id}&select=*",
        token=token,
    )
    print(json.dumps(dados[0] if dados else {}, ensure_ascii=False, indent=2))


def set_perfil(caminho_config, perfil_json):
    token, user_id = _access_token(caminho_config)
    corpo = json.loads(perfil_json)
    corpo["user_id"] = user_id
    _chamada(
        "POST", "/rest/v1/perfis",
        body=corpo, token=token,
        headers_extra={"Prefer": "resolution=merge-duplicates"},
    )
    print("[ok] Perfil salvo.")


def list_leads(caminho_config, status_filtro=None):
    token, user_id = _access_token(caminho_config)
    path = f"/rest/v1/leads?user_id=eq.{user_id}&select=*&order=criado_em.desc"
    if status_filtro:
        path += f"&status=eq.{status_filtro}"
    status, dados = _chamada("GET", path, token=token)
    print(json.dumps(dados, ensure_ascii=False, indent=2))


def upsert_lead(caminho_config, lead_json):
    token, user_id = _access_token(caminho_config)
    corpo = json.loads(lead_json)
    corpo["user_id"] = user_id
    _chamada(
        "POST", "/rest/v1/leads",
        body=corpo, token=token,
        headers_extra={"Prefer": "resolution=merge-duplicates",
                        "Content-Type": "application/json"},
    )
    print(f"[ok] Lead '{corpo.get('slug')}' salvo.")


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    comando, caminho_config = sys.argv[1], sys.argv[2]
    resto = sys.argv[3:]

    if comando == "login":
        login(caminho_config, resto[0], resto[1])
    elif comando == "get-perfil":
        get_perfil(caminho_config)
    elif comando == "set-perfil":
        set_perfil(caminho_config, resto[0])
    elif comando == "list-leads":
        list_leads(caminho_config, resto[0] if resto else None)
    elif comando == "upsert-lead":
        upsert_lead(caminho_config, resto[0])
    else:
        print(f"[ERRO] Comando desconhecido: {comando}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
