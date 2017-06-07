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


    return render(request, 'dominio/index.html', {
        'dominio': dominio,
        'enderecos': enderecos,
        'dns': domain['dns'],
        'domain_expiration': domain['dates'],
        'domain_owner': domain['owner'],
    })
def site(request):
    dominio = request.GET['dominio']
    return HttpResponse(verifica_site.requisicao(dominio))
