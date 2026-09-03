import pandas as pd

class Carro:
    def __init__(self, marca, modelo, tipo, cor, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.cor = cor
        self.ano = ano

carro1 = Carro('Toyota', 'Yaris', 'Sedan', 'Vermelho', 2012)
carro2 = Carro('Fiat', 'Argo', 'Hatch', 'Branco', 2021)
carro3 = Carro('Chevrolet', 'Spin', 'Perua', 'Verde Claro', 2027)

garagem = {
    'Carro1': carro1.__dict__,
    'Carro2': carro2.__dict__,
    'Carro3': carro3.__dict__,
}

df = pd.DataFrame(garagem)

def idade(ano: int):
    if ano < 2020:
        return 'velho'
    else:
        return 'novo'

df.loc['classificacao'] = df.loc['ano'].apply(idade)

print(df)