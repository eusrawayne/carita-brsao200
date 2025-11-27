"""
Crie um programa que cria um arquivo  com nome, idade e cidade de algumas pessoas, que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário, caso ocorra um erro ao salvar, mostre uma mensagem de falha. 
"""


# Lista de dados das pessoas
pessoas = [
    ["Nome", "Idade", "Cidade"],
    ["Ana", "25", "Vitória"],
    ["Bruno", "30", "Serra"],
    ["Camila", "22", "Vila Velha"],
    ["Daniel", "28", "Cariacica"]
]

# Solicita ao usuário o nome do arquivo de saída
nome_arquivo = input("Digite o nome do arquivo para salvar (ex: pessoas.txt): ")

try:
    # Tentativa de abrir o arquivo para escrita
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        
        # Escreve cada linha em formato tabular (separado por TAB)
        for linha in pessoas:
            arquivo.write("\t".join(linha) + "\n")

    print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")

except Exception as erro:
    # Caso ocorra erro ao salvar o arquivo
    print("Falha ao salvar o arquivo:", erro)