# -*- coding: utf-8 -*-

import re
import searchstrings
from subprocess import Popen, PIPE

def consulta_whois(dominio):
    consulta = Popen(["whois", dominio], stdin=PIPE, stdout=PIPE)
    resposta = unicode(consulta.communicate("n\n")[0], encoding='ascii', errors='ignore')
    analise_ns = re.findall(searchstrings.nameserver, str(resposta), re.IGNORECASE)
    analise_dates = re.findall(searchstrings.expiration_date, str(resposta), re.IGNORECASE)
    analise_owner = re.findall(searchstrings.owner, str(resposta), re.IGNORECASE)
    analise = {'dns': analise_ns, 'dates': analise_dates, 'owner': analise_owner}
    return analise

def consulta_host(dominio, nserver):
    def resposta(tipo, prefixo, dominio):
        consulta = Popen(["host", "-t", tipo, prefixo+dominio, nserver], stdin=PIPE, stdout=PIPE)
        retorna_consulta = consulta.communicate("n\n")[0]
        return retorna_consulta

    def add_ptr(lista_de_ip):
        ip_ptr = []
        for ip in lista_de_ip:
            ptr = re.findall(searchstrings.ptr, resposta('ptr', '', ip), re.IGNORECASE)
            if len(ptr) > 0:
                ip_ptr.append(ip+' [ '+ptr[0]+' ]')
            else:
                ip_ptr.append(ip)
        return ip_ptr

    analise_address = re.findall(searchstrings.address, resposta('a', '', dominio), re.IGNORECASE)
    analise_mail = re.findall(searchstrings.mail, resposta('mx', '', dominio), re.IGNORECASE)
    analise_ftp = re.findall(searchstrings.ftp, resposta('a', 'ftp.', dominio), re.IGNORECASE)
    analise_www = re.findall(searchstrings.address, resposta('a', 'www.', dominio), re.IGNORECASE)

    analise = {
        'address': add_ptr(analise_address),
        'mail': analise_mail,
        'ftp': analise_ftp,
        'www': add_ptr(analise_www),
    }
    return analise

def consulta_dig(dominio, tipo):
    consulta = Popen(["dig", "-t", tipo, dominio, "+short"], stdin=PIPE, stdout=PIPE)
    analise_dig = consulta.communicate("n\n")[0]
    return analise_dig
