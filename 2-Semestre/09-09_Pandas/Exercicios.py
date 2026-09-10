import pandas as pd
 
df = pd.DataFrame({
    "pedido":    [1001, 1002, 1003, 1004, 1005, 1006],
    "produto":   ["Notebook", "Mouse", "Monitor",
                  "Teclado", "Notebook", "Webcam"],
    "categoria": ["Informatica", "Acessorio",
                  "Informatica", "Acessorio",
                  "Informatica", "Acessorio"],
    "regiao":    ["SP", "RJ", "SP", "MG", "RJ", "SP"],
    "preco":     [4200.0, 89.9, 1350.0,
                  210.0, 3990.0, 149.9],
    "qtd":       [2, 10, 3, 5, 1, 4],
})

df['total'] = df['preco'] * df['qtd']

# Exercícios

# 1. Crie um filtro para trazer apeans informações do RJ.
# 2. Crie um filtro para trazer apenas as informações de produtos de informática.
# 3. Crie um filtro para selecionar valores de Total > 1000 apenas para SP.
# 4. Como criar um filtro utilizando duas variáveis (colunas)?

rj = df['regiao'] == 'RJ'
regiao = df[rj]
print(regiao)

print('\n')

info = df['categoria'] == 'Informatica'
categoria = df[info]
print(categoria)

print('\n')

filtro = (df['regiao'] == 'SP') & (df['total'] > 1000)
filtragem = df[filtro]
print(filtragem)

print('\n')