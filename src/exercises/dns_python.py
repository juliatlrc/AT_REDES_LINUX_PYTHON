import dns.resolver
import dns.query
import dns.zone
from dns.reversename import from_address


def consulta_dns(domain):
    try:
        print(f"Consultando registros A para o domínio: {domain}")
        resolver = dns.resolver.Resolver()
        resposta = resolver.resolve(domain, 'A')
        for ip in resposta:
            print(f"[+] Registro A: {ip.to_text()}")

        print(f"\nConsultando registros MX para o domínio: {domain}")
        resposta_mx = resolver.resolve(domain, 'MX')
        for mx in resposta_mx:
            print(f"[+] Registro MX: {mx.exchange.to_text()}")

        print(f"\nConsultando registros NS para o domínio: {domain}")
        resposta_ns = resolver.resolve(domain, 'NS')
        for ns in resposta_ns:
            print(f"[+] Registro NS: {ns.target.to_text()}")

    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print(f"[!] Não foi possível obter informações para o domínio: {domain}")
    except Exception as e:
        print(f"[!] Erro ao realizar consulta DNS: {e}")

def pesquisa_de_zona(dns_servidor, dominio):
    try:
        print(f"\nIniciando pesquisa de zona para o domínio {dominio} no servidor DNS {dns_servidor}")
        zona = dns.zone.from_xfr(dns.query.xfr(dns_servidor, dominio))
        for name, node in zona.nodes.items():
            print(f"[+] Nome: {name}, Registros: {node.to_text()}")
    except Exception as e:
        print(f"[!] Erro ao realizar pesquisa de zona: {e}")

def coletar_info_servidor_dns(dns_servidor, dominio):
    print(f"\nConsultando servidor DNS {dns_servidor} para o domínio {dominio}")
    try:
        resposta = dns.resolver.resolve(dominio, 'A', nameservers=[dns_servidor])
        print(f"[+] Resposta do servidor DNS {dns_servidor} para {dominio}: {resposta[0].to_text()}")
    except Exception as e:
        print(f"[!] Erro ao consultar o servidor DNS: {e}")

def main():
    print("[-] Coletando informações sobre servidores DNS")
    dominio = input("Digite o domínio para consulta: ")

    consulta_dns(dominio)

    resolver = dns.resolver.Resolver()
    servidores_dns = resolver.resolve(dominio, 'NS')
    for ns in servidores_dns:
        print(f"\n[+] Servidor DNS encontrado: {ns.target.to_text()}")
        pesquisa_de_zona(ns.target.to_text(), dominio)

    if servidores_dns:
        coletar_info_servidor_dns(servidores_dns[0].target.to_text(), dominio)

if __name__ == "__main__":
    main()
