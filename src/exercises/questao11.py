from scapy.all import sniff, IP, TCP, UDP


def processar_pacote(pacote):
    if IP in pacote:
        ip_src = pacote[IP].src
        ip_dst = pacote[IP].dst
        protocolo = pacote[IP].proto

        if TCP in pacote:
            porta_src = pacote[TCP].sport
            porta_dst = pacote[TCP].dport
            print(f"Pacote TCP: {ip_src}:{porta_src} -> {ip_dst}:{porta_dst}")

        elif UDP in pacote:
            porta_src = pacote[UDP].sport
            porta_dst = pacote[UDP].dport
            print(f"Pacote UDP: {ip_src}:{porta_src} -> {ip_dst}:{porta_dst}")

        else:
            print(f"Pacote IP: {ip_src} -> {ip_dst} (Protocólo: {protocolo})")


def capturar_pacotes(interface):
    print(f"Iniciando captura de pacotes na interface {interface}...")
    sniff(iface=interface, prn=processar_pacote, store=0, count=10)  # Captura 10 pacotes


if __name__ == "__main__":
    interface = input("Digite a interface de rede para captura (ex: eth0): ")
    capturar_pacotes(interface)
