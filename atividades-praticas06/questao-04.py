"""
4 - Crie um programa que realize consultas a cotações de moedas em relação ao Real (BRL)
usando a API AwesomeAPI, mostre valor atual, máxima, mínima e data/hora da última atualização.
Caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.
"""

import requests

def consultar_moeda():
    print("Moedas disponíveis: USD, EUR, GBP, ARS, BTC, JPY etc.")
    moeda = input("Digite o código da moeda que deseja consultar: ").upper()

    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)

        # Erro de conexão
        if resposta.status_code != 200:
            print("Erro ao conectar à API!")
            return
        
        dados = resposta.json()

        # O objeto chave muda: USD-BRL → USDBRL
        chave = f"{moeda}BRL"

        # Verifica se existe no retorno
        if chave not in dados:
            print("Moeda não encontrada! Verifique o código.")
            return

        info = dados[chave]

        print("\n=== Cotação Atual ===")
        print(f"Moeda: {info['code']} → Real (BRL)")
        print(f"Valor atual: R$ {info['bid']}")
        print(f"Máxima do dia: R$ {info['high']}")
        print(f"Mínima do dia: R$ {info['low']}")
        print(f"Última atualização: {info['create_date']}")

    except Exception as e:
        print("Erro ao realizar a consulta:", e)

consultar_moeda()
