"""
5 - Crie um programa que gere senhas aleatórias com letras, números e símbolos
e permita que o usuário escolha o tamanho da senha.
"""

import random
import string

def gerar_senha():
    print("=== GERADOR DE SENHAS SEGURAS ===")

    # Escolha do tamanho
    tamanho = input("Digite o tamanho desejado para a senha: ")

    # Verifica se digitou corretamente
    if not tamanho.isdigit():
        return "Erro: você deve digitar apenas números!"

    tamanho = int(tamanho)

    # Conjunto de caracteres possíveis
    letras = string.ascii_letters      # letras maiúsculas e minúsculas
    numeros = string.digits            # 0-9
    simbolos = string.punctuation      # símbolos como !@#$%

    # Junta tudo em um único conjunto
    todos_caracteres = letras + numeros + simbolos

    # Gera a senha aleatória
    senha = ''.join(random.choice(todos_caracteres) for _ in range(tamanho))

    return f"Sua senha gerada é: {senha}"


# Chamando a função
print(gerar_senha())
