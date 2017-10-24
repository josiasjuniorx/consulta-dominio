from .whois import *
import verifica_site
from django.shortcuts import render
import os
import logging

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse

logger = logging.getLogger("CONSULTAS")
logger.setLevel(logging.INFO)
handler = logging.FileHandler('static/logs.html')
formatter = logging.Formatter(\
    '<center><table style="border:1px;border-style:solid;\
    width:900px;color:blue;border-color:black;font-size:12px">\
    <tr><td>%(asctime)s [UTC] - %(message)s</td></tr>',
    datefmt='%d/%b/%Y %H:%M:%S'\
)
handler.setFormatter(formatter)
logger.addHandler(handler)

def index(request):
    if not request.method == 'POST':
        return render(request, 'dominio/index.html')

    dominio = request.POST['dominio']
    dominio = clean_dominio(dominio)
    cliente = request.META.get('REMOTE_ADDR')

    nserver = request.POST['nserver']
    whois = consulta_whois(dominio)
    enderecos = consulta_host(dominio, nserver)

    logger.info('[ %s ] consultou o dominio ( %s )', cliente, dominio)

    return render(request, 'dominio/index.html', {
        'dominio': dominio,
        'enderecos': enderecos,
        'whois': whois
    })

def site(request):
    dominio = request.GET['dominio']
    return HttpResponse(verifica_site.requisicao(dominio))
