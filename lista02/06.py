# Exercício 6
num = int(input("Digite um número inteiro: "))
multiplo = int(input("Digite o múltiplo a ser testado: "))
if num % multiplo == 0:
    print(f"{num} é múltiplo de {multiplo}")
else:
    print(f"{num} não é múltiplo de {multiplo}")
