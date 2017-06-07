# -*- coding: utf-8 -*-

import re
import searchstrings
from subprocess import check_output

def consulta_whois(dominio):
    resposta = check_output(["whois", dominio])
    analise_ns = re.findall(searchstrings.nameserver, str(resposta), re.IGNORECASE)
    analise_dates = re.findall(searchstrings.expiration_date, str(resposta), re.IGNORECASE)
    analise_owner = re.findall(searchstrings.owner, str(resposta), re.IGNORECASE)
    analise = {'dns': analise_ns, 'dates': analise_dates, 'owner': analise_owner}
    return analise

def consulta_host(dominio, nserver):
    def is_responding(tipo, endereco):
        try:
            consulta = check_output(["host", "-t", tipo, endereco, nserver])
        except:
            consulta = None
        return consulta

    def add_ptr(lista_de_ip):
        ip_ptr = []
        for ip in lista_de_ip:
            ptr = is_responding('ptr', ip)
            if ptr is not None:
                ptr = re.findall(searchstrings.ptr, ptr, re.IGNORECASE)
                if len(ptr) > 0:
                    ip_ptr.append({'ip': ip, 'ptr': ptr})
            else:
                ip_ptr.append({'ip': ip})
        return ip_ptr

    def sub_dominios(dominio, nserver):
        sub_dominios = ['www', 'ftp']
        tipos_entrada = ['soa', 'ns', 'server', 'spf', 'mail']
        enderecos = {}

        for sub in sub_dominios:
            checar = is_responding('a', sub+'.'+dominio)
            if checar != None:
                endereco = re.findall(getattr(searchstrings, sub), checar, re.IGNORECASE)
                if sub == 'www' and len(endereco) > 0:
                    endereco = add_ptr(endereco)
                enderecos.update({sub: endereco})

        registros = is_responding('any', dominio)
        if registros != None:
            for tipo in tipos_entrada:
                endereco = re.findall(getattr(searchstrings, tipo), registros, re.IGNORECASE)
                if tipo == 'server' and len(endereco) > 0:
                    endereco = add_ptr(endereco)
                enderecos.update({tipo: endereco})
        return enderecos
    return sub_dominios(dominio, nserver)

def clean_dominio(dominio):
    dominio = re.sub('.*://', '',  dominio)
    dominio = re.sub('/.*', '',  dominio)
    dominio = re.sub(' ', '', dominio)
    return dominio
