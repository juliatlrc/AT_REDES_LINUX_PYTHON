import sys

from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr1


def escanear_porta(ip, porta):
    pacotes = IP(dst=ip)/TCP(dport=porta, flags="S")
    resposta = sr1(pacotes, timeout=1, verbose=0)

    if resposta is None:
        print(f"[{porta}] Porta fechada ou sem resposta.")
    elif resposta.haslayer(TCP):
        if resposta[TCP].flags == 18:
            print(f"[{porta}] Porta aberta.")
        elif resposta[TCP].flags == 20:
            print(f"[{porta}] Porta fechada.")

def escanear_portas(ip, portas):
    print(f"[INFO] Iniciando escaneamento de portas no host {ip}...")
    for porta in portas:
        escanear_porta(ip, porta)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python scapy_escaneamento.py <IP> <porta1,porta2,...>")
        sys.exit(1)

    ip_destino = sys.argv[1]
    portas_destino = [int(porta) for porta in sys.argv[2].split(",")]

    escanear_portas(ip_destino, portas_destino)
