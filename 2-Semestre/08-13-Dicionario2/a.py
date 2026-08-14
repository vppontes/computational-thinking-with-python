cliente = {
    "nome": "Kaio",
    "idade": 18,
    "sexo": "M"
}
print(cliente.items())
print(cliente.keys()) # IMPORTANTES
print(cliente.values())

estoque = {
    "maçã": 10,
    "banana": 7,
    "coco": 3
}

for fruta, quantidade in estoque.items():
    print(f'Fruta: {fruta.capitalize()}\tQuantidade: {quantidade}')

# Dicionário aninhado (duplo)
alunos = {
    "victor": {"nota1": 10, "nota2": 9},
    "savio": {"nota1": 6, "nota2": 4}
}

for nome, notas in alunos.items():
    for valor in notas.values():
        print(f'Nome: {nome}\tValor: {valor}')

for indice, (nome, notas) in enumerate(alunos.items()):
    print(f'Índice: {indice}\tNome: {nome}\tNotas: {notas.values()}')