"""
2 - Criar um programa que acesse a API Random User Generator para buscar um usuário fictício aleatório.
Exibir o nome, e-mail e país desse usuário. Em caso de erro na conexão, mostrar uma mensagem de falha.
"""

import requests

def buscar_usuario():
    url = "https://randomuser.me/api/"

    try:
        resposta = requests.get(url)  # Faz a requisição
        
        # Se a resposta NÃO for 200 (OK), lança erro
        resposta.raise_for_status()

        dados = resposta.json()

        # Acessando os dados do usuário
        usuario = dados["results"][0]

        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario["email"]
        pais = usuario["location"]["country"]

        print("=== Usuário Encontrado ===")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException:
        print("❌ Falha ao acessar a API. Verifique sua conexão ou tente mais tarde.")


# Chamando a função
buscar_usuario()