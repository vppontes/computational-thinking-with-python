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

# normal
total = []

for i in range(len(df)):
    total.append(float(df['preco'][i] * df['qtd'][i]))

print(*total, sep='\n')
# * "desempacota" a lista, colocando os itens separados apenas por espaço por padrão
# sep é como posso separar estes itens

df['total'] = df['preco'] * df['qtd']
# pandas facilita por nao precisar usar o laço de repetição

print(df[['preco', 'qtd', 'total']])

# normal
lista_acima = []
for i in range(len(df)):
    if df["total"][i] > 1000:
        lista_acima.append(float(df["total"][i]))

print(*lista_acima, sep='\n')

# com pandas
mask = df["total"] > 1000
valores_acima = df[mask]

print(valores_acima)

# 2 - criando um novo DataFrame
df1 = df[df["total"] > 1000]
print(f'\n{df1}')

print('\n')

# outro
print(df['produto'].value_counts())