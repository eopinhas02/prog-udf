# Tarefa 8 - Ler nome e idade de várias pessoas e mostrar a mais velha

def tarefa8():
    mais_velho_nome = None
    mais_velho_idade = -1

    while True:
        nome = input("Nome (vazio para encerrar): ").strip()
        if not nome:
            break
        idade = int(input(f"Idade de {nome}: "))
        if idade > mais_velho_idade:
            mais_velho_nome = nome
            mais_velho_idade = idade

    if mais_velho_nome:
        print(f"A pessoa mais velha é {mais_velho_nome} com {mais_velho_idade} anos.")
    else:
        print("Nenhuma pessoa informada.")

if __name__ == "__main__":
    tarefa8()
