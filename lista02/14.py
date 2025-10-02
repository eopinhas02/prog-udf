
media_aprov = float(input("Digite a média mínima para aprovação: "))
nome = input("Digite o nome do aluno: ")
sexo = input("Digite o sexo do aluno (M/F): ").upper()
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))

media = (n1 + n2 + n3) / 3

if media >= media_aprov:
    if sexo == "M":
        print(f"O aluno {nome} foi aprovado com média {media:.2f}")
    else:
        print(f"A aluna {nome} foi aprovada com média {media:.2f}")
else:
    if sexo == "M":
        print(f"O aluno {nome} foi reprovado com média {media:.2f}")
    else:
        print(f"A aluna {nome} foi reprovada com média {media:.2f}")
