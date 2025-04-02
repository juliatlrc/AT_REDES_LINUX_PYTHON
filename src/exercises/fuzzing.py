import requests
import random
import string
import time

def gerar_parametro_aleatorio(tamanho=8):
    """Função que gera uma string aleatória para fuzzing."""
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def realizar_fuzzing(url, num_tests=10):
    """Função que realiza o fuzzing no servidor Web."""
    for i in range(num_tests):
        # Gerar parâmetros aleatórios para enviar
        parametro_aleatorio = gerar_parametro_aleatorio()

        # Enviar a requisição HTTP GET
        nova_url = f"{url}?param={parametro_aleatorio}"
        try:
            resposta = requests.get(nova_url, timeout=5)
            print(f"[+] Testando: {nova_url} | Status Code: {resposta.status_code}")

            # Verificando respostas 500 (erro do servidor) ou outros erros
            if resposta.status_code == 500:
                print(f"[!] Possível vulnerabilidade encontrada no parâmetro: {nova_url}")
            elif resposta.status_code == 400:
                print(f"[!] Erro de requisição em: {nova_url}")
            elif resposta.status_code == 404:
                print(f"[+] Requisição bem-sucedida, mas não encontrado: {nova_url}")
        except requests.exceptions.RequestException as e:
            print(f"[!] Erro ao acessar {nova_url}: {e}")

        # Atraso para evitar sobrecarga no servidor durante os testes
        time.sleep(1)

def main():
    url = input("Digite a URL do servidor Web para realizar o fuzzing (ex: http://example.com): ")
    num_tests = int(input("Digite o número de testes a realizar: "))
    print(f"[*] Iniciando fuzzing em {url}...")

    realizar_fuzzing(url, num_tests)

if __name__ == "__main__":
    main()
