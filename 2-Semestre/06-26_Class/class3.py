class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura


retangulos = [
    Retangulo(10, 5),
    Retangulo(8, 4),
    Retangulo(12, 6),
    Retangulo(7, 3),
    Retangulo(15, 5)
]

for i, r in enumerate(retangulos, 1):
    area = r.base * r.altura
    perimetro = 2 * (r.base + r.altura)

    print(f"{i}: Base: {r.base} | Altura: {r.altura} | "
          f"Área: {area} | Perímetro: {perimetro}")