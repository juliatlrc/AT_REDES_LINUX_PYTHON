from scapy.all import *

def capturar_pacotes(interface):
    print(f"Capturando pacotes na interface {interface}...")
    
    def processar_pacote(packet):
        print(f"Pacote capturado: {packet.summary()}")
        if packet.haslayer(ICMP):
            analisar_pacote(packet)
            modificar_pacote(packet)

    sniff(iface=interface, prn=processar_pacote, store=0)

def analisar_pacote(packet):
    print(f"Analisando pacote ICMP:")
    print(f"IP de origem: {packet[IP].src}")
    print(f"IP de destino: {packet[IP].dst}")
    print(f"Tipo de ICMP: {packet[ICMP].type}")
    print(f"ID do pacote ICMP: {packet[ICMP].id}")
    print(f"Sequência do pacote ICMP: {packet[ICMP].seq}")

def modificar_pacote(packet):
    novo_destino = "8.8.8.8"
    print(f"Modificando o pacote ICMP para destino {novo_destino}")
    pacote_modificado = packet.copy()
    pacote_modificado[IP].dst = novo_destino
    print(f"Injetando pacote modificado para {novo_destino}")
    send(pacote_modificado)

def injetar_pacote(destino_ip):
    pacote = IP(dst=destino_ip)/ICMP()
    print(f"Injetando pacote ICMP para {destino_ip}")
    send(pacote)

if __name__ == "__main__":
    interface = input("Digite a interface de rede para captura (ex: eth0): ")
    capturar_pacotes(interface)
    destino_ip = input("Digite o IP de destino para injeção (ex: 192.168.1.1): ")
    injetar_pacote(destino_ip)

