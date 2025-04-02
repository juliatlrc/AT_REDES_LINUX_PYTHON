import nmap
import threading


def varredura_sincrona(ip, portas):
    nm = nmap.PortScanner()
    print(f"[*] Iniciando varredura síncrona para o IP {ip} nas portas {portas}...")

    for porta in portas:
        resultado = nm.scan(ip, str(porta))
        estado = resultado['scan'][ip]['tcp'][porta]['state']
        print(f"Porta {porta} está {estado}")


def varredura_assincrona(ip, portas):
    nm = nmap.PortScanner()
    print(f"[*] Iniciando varredura assíncrona para o IP {ip} nas portas {portas}...")

    def varrer_porta(porta):
        resultado = nm.scan(ip, str(porta))
        estado = resultado['scan'][ip]['tcp'][porta]['state']
        print(f"Porta {porta} está {estado}")

    threads = []

    for porta in portas:
        t = threading.Thread(target=varrer_porta, args=(porta,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


def main():
    ip = input("Digite o IP do alvo: ")
    portas_str = input("Digite as portas a serem escaneadas, separadas por vírgula: ")
    portas = [int(p.strip()) for p in portas_str.split(",")]

    tipo_varredura = input("Escolha o tipo de varredura (1 para síncrona, 2 para assíncrona): ")

    if tipo_varredura == "1":
        varredura_sincrona(ip, portas)
    elif tipo_varredura == "2":
        varredura_assincrona(ip, portas)
    else:
        print("Opção inválida. Selecione 1 ou 2.")


if __name__ == "__main__":
    main()
