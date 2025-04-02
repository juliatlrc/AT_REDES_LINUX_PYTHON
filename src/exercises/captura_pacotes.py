from scapy.all import *

def listar_interfaces():
    interfaces = get_if_list()
    print("Interfaces de rede disponíveis:")
    for interface in interfaces:
        print(interface)

def capturar_pacotes(interface):
    print(f"Capturando pacotes na interface {interface}...")
    sniff(iface=interface, prn=processar_pacote, store=0)

def processar_pacote(packet):
    print(f"Pacote capturado: {packet.summary()}")

if __name__ == "__main__":
    listar_interfaces()

    interface = input("Digite a interface de rede para captura (ex: eth0): ")
    capturar_pacotes(interface)
