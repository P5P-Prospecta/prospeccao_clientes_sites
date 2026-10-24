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
  python3 supabase_client.py proximos CAMINHO/prospector-config.json [--app codex]

No Windows, se "python3" não existir, use "python" (ou "py -3").

O projeto (URL e chave "anon") é o mesmo pra toda a turma — só a
identidade de login (email/senha do aluno) muda, e o RLS do banco
garante que cada aluno só enxerga os próprios dados.
"""

import sys
import json
import datetime
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


def _chamada(metodo, path, body=None, token=None, headers_extra=None, silencioso=False):
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
        if not silencioso:
            print(f"[ERRO HTTP {e.code}] {metodo} {path} -> {corpo}")
            if e.code in (401, 403) and path.startswith("/rest/v1/"):
                print("[DICA] O banco recusou. Se o seu e-mail ainda não tem acesso liberado ao "
                      "P5P Prospecta, use o e-mail da compra do Método P5P (o mesmo do painel). "
                      "Se comprou com outro e-mail, fale com o suporte na área de membros.")
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
    if _tem_acesso(dados["access_token"]) is False:
        print("[AVISO] Este e-mail ainda não tem acesso liberado ao P5P Prospecta. Use o e-mail "
              "da compra do Método P5P (crie a conta no painel com ele). Se comprou com outro "
              "e-mail, fale com o suporte na área de membros do Método P5P.")


def _tem_acesso(token):
    """True/False conforme a compra do Método P5P; None se o banco ainda não tem essa regra."""
    try:
        _, dados = _chamada("POST", "/rest/v1/rpc/tem_acesso", body={}, token=token, silencioso=True)
    except Exception:
        return None
    return dados is True


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
    # on_conflict=user_id,slug: sem isso o banco tenta criar outro lead com o mesmo slug
    # e recusa (409). Com ele, o lead que já existe é atualizado só nos campos enviados.
    _chamada(
        "POST", "/rest/v1/leads?on_conflict=user_id,slug",
        body=corpo, token=token,
        headers_extra={"Prefer": "resolution=merge-duplicates",
                        "Content-Type": "application/json"},
    )
    print(f"[ok] Lead '{corpo.get('slug')}' salvo.")


# ---------------------------------------------------------------------------
# O que fazer agora: a mesma lógica da aba "Linha de produção" do painel web.
# ---------------------------------------------------------------------------
ETAPAS = ["Achado", "Refeito", "No ar", "Proposta", "Respondeu", "Fechado", "Pago"]
ORDEM_STATUS = ["novo", "redesenhado", "publicado", "proposta", "respondeu", "fechado"]
LIMITE = {"redesenhado": 2, "publicado": 2, "respondeu": 2, "fechado": 5}  # dias sem movimento
FOLLOWUP_DIAS = 3


def _dias_desde(valor):
    if not valor:
        return 0
    try:
        data = datetime.date.fromisoformat(str(valor)[:10])
    except ValueError:
        return 0
    return max(0, (datetime.date.today() - data).days)


def _estacao(lead):
    status = lead.get("status") or "novo"
    if status == "descartado":
        return -1
    if status == "fechado" and lead.get("pago"):
        return 6
    return ORDEM_STATUS.index(status) if status in ORDEM_STATUS else 0


def _dinheiro(valor):
    texto = f"{float(valor or 0):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return "R$ " + texto


def proximo_passo(lead, github_ok=True):
    """Devolve (o que fazer, comando ou None, está parado?, dias)."""
    nome = lead.get("nome") or lead.get("slug")
    est = _estacao(lead)
    mexido = _dias_desde(lead.get("atualizado_em"))
    if est == 0:
        return "Refazer o site com o conteúdo real do cliente", f"/redesenhar {nome}", False, mexido
    if est == 1:
        texto = "Publicar a página nova" if github_ok else "Conectar o GitHub (painel, Configurações) e publicar"
        return texto, f"/publicar {nome}", mexido >= LIMITE["redesenhado"], mexido
    if est == 2:
        texto = "Mandar a proposta por e-mail" if lead.get("email") else "Sem e-mail: a proposta vai pelo WhatsApp"
        return texto, f"/proposta {nome}", mexido >= LIMITE["publicado"], mexido
    if est == 3:
        if "follow" in (lead.get("obs") or "").lower():
            return ("Já recebeu o follow-up. Sem resposta: tente o WhatsApp ou descarte",
                    f"/respostas {nome}", mexido >= 4, mexido)
        dias = _dias_desde(lead.get("data_proposta") or lead.get("atualizado_em"))
        if dias >= FOLLOWUP_DIAS:
            return f"Sem resposta há {dias} dias: mandar o follow-up", f"/followup {nome}", True, dias
        return "Esperando a resposta. Conferir o e-mail", "/respostas", False, dias
    if est == 4:
        return ("Respondeu: falar com o cliente e combinar o valor. Quando fechar, marque Fechado no painel",
                None, mexido >= LIMITE["respondeu"], mexido)
    if est == 5:
        contrato = lead.get("contrato_status") or "pendente"
        parado = mexido >= LIMITE["fechado"]
        if contrato == "pendente":
            return "Fechou: gerar o contrato", f"/contrato {nome}", parado, mexido
        if contrato == "enviado":
            return "Contrato enviado: esperando a assinatura. Quando assinar, marque no painel", None, parado, mexido
        return "Contrato assinado: receber o pagamento e marcar Pago no painel", None, parado, mexido
    if est == 6:
        manut = lead.get("manutencao")
        return (f"Pago. Manutenção de {_dinheiro(manut)} por mês" if manut else "Pago"), None, False, 0
    return "Descartado", None, False, 0


def texto_proximos(leads, github_ok=True, app="claude"):
    p = "$" if app == "codex" else "/"
    if not leads:
        return ("Nenhum cliente ainda.\n"
                f"Comece por {p}prospectar (se ainda não fez a configuração, rode {p}setup antes).")
    ativos, pagos, descartados = [], 0, 0
    for lead in leads:
        est = _estacao(lead)
        if est == -1:
            descartados += 1
        elif est == 6:
            pagos += 1
        else:
            ativos.append((lead, est, proximo_passo(lead, github_ok)))
    parados = sorted([a for a in ativos if a[2][2]], key=lambda a: -a[2][3])
    andando = sorted([a for a in ativos if not a[2][2]], key=lambda a: -a[1])

    linhas = [f"O QUE FAZER AGORA ({len(ativos)} clientes ativos, {len(parados)} parados)"]

    def bloco(titulo, itens):
        if not itens:
            return
        linhas.append("")
        linhas.append(titulo)
        for n, (lead, est, (texto, cmd, parado, dias)) in enumerate(itens, 1):
            cab = f"{n}. {lead.get('nome') or lead.get('slug')} · {ETAPAS[est]}"
            if parado:
                cab += f" · parado há {dias} {'dia' if dias == 1 else 'dias'}"
            linhas.append(cab)
            linhas.append(f"   {texto}")
            if cmd:
                if p == "$" and cmd.startswith("/"):
                    cmd = "$" + cmd[1:]
                linhas.append(f"   Comando: {cmd}")

    bloco("PARADOS (faça primeiro)", parados)
    bloco("ANDANDO (do mais perto de fechar para o começo)", andando)
    if not ativos:
        linhas.append("")
        linhas.append(f"Nenhum cliente ativo agora. Rode {p}prospectar para achar mais.")
    linhas.append("")
    linhas.append(f"Pagos: {pagos} · Descartados: {descartados}")
    return "\n".join(linhas)


def proximos(caminho_config, app="claude"):
    token, user_id = _access_token(caminho_config)
    _, leads = _chamada("GET", f"/rest/v1/leads?user_id=eq.{user_id}&select=*", token=token)
    _, perfis = _chamada("GET", f"/rest/v1/perfis?user_id=eq.{user_id}&select=github_usuario,github_token",
                         token=token)
    perfil = perfis[0] if perfis else {}
    github_ok = bool(perfil.get("github_usuario") and perfil.get("github_token"))
    print(texto_proximos(leads, github_ok, app))


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
    elif comando == "proximos":
        i = resto.index("--app") if "--app" in resto else -1
        app = resto[i + 1].lower() if 0 <= i < len(resto) - 1 else "claude"
        proximos(caminho_config, app)
    else:
        print(f"[ERRO] Comando desconhecido: {comando}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
