
p1 = float(input("Digite a nota da primeira prova: "))
p2 = float(input("Digite a nota da segunda prova: "))
p3 = float(input("Digite a nota da terceira prova: "))
media = (p1*2 + p2*3 + p3*5) / 10
if media >= 6:
    print(f"Aprovado com média {media:.2f}")
else:
    print(f"Reprovado com média {media:.2f}")
