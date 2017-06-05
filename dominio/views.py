from .whois import *
import verifica_site
from django.shortcuts import render
import os

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse

def index(request):
    if not request.method == 'POST':
        return render(request, 'dominio/index.html')

    dominio = request.POST['dominio']
    dominio = clean_dominio(dominio)

    nserver = request.POST['nserver']
    domain = consulta_whois(dominio)
    enderecos = consulta_host(dominio, nserver)
    dns_txt = consulta_dig(dominio, "TXT")
    dns_soa = consulta_dig(dominio, "SOA")

    return render(request, 'dominio/index.html', {
        'dominio': dominio,
        'address': enderecos['address'],
        'mail': enderecos['mail'],
        'ftp': enderecos['ftp'],
        'www': enderecos['www'],
        'dns': domain['dns'],
        'domain_expiration': domain['dates'],
        'domain_owner': domain['owner'],
        'dns_txt': dns_txt,
        'dns_soa': dns_soa,
    })
def site(request):
    dominio = request.GET['dominio']
    return HttpResponse(verifica_site.requisicao(dominio))
