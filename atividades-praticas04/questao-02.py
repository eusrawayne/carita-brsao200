"""
2 - Criar um código que registre as notas de alunos e calcule a média da turma.
"""

def media_turma():
    print("=== Registro de Notas ===")

    qtd_alunos = int(input("Quantos alunos serão cadastrados? "))

    soma_notas = 0  # Acumula as notas

    for i in range(qtd_alunos):
        nota = float(input(f"Digite a nota do aluno {i + 1}: "))
        soma_notas += nota

    media = soma_notas / qtd_alunos

    return f"A média da turma é: {media:.2f}"


print(media_turma())
