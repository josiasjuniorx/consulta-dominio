from .whois import *
from django.shortcuts import render

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse

def index(request):
    if not request.method == 'POST':
        return render(request, 'dominio/index.html')


    dominio = request.POST['dominio']


    nserver = request.POST['nserver']
    domain = consulta_whois(dominio)
    enderecos = consulta_host(dominio, nserver)
    dns_txt = consulta_dig(dominio, "TXT")
    dns_soa = consulta_dig(dominio, "SOA")

    return render(request, 'dominio/index.html', {
        'dominio': dominio,
        'dns': domain['dns'],
        'address': enderecos['address'],
        'mail': enderecos['mail'],
        'ftp': enderecos['ftp'],
        'www': enderecos['www'],
        'domain_expiration': domain['dates'],
        'domain_owner': domain['owner'],
        'dns_txt': dns_txt,
        'dns_soa': dns_soa,
    })
