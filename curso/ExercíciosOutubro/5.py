# Tarefa 5 - Ler números positivos e calcular porcentagem de pares e ímpares

def tarefa5():
    pares = []
    impares = []
    total = 0

    print("Digite números positivos (digite um negativo para encerrar):")
    while True:
        try:
            n = int(input("Número: "))
        except ValueError:
            print("Valor inválido. Tente novamente.")
            continue
        if n < 0:
            break
        total += 1
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)

    if total == 0:
        print("Nenhum número positivo informado.")
        return

    pct_pares = (len(pares) / total) * 100
    pct_impares = (len(impares) / total) * 100

    print(f"Pares: {pares}")
    print(f"Ímpares: {impares}")
    print(f"Porcentagem de pares: {pct_pares:.2f}%")
    print(f"Porcentagem de ímpares: {pct_impares:.2f}%")

if __name__ == "__main__":
    tarefa5()
