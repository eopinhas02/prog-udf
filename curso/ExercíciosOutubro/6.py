# Programa: Tarefa 6
# Descrição:
# Solicita uma quantidade indefinida de números positivos (para quando for digitado um número negativo)
# Armazena todos os números digitados em uma lista, sem repetição.

nome = "Tarefa 6"
numero = 6

def coletar_numeros_unicos():
    numeros = []     # lista que vai guardar os números sem repetição
    vistos = set()   # conjunto para verificar duplicatas rapidamente

    while True:
        try:
            valor = float(input("Digite um número positivo (ou negativo para parar): "))
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
            continue

        if valor < 0:
            print("\nNúmero negativo detectado. Encerrando a entrada de dados.")
            break

        if valor not in vistos:
            numeros.append(valor)
            vistos.add(valor)
        else:
            print(f"O número {valor} já foi digitado. Não será adicionado novamente.")

    return numeros


def main():
    print(f"\nPrograma: {nome}  |  Número: {numero}\n")
    lista_final = coletar_numeros_unicos()
    print("\nNúmeros digitados (sem repetição):")
    for n in lista_final:
        if n.is_integer():
            print(int(n))
        else:
            print(n)


if __name__ == "__main__":
    main()
