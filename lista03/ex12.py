qtd = int(input())
mais_velho = ""
idade_mais_velho = -1
for i in range(qtd):
    nome = input()
    idade = int(input())
    if idade > idade_mais_velho:
        idade_mais_velho = idade
        mais_velho = nome
print(mais_velho, idade_mais_velho)