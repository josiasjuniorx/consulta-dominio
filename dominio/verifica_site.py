# -*- coding: utf-8 -*-
import requests, json

def requisicao(dominio):
    try:
        req = requests.get('http://'+dominio, timeout=15)
    except:
        return "Ocorreu um erro ao acessar a URL"
    ok = req.ok
    url = req.url
    tempo = req.elapsed.total_seconds()
    status_code = req.status_code
    encoding = req.encoding
    ap_enc = req.apparent_encoding
    req.headers['content-type']
    conttype = req.headers['content-type']
    redirect = req.is_redirect
    perm_redirect = req.is_permanent_redirect
    cont = req.content
    try:
        length = req.headers['content-length']
    except:
        length=""

    retorno = "\
    <b>OK:</b> {}<br>\
    <b>URL:</b> {}<br>\
    <b>Tempo de resposta:</b> {} segundos<br>\
    <b>Status Code:</b> {}<br>\
    <b>Codificação:</b> {}<br>\
    <b>Codificação Aparente:</b> {}<br>\
    <b>Content-Type:</b> {}<br>\
    <b>Redirecionamento:</b> {}<br>\
    <b>Redirec. Permanente:</b> {}<br>\
    <b>Tamanho:</b> {}<br><br>"\
    .format(ok, url, tempo, status_code, encoding, ap_enc, conttype, redirect, perm_redirect, length)

    return retorno


#http://www.tangowithdjango.com/book/chapters/ajax.html
