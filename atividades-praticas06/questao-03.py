"""
3 - Crie um programa que consulte informações de um CEP na API ViaCEP,
retorne logradouro, bairro, cidade e estado do CEP digitado.
Caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.
"""

import requests

def consultar_cep():
    cep = input("Digite um CEP (somente números): ")

    # Validação simples
    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido! Digite exatamente 8 números.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url)

        # Se não conseguir conectar
        if resposta.status_code != 200:
            print("Erro ao se conectar à API!")
            return

        dados = resposta.json()

        # API retorna "erro": true quando o CEP não existe
        if "erro" in dados:
            print("CEP não encontrado!")
            return

        print("\n=== Resultado da Consulta ===")
        print(f"Logradouro: {dados['logradouro']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")
    
    except Exception as e:
        print("Falha na requisição:", e)

consultar_cep()
