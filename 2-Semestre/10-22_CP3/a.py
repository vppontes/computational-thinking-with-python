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
print((vendas['nivel'] == vendas['nivel2']).all())

# Aplique a função na coluna `preco` para criar a coluna `faixa` e use `value_counts()` para contar quantos produtos há em cada faixa.

# **Resultado esperado:** 4 produtos em cada faixa (Barato, Médio e Caro).

def faixa_preco(preco):
    if preco < 200:
        faixa = 'Barato'
    elif 200 <= preco <= 1000:
        faixa = 'Médio'
    else:
        faixa = 'Caro'
    return faixa

vendas['faixa'] = vendas['preco'].apply(faixa_preco)

print(vendas['faixa'].value_counts())

# A loja vai dar **10% de desconto** nos pedidos que atendem **às duas** condições:
# - categoria `"Informatica"` **e**
# - `qtd` ≥ 2.

# Os demais pedidos têm desconto 0.

# 1. Crie a coluna `desconto` (em reais) com `apply(..., axis=1)` e uma `lambda` que olha para a linha inteira.
# 2. Crie a coluna `total_final` = `total` − `desconto`.
# 3. Mostre apenas os pedidos que receberam desconto e o valor total de descontos concedidos.

condicoes = lambda linha: 0.1 * linha['total'] if (linha['categoria'] == 'Informatica' and linha['qtd'] >= 2) else 0

vendas['desconto'] = vendas.apply(condicoes, axis=1)
vendas['total_final'] = vendas['total'] - vendas['desconto']

pedidos_com_desconto = []
desconto_pedido = 0

for pedido, desconto in zip(vendas['pedido'], vendas['desconto']):
    if desconto > 0:
        pedidos_com_desconto.append(pedido)
        desconto_pedido += desconto

print(f'{len(pedidos_com_desconto)} pedidos com desconto {pedidos_com_desconto}; total de descontos: R$ {desconto_pedido:.2f}')

regioes = ["SP", "RJ", "MG"]
metas   = [15000, 12000, 5000]

# 1. Use `zip` para criar o dicionário `meta_por_regiao` (`{"SP": 15000, ...}`).
# 2. Crie a coluna `meta_regiao` em `vendas` usando `.map()` com esse dicionário.
# 3. Mostre `pedido`, `regiao` e `meta_regiao` das 5 primeiras linhas.

# **Resultado esperado:** `{'SP': 15000, 'RJ': 12000, 'MG': 5000}`

meta_por_regiao = dict(zip(regioes, metas))

vendas['meta_regiao'] = vendas['regiao'].map(meta_por_regiao)

print(vendas[['regiao', 'meta_regiao']].head(5))

alertas = 0
for produto, qtd, regiao in zip(vendas['produto'], vendas['qtd'], vendas['regiao']):
    if qtd < 3:
        print(f'ATENÇÃO:\t{produto} ({regiao})\tvendeu só\t{qtd} unidade(s)')
        alertas += 1

print(f'{alertas} alertas gerados')

contagem = {}
for regiao, qtd in zip(vendas['regiao'], vendas['qtd']):
    if regiao not in contagem:
        contagem[regiao] = 0
    contagem[regiao] += 1

print(contagem)
print(vendas['regiao'].value_counts())

cadastro = pd.DataFrame({
    "cliente_bruto": ["  ana souza", "BRUNO LIMA ", "carla   dias", "Diego rocha", " elisa PRADO"]
})

condicao = lambda cliente: " ".join(cliente.split()).title()
cadastro['cliente'] = cadastro['cliente_bruto'].apply(condicao)

print(f'{cadastro["cliente"].isin(vendas['cliente']).all()} - os cinco nomes limpos existem em vendas')

### Exercício 11 – Condição vetorizada: máscaras com `&`, `|` e `~`
# *Temas: DataFrame · condição*

# Sem usar `for` nem `apply`, responda com **máscaras booleanas**:

# 1. Quais pedidos são de **SP** **e** têm `total` > 1000?
# 2. Quais pedidos são de **RJ** **ou** da categoria **Acessorio**? (quantos são?)
# 3. Quais pedidos **não** são de Informatica e têm `qtd` ≥ 5?

# Mostre para cada item as colunas `pedido`, `produto`, `regiao`, `categoria`, `qtd` e `total`.

# *Lembrete:* cada condição vai entre parênteses.

# **Resultado esperado:** 1) 3 pedidos (1001, 1003, 1011) · 2) 8 pedidos · 3) 3 pedidos (1002, 1004, 1010).

lista_mascara1 = []
mascara1 = (vendas['regiao'] == 'SP') & (vendas['total'] > 1000)
for pedido in vendas[mascara1]['pedido']:
    lista_mascara1.append(pedido)

lista_mascara2 = []
mascara2 = (vendas['regiao'] == 'RJ') | (vendas['categoria'] == 'Acessorio')
for pedido in vendas[mascara2]['pedido']:
    lista_mascara2.append(pedido)

lista_mascara3 = []
mascara3 = (vendas['categoria'] != 'Informatica') & (vendas['qtd'] >= 5)
for pedido in vendas[mascara3]['pedido']:
    lista_mascara3.append(pedido)

print(f'1) {len(lista_mascara1)} pedidos {lista_mascara1} · 2) {len(lista_mascara2)} pedidos · 3) {len(lista_mascara3)} pedidos {lista_mascara3}')

