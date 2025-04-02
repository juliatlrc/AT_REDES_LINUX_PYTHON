from scapy.all import ARP, Ether, srp
import time

arp_cache = {}

def obter_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    pacote = broadcast/arp_request
    resposta = srp(pacote, timeout=1, verbose=False)[0]

    for elemento in resposta:
        return elemento[1].hwsrc

    return None

def verificar_arp_spoofing():
    print("Verificando ARP Spoofing...")

    ip_range = "192.168.1.1/24"
    ips_na_rede = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    pacote = broadcast/ips_na_rede
    respostas, nao_respostas = srp(pacote, timeout=3, verbose=False)

    for resposta in respostas:
        ip = resposta[1].psrc
        mac = resposta[1].hwsrc

        if ip in arp_cache:
            if arp_cache[ip] != mac:
                print(f"[ALERTA] ARP Spoofing detectado! IP: {ip} | MAC alterado de {arp_cache[ip]} para {mac}")
        arp_cache[ip] = mac

while True:
    verificar_arp_spoofing()
    time.sleep(5)
