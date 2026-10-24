#!/usr/bin/env python3
"""
Monta o link "Abrir no Gmail": um clique abre o Gmail do aluno já com
destinatário, assunto e texto preenchidos. Ele revisa e clica em Enviar.
Serve quando o app (Claude ou Codex) não tem o Gmail conectado.

Uso:
  python link_gmail.py --para cliente@email.com --assunto "Assunto" --corpo-arquivo corpo.txt
  python link_gmail.py --para cliente@email.com --assunto "Assunto" --corpo "Texto do e-mail"
  (opcional) --conta email-do-aluno@gmail.com   abre na conta certa se ele tiver mais de um Gmail

No Windows use "python"; no Mac, "python3". Só usa a biblioteca padrão.
"""
import argparse
import sys
import urllib.parse


def montar_link(para, assunto, corpo, conta=None):
    params = {'view': 'cm', 'fs': '1', 'to': para.strip(), 'su': assunto.strip(), 'body': corpo}
    if conta:
        params = {'authuser': conta.strip(), **params}
    return 'https://mail.google.com/mail/?' + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)


def main():
    ap = argparse.ArgumentParser(description='Link "Abrir no Gmail" com o e-mail pronto.')
    ap.add_argument('--para', required=True)
    ap.add_argument('--assunto', required=True)
    grupo = ap.add_mutually_exclusive_group(required=True)
    grupo.add_argument('--corpo')
    grupo.add_argument('--corpo-arquivo')
    ap.add_argument('--conta')
    a = ap.parse_args()
    corpo = a.corpo if a.corpo is not None else open(a.corpo_arquivo, encoding='utf-8-sig').read()
    corpo = corpo.replace('\r\n', '\n').strip() + '\n'
    if '@' not in a.para:
        sys.exit('[ERRO] E-mail do cliente inválido.')
    print(montar_link(a.para, a.assunto, corpo, a.conta))


if __name__ == '__main__':
    main()
