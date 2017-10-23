from .whois import *
import verifica_site
from django.shortcuts import render
import os
import logging

from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse

logging.basicConfig(level=logging.INFO,
                    format='\
                    <center><table style="border:1px;border-style:solid;\
                    width:900px;color:blue;border-color:black;font-size:12px">\
                    <tr><td>%(asctime)s  %(message)s</td></tr>',
                    datefmt='%d/%b/%Y %H:%M:%S',
                    filename='templates/dominio/logs.html',
                    filemode='w'
                    )

def index(request):
    if not request.method == 'POST':
        return render(request, 'dominio/index.html')

    dominio = request.POST['dominio']
    dominio = clean_dominio(dominio)
    cliente = request.META.get('REMOTE_ADDR')

    nserver = request.POST['nserver']
    whois = consulta_whois(dominio)
    enderecos = consulta_host(dominio, nserver)

    logging.info('[%s] consultou o dominio ( %s )', cliente, dominio)

    return render(request, 'dominio/index.html', {
        'dominio': dominio,
        'enderecos': enderecos,
        'whois': whois
    })

def site(request):
    dominio = request.GET['dominio']
    return HttpResponse(verifica_site.requisicao(dominio))
def logs(request):
    return render(request, 'dominio/logs.html')
