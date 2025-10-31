# Tarefa 1 - Ler 5 números inteiros e armazenar em uma lista

def tarefa1():
    numeros = []
    for i in range(5):
        while True:
            try:
                n = int(input(f"Digite o {i+1}º número inteiro: "))
                numeros.append(n)
                break
            except ValueError:
                print("Valor inválido, tente novamente.")
    print(f"Lista final: {numeros}")

if __name__ == "__main__":
    tarefa1()
