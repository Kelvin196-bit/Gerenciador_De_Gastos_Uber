import os
import requests
from datetime import datetime

# Data e hora atual formatada
data_hora_formatada = datetime.now().strftime("%d/%m/%Y às %H:%M")

# Token de acesso do GitHub (use variável de ambiente por segurança)
token = os.getenv("GITHUB_TOKEN")

# Diretório de trabalho atual
caminho_base = os.getcwd()

# Caminhos dos arquivos
lucro_path = os.path.join(caminho_base, "lucro.txt")
rendimentos_path = os.path.join(caminho_base, "Rendimentos.txt")
lucro_marginal_path = os.path.join(caminho_base, "margem_de_lucro_percentual.txt")


# Função para enviar arquivo como Gist privado no GitHub
def send_to_github(content, filename):
    url = "https://api.github.com/gists"
    data = {
        "description": "Meu Gist privado",
        "public": False,
        "files": {
            filename: {
                "content": content
            }
        }
    }
    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/json"
    }
    requests.post(url, json=data, headers=headers)


# Função principal de cálculo
def calcula():
    km_inicial = float(input("Digite o kilometro inicial: "))
    km_final = float(input("Digite o kilometro final: "))
    km_total = km_final - km_inicial
    recebido = float(input("Digite quanto você recebeu da Uber: "))
    valor_gasolina = float(input("Digite o valor da gasolina: "))

    litros_consumidos = km_total / 46
    gasto_gasolina = valor_gasolina * litros_consumidos
    taxa_fixa = (13 / 46) * valor_gasolina
    repasse_kelv = ((gasto_gasolina / 2) + (recebido / 2)) + (taxa_fixa / 2)
    lucro = (recebido - (gasto_gasolina + taxa_fixa)) / 2
    rendimento = (2 * lucro) / (gasto_gasolina + taxa_fixa)
    margem_lucro = ((2 * lucro - 0.015 * km_total - 1) / recebido) * 100

    # Atualiza ou cria os arquivos
    atualizar_arquivo(lucro_path, f"{round(lucro, 2)}\n")
    atualizar_arquivo(rendimentos_path, f"{round(rendimento, 2)}\n")
    atualizar_arquivo(lucro_marginal_path, f"{round(margem_lucro, 2)}%\n")

    return litros_consumidos, gasto_gasolina, repasse_kelv, lucro, rendimento, (lucro - 0.015 * km_total - 1), margem_lucro


# Atualiza o conteúdo do arquivo mantendo cabeçalho com data
def atualizar_arquivo(caminho, novo_valor):
    if not os.path.exists(caminho):
        with open(caminho, "w") as arquivo:
            arquivo.write(f"Data e Hora: {data_hora_formatada}\n")
            arquivo.write(novo_valor)
    else:
        with open(caminho, "a") as arquivo:
            arquivo.write(novo_valor)

        with open(caminho, "r") as file:
            linhas = file.readlines()[1:]  # Remove primeira linha
            novo_conteudo = ''.join(linhas)

        with open(caminho, "w") as file:
            file.write(f"Data e Hora: {data_hora_formatada}\n")
            file.write(novo_conteudo)


# Execução principal
if __name__ == "__main__":
    L, C, H, G, K, lucro_real, margem_lucro = calcula()

    with open(lucro_path, 'r') as file:
        send_to_github(file.read(), "lucro.txt")

    with open(rendimentos_path, 'r') as file:
        send_to_github(file.read(), "Rendimentos.txt")

    with open(lucro_marginal_path, 'r') as file:
        send_to_github(file.read(), "margem_de_lucro_percentual.txt")

    # Exibe os resultados
    print("\n--- Resultados ---")
    print("Você consumiu:", round(L, 2), "litros")
    print("Você gastou: R$", round(C, 2))
    print("Você tem que enviar para Kelv: R$", round(H, 2))
    print("Você lucrou: R$", round(G, 2))
    print("Seu rendimento foi:", round(K, 2))
    print("Seu lucro real:", round(lucro_real, 2))
    print("Sua margem de lucro (por dupla):", round(margem_lucro, 2), "%")
