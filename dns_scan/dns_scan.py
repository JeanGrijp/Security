import dns.resolver
import sys


dominio = sys.argv[1]
nome_arquivo = sys.argv[2]
arquivo = open(nome_arquivo,'r')
subdominiuns = arquivo.readlines()
for i in subdominiuns:
    sub = i[:len(i)-1]
    dns_nome = sub + "." + dominio
    try:
        resultado = dns.resolver.query(dns_nome)
        for resposta in resultado:
            print(dns_nome, resultado[0].address)
    except:
        pass
arquivo.close()
