numeros = []
while True:
    num = float(input())
    if num == 0:
        break
    numeros.append(num)
numeros.sort()
print(numeros)