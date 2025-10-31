# Exercício - Dicionário de alunos e notas

def exercicio_notas():
    alunos = {
        "Alice": 8.5,
        "Bruno": 7.8,
        "Carla": 9.2,
        "Diego": 6.9,
        "Eva": 8.0,
        "Fernando": 7.5,
        "Gabriela": 9.0,
        "Henrique": 6.7,
        "Isabela": 8.3,
        "João": 7.2
    }

    qtd = len(alunos)
    notas = list(alunos.values())
    existe_zero = any(n == 0 for n in notas)
    menor = min(notas)
    maior = max(notas)

    print(f"Quantidade de alunos: {qtd}")
    print(f"Alguém tirou nota zero? {'Sim' if existe_zero else 'Não'}")
    print(f"Menor nota: {menor}")
    print(f"Maior nota: {maior}")

if __name__ == "__main__":
    exercicio_notas()
