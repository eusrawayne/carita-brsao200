"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
def celsius_to_kelvin(c):
    return c + 273.15
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9                       
def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15
def kelvin_to_celsius(k):
    return k - 273.15
def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32
temp = float(input("Digite a temperatura a ser convertida: "))
unidade_origem = input("Digite a unidade de origem (C, F, K): ").upper()
unidade_destino = input("Digite a unidade de destino (C, F, K): ").upper()
if unidade_origem == "C":
    if unidade_destino == "F":
        resultado = celsius_to_fahrenheit(temp)
    elif unidade_destino == "K":
        resultado = celsius_to_kelvin(temp)
    else:
        resultado = temp
elif unidade_origem == "F":
    if unidade_destino == "C":
        resultado = fahrenheit_to_celsius(temp)
    elif unidade_destino == "K":
        resultado = fahrenheit_to_kelvin(temp)
    else:
        resultado = temp
elif unidade_origem == "K":
    if unidade_destino == "C":
        resultado = kelvin_to_celsius(temp)
    elif unidade_destino == "F":
        resultado = kelvin_to_fahrenheit(temp)
    else:
        resultado = temp
else:
    print("Unidade de origem inválida.")
    resultado = None
if resultado is not None:
    print(f"{temp}°{unidade_origem} é igual a {round(resultado, 2)}°{unidade_destino}")
# Fim do código