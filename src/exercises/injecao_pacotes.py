from scapy.all import sniff, IP, TCP, send
import sys

def processar_pacote(pacote):
    if IP in pacote and TCP in pacote:
        print("\n[INFO] Pacote detectado:")
        print(f"    [ORIGEM] {pacote[IP].src}:{pacote[TCP].sport}")
        print(f"    [DESTINO] {pacote[IP].dst}:{pacote[TCP].dport}")

        pacote_modificado = pacote.copy()
        pacote_modificado[IP].src = "192.168.100.50"
        pacote_modificado[IP].dst = "192.168.100.1"
        pacote_modificado[TCP].dport = 8080

        del pacote_modificado[IP].chksum
        del pacote_modificado[TCP].chksum

        print("[ALERTA] Enviando pacote modificado...")
        send(pacote_modificado, verbose=0)
        print("[SUCESSO] Pacote enviado com sucesso.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Erro: informe a interface de rede como argumento (exemplo: sudo python scapy_ex8.py eth0)")
        sys.exit(1)

    interface = sys.argv[1]
    print(f"[AVISO] Iniciando captura de pacotes na interface {interface}...")
    sniff(iface=interface, prn=processar_pacote, count=15)
