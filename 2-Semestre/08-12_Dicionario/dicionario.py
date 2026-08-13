import pandas as pd

dicionario = {
    'time': ['São Paulo', 'Cortinas', 'Paumeiras'],
    'vitorias': [5, 0, 4],
    'estado': ['SP', 'SP', 'SP']
}

print("\033[H\033[J", end="") # Dá um cls no console
print(dicionario)


dados = pd.DataFrame(dicionario)
print(dados)