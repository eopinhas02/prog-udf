# Tarefa 4 - Ler notas indefinidamente e calcular a média

def tarefa4():
    notas = []
    print("Digite as notas (digite um número negativo para encerrar):")
    while True:
        try:
            nota = float(input("Nota: ").replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número.")
            continue
        if nota < 0:
            break
        notas.append(nota)

    if len(notas) == 0:
        print("Nenhuma nota informada.")
    else:
        media = sum(notas) / len(notas)
        print(f"Notas: {notas}")
        print(f"Média: {media:.2f}")

if __name__ == "__main__":
    tarefa4()
