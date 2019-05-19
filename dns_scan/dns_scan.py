import dns.resolver
import sys


#dominio = sys.argv[1]
#nome_arquivo = sys.argv[2]
#arquivo = open(nome_arquivo,'r')
arquivo = open("dns.txt",'r')
dominio = "globo.com"
subdominiuns = arquivo.readlines()
for i in subdominiuns:
    sub = i[:len(i)-1]
    dns_nome = sub + "." + dominio
    try:
        resultado = dns.resolver.query(qname=dns_nome, tcp=False, rdtype="a")
        for resposta in resultado:
            print("SUBDOMINIO: ",sub,"  /  " "DNS: ", dns_nome,"  /  IP: ", resultado[0].address)
    except:
        pass
arquivo.close()