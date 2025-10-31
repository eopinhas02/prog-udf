# Tarefa 2 - Dicionário de animes: calcular percentuais e exibir ordenado

def tarefa2():
    animes = {
        "Naruto": 220,
        "Jujutsu Kaisen": 47,
        "Dragon Ball Z": 291,
        "Fullmetal Alchemist": 64,
        "Evangelion": 26,
        "Berserk": 25,
        "Code Geass": 50,
        "Akame ga Kill!": 24
    }

    total = sum(animes.values())
    print(f"Total de episódios: {total}\n")

    for nome, qtd in animes.items():
        animes[nome] = (qtd / total) * 100

    ordenado = sorted(animes.items(), key=lambda x: x[1], reverse=True)
    print("Percentual de episódios por anime:")
    for nome, pct in ordenado:
        print(f"{nome}: {pct:.2f}%")

if __name__ == "__main__":
    tarefa2()
