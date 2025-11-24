"""
3 - Criar um código que serve para verificar se uma senha digitada pelo usuário 
atende a critérios básicos de segurança.
"""

senha = input("Digite sua senha: ")

# Critérios mínimos
tem_maiuscula = any(char.isupper() for char in senha)
tem_minuscula = any(char.islower() for char in senha)
tem_numero = any(char.isdigit() for char in senha)
tamanho_valido = len(senha) >= 8

# Verificando critérios
if tem_maiuscula and tem_minuscula and tem_numero and tamanho_valido:
    print("Senha válida! ✔")
else:
    print("Senha inválida! ❌")
    print("A senha deve conter:")
    print("- Pelo menos 1 letra maiúscula")
    print("- Pelo menos 1 letra minúscula")
    print("- Pelo menos 1 número")
    print("- Pelo menos 8 caracteres")
