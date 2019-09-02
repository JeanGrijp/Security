"""
Copyright GRIJP, Jean.

Este código ainda está incompleto, em relação ao esperado, mas 
se colocar a seguinte linha do comando no linux, ele executa.
>>> python3 site arquivo_de_subdominiuns_dns.

um detalhe, a biblioteca dns.resolver não vem com o python
sendo necessario instalar com o pip no seguinte comando.
>>> pip install dnspython

"""
################################ IMPORTs ######################################

import dns.resolver
import sys
import urllib.request
import urllib.response
import re

###############################################################################

dominio = sys.argv[1]
nome_arquivo = sys.argv[2]
arquivo_diretorios = sys.argv[3]
with open(nome_arquivo, "r") as arquivo:
    var = arquivo.readlines()
    let = []
    for i in var:
        string = ""
        for j in range(0, len(i)-1):
            string += i[j]
        let.append(string)
        string = ""
    let[-1] = let[-1] + "e"
    for i in let:
        sub = i[:len(i)-1]
        dns_nome = sub + "." + dominio
        try:
            resultado = dns.resolver.query(qname=dns_nome, tcp=False, rdtype="a")
            for resposta in resultado:
                print("SUBDOMINIO: ",sub,"  /  " "DNS: ", dns_nome,"  /  IP: ", resultado[0].address)
        except:
            pass

