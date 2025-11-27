"""
Crie um programa que leia e escreva arquivos no formato , que salve em um dicionário com nome, idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados, caso o arquivo não existir ou ocorrer erro ao salvar, mostre uma mensagem de falha.
"""
import json  # Biblioteca padrão para trabalhar com arquivos JSON

# Dados a serem salvos no arquivo
dados = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "Vitória"
}

# Nome do arquivo JSON
arquivo_json = input("Digite o nome do arquivo para salvar (ex: dados.json): ")

# -----------------------------
# SALVANDO O ARQUIVO JSON
# -----------------------------
try:
    with open(arquivo_json, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
    print(f"Arquivo '{arquivo_json}' salvo com sucesso!")

except Exception as erro:
    print("Falha ao salvar o arquivo JSON:", erro)
    exit()  # Encerra o programa se não conseguir salvar


# -----------------------------
# LENDO O ARQUIVO JSON
# -----------------------------
try:
    with open(arquivo_json, "r", encoding="utf-8") as arquivo:
        conteudo = json.load(arquivo)
    
    print("\nConteúdo do arquivo JSON:")
    print(f"Nome: {conteudo['nome']}")
    print(f"Idade: {conteudo['idade']}")
    print(f"Cidade: {conteudo['cidade']}")

except FileNotFoundError:
    print("Erro: Arquivo JSON não encontrado.")

except Exception as erro:
    print("Erro ao ler o arquivo JSON:", erro)
