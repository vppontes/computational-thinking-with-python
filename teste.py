notas = []
nota = 0

while True:
    nota = float(input('Insira uma nota: '))

    if nota == -1:
        break
    elif nota >= 0 and nota <= 10:
        notas.append(nota)
    else:
        print('Nota inválida !')

media = 0
for i in notas:
    media += i
media = media / len(notas)

acimaMedia = 0
for z in notas:
    if z > media:
        acimaMedia += 1

print(f'Total de notas: {len(notas)}\nNotas: {notas}\nMédia: {media}\nNotas acima da média: {acimaMedia}')