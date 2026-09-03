import pandas as pd

dicionario = {
    'Pontos A': [10, 20, 30, 40, 50],
    'Pontos B': [100, 200, 300, 400, 500],
    'Pontos C': [1, 2, 3, 4, 5]
}

df1 = pd.DataFrame(dicionario)
print(df1)

def classificar(a):
    if a >= 20:
        return f'{a} baixo'
    elif a >= 30:
        return f'{a} médio'
    else:
        return f'{a} alto'

print(df1['Pontos A'].apply(classificar))