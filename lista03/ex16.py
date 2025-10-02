idades = []
while True:
    idade = int(input())
    idades.append(idade)
    cont = input().upper()
    if cont == "N":
        break
mais_novo = min(idades)
mais_velho = max(idades)
maiores_18 = sum(1 for i in idades if i > 18)
menores_18 = sum(1 for i in idades if i <= 18)
media = sum(idades) / len(idades)
idades.sort()
n = len(idades)
if n % 2 == 0:
    mediana = (idades[n//2 - 1] + idades[n//2]) / 2
else:
    mediana = idades[n//2]
print(mais_novo)
print(mais_velho)
print(maiores_18)
print(menores_18)
print(media)
print(mediana)