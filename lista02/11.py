
nome1 = input("Digite o nome da primeira pessoa: ")
peso1 = float(input("Digite o peso da primeira pessoa: "))
nome2 = input("Digite o nome da segunda pessoa: ")
peso2 = float(input("Digite o peso da segunda pessoa: "))

if peso1 > peso2:
    print(f"A pessoa mais pesada é {nome1}")
elif peso2 > peso1:
    print(f"A pessoa mais pesada é {nome2}")
else:
    print("As duas pessoas têm o mesmo peso")
