"""
4 - Criar um código que serve para analisar números digitados pelo usuário,
classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.
"""

def analisar_numeros():
    pares = 0
    impares = 0

    print("Digite números para analisar. Digite 'sair' para encerrar.\n")

    while True:
        numero = input("Digite um número: ")

        if numero.lower() == "sair":
            break

        # Verifica se digitou algo que pode ser número
        if not numero.isdigit() and not (numero.startswith('-') and numero[1:].isdigit()):
            print("Entrada inválida! Digite apenas números ou 'sair'.")
            continue

        numero = int(numero)

        if numero % 2 == 0:
            pares += 1
            print(f"{numero} é par.")
        else:
            impares += 1
            print(f"{numero} é ímpar.")

    print("\n===== RESULTADO FINAL =====")
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")


# Chamando a função
analisar_numeros()

