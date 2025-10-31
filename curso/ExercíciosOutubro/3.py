# Tarefa 3 - Dicionário de bandas e álbuns

bandas = {
    "Gangrena Gasosa": [
        {"álbum": "Gente Ruim Só Manda Lembrança Pra Quem Não Presta", "ano": 2019},
        {"álbum": "Se Deus É 10, Satã é 666", "ano": 1999},
        {"álbum": "Welcome to the Macumba", "ano": 1995},
    ],
    "Rogério Skylab": [
        {"álbum": "Nas Portas do Cu", "ano": 2023},
        {"álbum": "Crítica da Faculdade do Cu", "ano": 2021},
        {"álbum": "Cosmos", "ano": 2019},
    ],
    "Garotos Podres": [
        {"álbum": "Canções para Ninar", "ano": 2003},
        {"álbum": "Com a Corda Toda", "ano": 1997},
        {"álbum": "Rock de Subúrbio", "ano": 1995},
    ],
    "Massacration": [
        {"álbum": "Live Metal Espancation", "ano": 2017},
        {"álbum": "Good Blood Headbangers", "ano": 2009},
        {"álbum": "Gates of Metal Fried Chicken of Death", "ano": 2005},
    ],
    "Raimundos": [
        {"álbum": "Cantigas de Roda", "ano": 2014},
        {"álbum": "Roda Viva", "ano": 2006},
        {"álbum": "Éramos 4", "ano": 2001},
    ]
}

def tarefa3():
    mais_antigo = None
    banda_mais_antiga = None

    for banda, albuns in bandas.items():
        for album in albuns:
            if mais_antigo is None or album["ano"] < mais_antigo["ano"]:
                mais_antigo = album
                banda_mais_antiga = banda

    print(f"\n➡️ Álbum mais antigo: '{mais_antigo['álbum']}' ({mais_antigo['ano']}) da banda {banda_mais_antiga}")

    maior_intervalo = 0
    banda_maior_intervalo = None

    for banda, albuns in bandas.items():
        anos = [a["ano"] for a in albuns]
        intervalo = max(anos) - min(anos)
        if intervalo > maior_intervalo:
            maior_intervalo = intervalo
            banda_maior_intervalo = banda

    print(f"➡️ Banda com maior intervalo entre álbuns: {banda_maior_intervalo} ({maior_intervalo} anos)")

    todos_albuns = []
    for banda, albuns in bandas.items():
        for album in albuns:
            todos_albuns.append({"banda": banda, "álbum": album["álbum"], "ano": album["ano"]})

    ordenados = sorted(todos_albuns, key=lambda x: x["ano"], reverse=True)

    print("\n➡️ Todos os álbuns do mais novo para o mais antigo:")
    for item in ordenados:
        print(f"{item['ano']} - {item['banda']}: {item['álbum']}")

if __name__ == "__main__":
    tarefa3()
