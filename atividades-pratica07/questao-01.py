"""
Crie um programa que lê um arquivo CSV de  com a biblioteca , calcule e exiba a  e o  da coluna tempo_execucao, caso e o arquivo não exista ou houver erro na leitura, mostre uma mensagem de erro. 
"""
import pandas as pd  # Importa a biblioteca pandas para manipular arquivos CSV

# Caminho completo do arquivo CSV
caminho = r"C:\Users\USER\Desktop\BRAO200\atividades-pratica07\dados.csv"

try:
    # Lê o arquivo CSV
    df = pd.read_csv(caminho)

    # Exibe as 5 primeiras linhas
    print("Primeiras 5 linhas do arquivo:")
    print(df.head())

    # Exibe as colunas do arquivo
    print("\nColunas encontradas no arquivo:")
    print(df.columns)

    # Exibe informações gerais do CSV
    print("\nInformações gerais:")
    print(df.info())

except FileNotFoundError:
    print("Erro: Arquivo CSV não encontrado. Verifique o caminho informado.")
except Exception as erro:
    print("Erro inesperado:", erro)