# Tarefa 7 - Verificar se há pessoas com mesma altura e peso

def tarefa7():
    pessoas = []
    for i in range(5):
        nome = input(f"Nome da pessoa {i+1}: ").strip() or f"Pessoa{i+1}"
        altura = float(input(f"Altura de {nome} (em metros): ").replace(",", "."))
        peso = float(input(f"Peso de {nome} (em kg): ").replace(",", "."))
        pessoas.append({"nome": nome, "altura": altura, "peso": peso})

    iguais = []
    for i in range(len(pessoas)):
        for j in range(i + 1, len(pessoas)):
            if pessoas[i]["altura"] == pessoas[j]["altura"] and pessoas[i]["peso"] == pessoas[j]["peso"]:
                iguais.append((pessoas[i]["nome"], pessoas[j]["nome"]))

    if iguais:
        print("Existem pessoas com mesma altura e peso:")
        for par in iguais:
            print(f"{par[0]} e {par[1]}")
    else:
        print("Nenhuma pessoa tem a mesma altura e peso.")

if __name__ == "__main__":
    tarefa7()
