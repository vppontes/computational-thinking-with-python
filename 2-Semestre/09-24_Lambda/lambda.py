import requests
import pandas as pd

# 1) Endereço da API (endpoint)
url = "https://api.open-meteo.com/v1/forecast"

# 2) As 10 variáveis que queremos
variaveis = [
    "temperature_2m",             # temperatura do ar (°C)
    "apparent_temperature",       # sensação térmica (°C)
    "relative_humidity_2m",       # umidade relativa (%)
    "precipitation",              # chuva acumulada na hora (mm)
    "precipitation_probability",  # probabilidade de chuva (%)
    "cloud_cover",                # cobertura de nuvens (%)
    "wind_speed_10m",             # velocidade do vento (km/h)
    "wind_direction_10m",         # direção do vento (°)
    "pressure_msl",               # pressão ao nível do mar (hPa)
    "uv_index",                   # índice UV
]

# 3) Parâmetros da requisição: local, variáveis e fuso horário
params = {
    "latitude": -23.55,           # São Paulo
    "longitude": -46.63,
    "hourly": ",".join(variaveis),
    "timezone": "America/Sao_Paulo",
}

# 4) Chamada à API
resp = requests.get(url, params=params, timeout=10)
resp.raise_for_status()           # para o programa se a API retornar erro
dados = resp.json()               # converte a resposta JSON em dicionário Python

# 5) Transformar em DataFrame
df = pd.DataFrame(dados["hourly"])
df["time"] = pd.to_datetime(df["time"])

# 6) (Opcional) Renomear as colunas para português
df = df.rename(columns={
    "time": "data_hora",
    "temperature_2m": "temperatura",
    "apparent_temperature": "sensacao_termica",
    "relative_humidity_2m": "umidade",
    "precipitation": "chuva_mm",
    "precipitation_probability": "prob_chuva",
    "cloud_cover": "nuvens",
    "wind_speed_10m": "vento_kmh",
    "wind_direction_10m": "vento_direcao",
    "pressure_msl": "pressao",
    "uv_index": "indice_uv",
})

df

# Exercícios 

# 1. Crie uma estrutura para calcular/retornar os valores min, max, media e mediana das colunas "temperatura", "sensacao_termica", "umidade", "chuva_mm".

# a. Utilize uma estrutura com repetição.

colunas = ["temperatura", "sensacao_termica", "umidade", "chuva_mm"]

for i in colunas:
    print(f'Coluna: {i}')
    print(f'Min: {df[i].min()}')
    print(f'Max: {df[i].max()}')
    print(f'Média: {df[i].mean()}')
    print(f'Mediana: {df[i].mean()}')
# _________________________________________________________________

# b. Utilize uma estrutura com pandas.

print(df["temperatura"].min())
print(df["temperatura"].max())
print(df["temperatura"].mean())
print(df["temperatura"].median())

print(df["sensacao_termica"].min())
print(df["sensacao_termica"].max())
print(df["sensacao_termica"].mean())
print(df["sensacao_termica"].median())

print(df["umidade"].min())
print(df["umidade"].max())
print(df["umidade"].mean())
print(df["umidade"].median())

print(df["chuva_mm"].min())
print(df["chuva_mm"].max())
print(df["chuva_mm"].mean())
print(df["chuva_mm"].median())
# __________________________________________________________________

# c. Utilize uma estrutura com lambda. 

colunas = ["temperatura", "sensacao_termica", "umidade", "chuva_mm"]

funcoes = {
    'min': lambda x: x.min(),
    'max': lambda x: x.max(),
    'mean': lambda x: x.mean(),
    'median': lambda x: x.median()
    }

for coluna in colunas:
  print(f'Coluna: {coluna}')
  for nome_funcao, funcao in funcoes.items():
    resultado = funcao(df[coluna])
    print(f'{nome_funcao}: {resultado}')

# Abordagem 4 - Utilizando a função agg() em python

colunas = ["temperatura", "sensacao_termica", "umidade", "chuva_mm"]

df[colunas].agg(["min", "max", "mean", "median"])
# __________________________________________________________________

# 2. Crie um gráfico para mostrar as curvas de 'temperatura' e 'sensacao_termica'. 

# 3. O que acontece com o gráfico ao incluir a variável pressao no mesmo gráfico?

# 4. O que fazer para resolver o problema da questão 3?

#### ----------------------------------------

funcoes = {
    'min': lambda x: x.min(),
    'max': lambda x: x.max(),
    'mean': lambda x: x.mean(),
    'median': lambda x: x.median(),
}

for coluna in colunas:
    print(f'Coluna: {coluna}')
    for nome_funcao, funcao in funcoes.items():
        resultado = funcao(df[coluna])
        print(f'{nome_funcao}: {resultado}')
        