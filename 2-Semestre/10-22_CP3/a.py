import pandas as pd
import numpy as np

def carregar_vendas():
    """Devolve o DataFrame base da lista (12 pedidos)."""
    return pd.DataFrame({
        "pedido":    [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012],
        "data":      pd.to_datetime(["2026-09-01", "2026-09-02", "2026-09-03", "2026-09-05",
                                     "2026-09-06", "2026-09-08", "2026-09-10", "2026-09-11",
                                     "2026-09-13", "2026-09-15", "2026-09-18", "2026-09-20"]),
        "cliente":   ["Ana Souza", "Bruno Lima", "Carla Dias", "Ana Souza", "Diego Rocha", "Bruno Lima",
                      "Carla Dias", "Elisa Prado", "Diego Rocha", "Ana Souza", "Elisa Prado", "Bruno Lima"],
        "produto":   ["Notebook", "Mouse", "Monitor", "Teclado", "Notebook", "Webcam",
                      "Headset", "Impressora", "Monitor", "Mouse", "SSD", "Teclado"],
        "categoria": ["Informatica", "Acessorio", "Informatica", "Acessorio", "Informatica", "Acessorio",
                      "Acessorio", "Informatica", "Informatica", "Acessorio", "Informatica", "Acessorio"],
        "regiao":    ["SP", "RJ", "SP", "MG", "RJ", "SP", "MG", "SP", "RJ", "MG", "SP", "RJ"],
        "preco":     [4200.0, 89.9, 1350.0, 210.0, 3990.0, 149.9, 320.0, 980.0, 1290.0, 95.0, 450.0, 199.0],
        "qtd":       [2, 10, 3, 5, 1, 4, 2, 1, 2, 6, 3, 4],
    })

vendas = carregar_vendas()
vendas

# 1. Crie a coluna `total` = `preco` × `qtd` (sem laço, de forma vetorizada).
# 2. Use um `for` com `zip` sobre as colunas `pedido` e `total` para imprimir uma linha por pedido no formato:
#    `Pedido 1001: R$ 8400.00`
# A coluna `total` será usada em todos os exercícios seguintes.

vendas['total'] = vendas['preco'] * vendas['qtd']

lista = []
for pedido, total in zip(vendas['pedido'], vendas['total']):
    if total >= 3000:
        nivel = 'Alto'
    else:
        nivel = 'Baixo'
    lista.append(nivel)

vendas['nivel'] = lista

print(vendas[['pedido', 'total', 'nivel']])

pedidos_altos = []
for pedido, nivel in zip(vendas['pedido'], vendas['nivel']):
    if nivel == 'Alto':
        pedidos_altos.append(pedido)

print(f'{len(pedidos_altos)} pedidos "Alto" {pedidos_altos}')

# ### Exercício 4 – A mesma regra com `apply` + `lambda`
# *Temas: apply · lambda · condição*

# Refaça o Exercício 3 **sem `for`**: crie a coluna `nivel2` usando `apply` com uma função `lambda` que contém uma expressão condicional (`"Alto" if ... else "Baixo"`).

# Depois, confirme com uma comparação que `nivel` e `nivel2` são idênticas (deve imprimir `True`).

# > 🔗 Usa colunas/variáveis criadas no Exercício 3.

# **Resultado esperado:** `True`
condicao = lambda x: 'Alto' if x >= 3000 else 'Baixo'

vendas['nivel2'] = vendas['total'].apply(condicao)
if vendas['nivel'].equals(vendas['nivel2']):
    print(True)
else:
    print(False)