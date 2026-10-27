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

# ### Exercício 12 – `for` sobre `groupby` com `if` (meta batida?)
# *Temas: for · groupby · condição*

# Usando o dicionário `meta_por_regiao` do Exercício 7:

# Percorra `vendas.groupby("regiao")` com `for regiao, grupo in ...`. Para cada região:
# - calcule o faturamento (`total` somado) do grupo;
# - compare com a meta e imprima `"META BATIDA"` ou `"abaixo da meta (faltam R$ X)"`.

# Formato sugerido:
# `SP: R$ 15,379.60 / meta R$ 15,000 -> META BATIDA`

# *(o formato `:,.2f` do Python usa vírgula para milhar e ponto para decimal)*

# > 🔗 Usa colunas/variáveis criadas no Exercício 7.

# **Resultado esperado:** Só SP bate a meta (R$ 15,379.60). MG faltam R$ 2,740.00 e RJ faltam R$ 3,735.00.

for regiao, grupo in vendas.groupby('regiao'):
    faturamento = grupo['total'].sum()
    meta = meta_por_regiao[regiao]
    if faturamento >= meta:
        print(f'{regiao}: R$ {faturamento:,.2f} / meta R$ {meta:,.2f} -> META BATIDA')
    else:
        faltam = meta - faturamento
        print(f'{regiao}: R$ {faturamento:,.2f} / meta R$ {meta:,.2f} -> abaixo da meta (faltam R$ {faltam:,.2f})')

### Exercício 13 – Ranking com `enumerate` + `zip`
# *Temas: for · zip · enumerate · DataFrame*

# Monte o **Top 5** de pedidos por `total`:

# 1. Ordene `vendas` por `total` em ordem decrescente e pegue as 5 primeiras linhas.
# 2. Com `for posicao, (cliente, produto, total) in enumerate(zip(...), start=1)`, imprima:
#    `1º Ana Souza - Notebook - R$ 8400.00`
# 3. Acrescente uma medalha: 🥇 para o 1º, 🥈 para o 2º, 🥉 para o 3º e nada para os demais (use `if/elif`).

# > 🔗 Usa colunas/variáveis criadas no Exercício 2.

# **Resultado esperado:** 1º Ana Souza - Notebook - R$ 8400.00 … 5º Elisa Prado - SSD - R$ 1350.00.

# Não lembro de ter sido mostrado em aula o sort_values mas é uma forma mais fácil de ordenar um DF sem ter que usar for e ifs.
top5 = vendas.sort_values(by='total', ascending=False).head(5)

for posicao, (cliente, produto, total) in enumerate(zip(top5['cliente'], top5['produto'], top5['total']), start=1):
    if posicao == 1:
        medalha = '🥇'
    elif posicao == 2:
        medalha = '🥈'
    elif posicao == 3:
        medalha = '🥉'
    else:
        medalha = ''
    print(f'{posicao}º {cliente} - {produto} - R$ {total:.2f} {medalha}')

### Exercício 14 – Frete com list comprehension + `zip` + condição
# *Temas: zip · condição · list comprehension*

# Regras de frete:
# - Pedidos com `total` ≥ 2000 têm **frete grátis** (0).
# - Os demais pagam o frete da tabela da região:

# ```python
# frete_tabela = {"SP": 25.0, "RJ": 35.0, "MG": 40.0}
# ```

# Crie a coluna `frete` com **uma única list comprehension** que percorre `zip(vendas["regiao"], vendas["total"])`.
# Mostre `pedido`, `regiao`, `total`, `frete` e informe quantos pedidos ganharam frete grátis.

# > 🔗 Usa colunas/variáveis criadas no Exercício 2.

# **Resultado esperado:** 4 pedidos com frete grátis.

frete_tabela = {"SP": 25.0, "RJ": 35.0, "MG": 40.0}

vendas['frete'] = [0 if total >= 2000 else frete_tabela[regiao] for regiao, total in zip(vendas['regiao'], vendas['total'])]

frete_gratis = vendas[vendas['frete'] == 0]

print(f"{len(frete_gratis)} pedidos com frete grátis")

### Exercício 15 – Gerando textos com `apply(axis=1)` + `lambda`
# *Temas: apply · lambda · f-string*

# Crie a coluna `resumo` com uma frase para cada pedido, no formato:

# `Ana Souza comprou 2x Notebook em SP`

# Use `apply` com `axis=1` e uma `lambda` com f-string. Mostre a coluna `resumo` dos 4 primeiros pedidos.

# **Extra:** quando `qtd` for 1, a frase deve ficar `comprou 1 Notebook` (sem o "x"). Resolva com expressão condicional dentro da própria lambda.

# **Resultado esperado:** `Bruno Lima comprou 10x Mouse em RJ`; para o pedido 1005: `Diego Rocha comprou 1 Notebook em RJ`.

condicao = lambda x: f'{x['cliente']} comprou {x['qtd']}x {x['produto']} em {x['regiao']}' if x['qtd'] > 1 else f'{x['cliente']} comprou 1 {x['produto']} em {x['regiao']}'

vendas['resumo'] = vendas.apply(condicao, axis=1)

print(vendas['resumo'].head(4))

### Exercício 16 – Função com parâmetros extras no `apply`
# *Temas: def · apply · lambda · condição*

# A loja vai reajustar preços **por categoria**. Escreva a função

# ```python
# def reajustar(preco, categoria, pct_info, pct_acess):
# ```

# que devolve o preço com aumento de `pct_info`% se a categoria for `"Informatica"` e de `pct_acess`% caso contrário, arredondado em 2 casas.

