"""
1 - Criar um código que faça uma calculadora que tenha as operações básicas (+, -, *, /).
"""

def calculadora():
    print("=== Calculadora Básica ===")
    print("Operações disponíveis:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Divisão (/)")
    print("4 - Multiplicação (*)")

    # Pede os números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Pede a operação
    operacao = input("Escolha a operação (+, -, /, *): ")

    # Calcula
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 == 0:
            return "Erro: divisão por zero não é permitida!"
        resultado = num1 / num2
    else:
        return "Operação inválida!"
    
    return f"Resultado: {resultado}"

# Chamando a função
print(calculadora())