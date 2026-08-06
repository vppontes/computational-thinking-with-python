lista = [3, 10, 7, 8, 1, 9, 8, 5, 8,]
max = lista[0]
min = lista[0]

for i in lista:
    if i > max:
        max = i
    else:
        min = i

print(f'Maior número: {max}\nMenor número: {min}')