# Use `apply(axis=1)` com uma `lambda` que chama `reajustar` passando **5%** para Informatica e **8%** para Acessorio, criando a coluna `preco_novo`.
# Mostre `produto`, `categoria`, `preco` e `preco_novo` sem repetir produtos (`drop_duplicates("produto")`).

# **Resultado esperado:** 8 produtos; Notebook 4200.00 → 4410.00, Mouse 89.90 → 97.09.

def reajustar(preco, categoria, pct_info, pct_acess):
    if categoria == "Informatica":
        preco_novo = preco * (1 + pct_info / 100)
    else:
        preco_novo = preco * (1 + pct_acess / 100)
    return round(preco_novo, 2)

vendas['preco_novo'] = vendas.apply(lambda x: reajustar(x['preco'], x['categoria'], 5, 8), axis=1)

print(vendas[['produto', 'categoria', 'preco', 'preco_novo']].drop_duplicates('produto'))

### Exercício 17 – Acumulador com `for` + `break`
# *Temas: for · condição · acumulador*

# A empresa quer saber **em que data** o faturamento de setembro ultrapassou **R$ 20.000**.

# 1. Ordene `vendas` pela coluna `data`.
# 2. Percorra `data`, `pedido` e `total` com `for` + `zip`, somando os totais em uma variável `acumulado` e imprimindo o acumulado a cada pedido.
# 3. Assim que `acumulado` ≥ 20000, imprima a data e o pedido que bateram a marca e **interrompa** o laço com `break`.

# > 🔗 Usa colunas/variáveis criadas no Exercício 2.

# **Resultado esperado:** Marca atingida em 11/09/2026 com o pedido 1008 (acumulado R$ 20,608.60).

acumulado = 0

vendas_ordenadas = vendas.sort_values('data')

for data, pedido, total in zip(
    vendas_ordenadas['data'],
    vendas_ordenadas['pedido'],
    vendas_ordenadas['total']
):
    acumulado += total
    print(f'Acumulado: R$ {acumulado:.2f}')
    if acumulado >= 20000:
        print(f'Marca atingida em {data:%d-%m-%Y} com o pedido {pedido} (acumulado R$ {acumulado:.2f})')
        break

### Exercício 18 – Comparando duas colunas com `zip` (subiu, caiu ou igual)
# *Temas: zip · for · condição · DataFrame*

# O fornecedor mandou a nova tabela de custos. Compare custo antigo e novo:

# ```python
# custos = pd.DataFrame({
#     "produto":     ["Notebook", "Mouse", "Monitor", "Teclado", "Webcam", "Headset", "Impressora", "SSD"],
#     "custo_antigo": [3100.0, 45.0, 900.0, 120.0, 80.0, 190.0, 610.0, 280.0],
#     "custo_novo":   [3250.0, 45.0, 870.0, 135.0, 80.0, 175.0, 655.0, 260.0],
# })
# ```

# 1. Com `for` + `zip` sobre `custo_antigo` e `custo_novo`, monte a lista `situacao` com `"subiu"`, `"caiu"` ou `"igual"` e grave na coluna de mesmo nome.
# 2. Crie a coluna `variacao_pct` com `apply` + `lambda` (axis=1), arredondada em 1 casa.
# 3. Mostre o DataFrame e a contagem de cada situação.

# **Resultado esperado:** subiu 3 · caiu 3 · igual 2; Teclado tem a maior alta (12.5%).

custos = pd.DataFrame({
    "produto":     ["Notebook", "Mouse", "Monitor", "Teclado", "Webcam", "Headset", "Impressora", "SSD"],
    "custo_antigo": [3100.0, 45.0, 900.0, 120.0, 80.0, 190.0, 610.0, 280.0],
    "custo_novo":   [3250.0, 45.0, 870.0, 135.0, 80.0, 175.0, 655.0, 260.0],
})

situacao = []

for antigo, novo in zip(custos['custo_antigo'], custos['custo_novo']):
    if novo > antigo:
        situacao.append('subiu')
    elif novo < antigo:
        situacao.append('caiu')
    else:
        situacao.append('igual')

custos['situacao'] = situacao

condicao = lambda x: round((x['custo_novo'] - x['custo_antigo']) / x['custo_antigo'] * 100, 1)

custos['variacao_pct'] = custos.apply(condicao, axis=1)

print(custos)

### Exercício 19 – `lambda` aplicada a grupos
# *Temas: groupby · apply · lambda · condição*

# Para cada **categoria**, calcule com `groupby(...)["total"].apply(lambda ...)`:

# 1. a **amplitude** dos totais (maior total − menor total);
# 2. a **proporção de pedidos acima de R$ 1.000** (em %, 1 casa decimal).

# Junte os dois resultados em um DataFrame `analise` com as colunas `amplitude` e `pct_acima_1000`.

# Depois, adicione a coluna `perfil`, com `apply` + `lambda` sobre `pct_acima_1000`: `"ticket alto"` se for maior que 50, senão `"ticket baixo"`.

# > 🔗 Usa colunas/variáveis criadas no Exercício 2.

# **Resultado esperado:** Acessorio: amplitude 480.0, 16.7%, ticket baixo · Informatica: amplitude 7420.0, 83.3%, ticket alto.

condicao_lambda = lambda x: x.max() - x.min()

amplitude = vendas.groupby('categoria')['total'].apply(condicao_lambda)

condicao_pct = lambda x: round((x > 1000).sum() / len(x) * 100, 1)

pct_acima_1000 = vendas.groupby('categoria')['total'].apply(condicao_pct)

analise = pd.DataFrame({
    'amplitude': amplitude,
    'pct_acima_1000': pct_acima_1000
})

condicao_perfil = lambda x: 'ticket alto' if x > 50 else 'ticket baixo'

analise['perfil'] = analise['pct_acima_1000'].apply(condicao_perfil)

print(analise)