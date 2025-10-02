qtd = int(input())
soma_m = soma_f = 0
cont_m = cont_f = 0
for i in range(qtd):
    sexo = input().upper()
    idade = int(input())
    if sexo == "M":
        soma_m += idade
        cont_m += 1
    elif sexo == "F":
        soma_f += idade
        cont_f += 1
if cont_m > 0:
    print(soma_m / cont_m)
if cont_f > 0:
    print(soma_f / cont_f)