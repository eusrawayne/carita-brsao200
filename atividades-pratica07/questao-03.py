"""
  Crie um programa que leia um arquivo  informado pelo usuário, percorrendo cada linha do arquivo e a exibe na tela, caso o arquivo não seja encontrado, mostre uma mensagem de er
 """

# Solicita o nome do arquivo ao usuário
nome_arquivo = input("Digite o nome do arquivo para ler: ")

try:
    # Tenta abrir o arquivo no modo leitura
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        
        # Percorre cada linha do arquivo e exibe na tela
        for linha in arquivo:
            print(linha.strip())  # .strip() remove quebra de linha extra

except FileNotFoundError:
    # Caso o arquivo não exista
    print("Erro: Arquivo não encontrado.")

except Exception as erro:
    # Caso outro erro aconteça
    print("Erro ao ler o arquivo:", erro)