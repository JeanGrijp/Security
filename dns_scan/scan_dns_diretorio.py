import dns.resolver
import sys
import urllib.request



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

