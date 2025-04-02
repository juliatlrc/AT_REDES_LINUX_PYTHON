from scapy.all import IP, ICMP, send, sniff


def injetar_pacote(destino_ip):
    pacote = IP(dst=destino_ip) / ICMP()
    print(f"Injetando pacote ICMP para {destino_ip}")
    send(pacote)


def capturar_resposta(interface):
    print(f"Capturando pacotes na interface {interface}...")

    def processar_pacote(packet):
        if packet.haslayer(ICMP):
            print(f"Pacote ICMP capturado: {packet.summary()}")

    sniff(iface=interface, prn=processar_pacote, store=0)


if __name__ == "__main__":
    destino_ip = input("Digite o IP de destino para injeção (ex: 192.168.1.1): ")
    injetar_pacote(destino_ip)

    interface = input("Digite a interface de rede para captura (ex: eth0): ")
    capturar_resposta(interface)
