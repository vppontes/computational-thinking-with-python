class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property
    def area(self):
        return self.base * self.altura

    @property
    def perimetro(self):
        return 2 * (self.base + self.altura)


retangulos = [
    Retangulo(10, 5),
    Retangulo(8, 4),
    Retangulo(12, 6),
    Retangulo(7, 3),
    Retangulo(15, 5)
]

for i, r in enumerate(retangulos, 1):
    print(
        f"{i}:\tBase: {r.base}\n"
        f"\tAltura: {r.altura}\n"
        f"\tÁrea: {r.area}\n"
        f"\tPerímetro: {r.perimetro}"
    )