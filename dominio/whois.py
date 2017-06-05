# -*- coding: utf-8 -*-

import re
import searchstrings
from subprocess import Popen, PIPE, check_output

def consulta_whois(dominio):
    resposta = check_output(["whois", dominio])
    analise_ns = re.findall(searchstrings.nameserver, str(resposta), re.IGNORECASE)
    analise_dates = re.findall(searchstrings.expiration_date, str(resposta), re.IGNORECASE)
    analise_owner = re.findall(searchstrings.owner, str(resposta), re.IGNORECASE)
    analise = {'dns': analise_ns, 'dates': analise_dates, 'owner': analise_owner}
    return analise

def consulta_host(dominio, nserver):
    def resposta(tipo, prefixo, dominio):
        try:
            consulta = check_output(["host", "-t", tipo, prefixo+dominio, nserver])
        except:
            pass
        return consulta

    def add_ptr(lista_de_ip):
        ip_ptr = []
        for ip in lista_de_ip:
            try:
                ptr = re.findall(searchstrings.ptr, resposta('ptr', '', ip), re.IGNORECASE)
                if len(ptr) > 0:
                    ip_ptr.append(ip+' [ '+ptr[0]+' ]')
            except:
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
    consulta = check_output(["dig", "-t", tipo, dominio, "+short"])
    if (tipo == "soa" or tipo == "SOA") and len(consulta) > 0:
        l_consulta = consulta.split()
        consulta = {'autoridade': l_consulta[0], 'email': l_consulta[1], 'serial': l_consulta[2]}
    return consulta

def clean_dominio(dominio):
    dominio = re.sub('.*://', '', dominio)
    dominio = re.sub(' ', '', dominio)
    return dominio
