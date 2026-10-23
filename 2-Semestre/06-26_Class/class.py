class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


# Criando 5 objetos
a1 = Retangulo(10, 5)
a2 = Retangulo(8, 4)
a3 = Retangulo(12, 6)
a4 = Retangulo(7, 3)
a5 = Retangulo(15, 5)


# Lista de objetos
lista_retangulo = [a1, a2, a3, a4, a5]


# Inserindo os objetos em um dicionário usando for
dicionario = {}

for i in range(len(lista_retangulo)):
    dicionario[i] = {
        "base": lista_retangulo[i].base,
        "altura": lista_retangulo[i].altura,
        "area": lista_retangulo[i].area(),
        "perimetro": lista_retangulo[i].perimetro()
    }
    i += 1

for i in range(len(dicionario)):
    print(f"{i + 1}:\tBase: {dicionario[i]['base']}\n\tAltura: {dicionario[i]['altura']}\n\tÁrea: {dicionario[i]['area']}\n\tPerímetro: {dicionario[i]['perimetro']}{'' if i == len(dicionario) - 1 else '\n'}")