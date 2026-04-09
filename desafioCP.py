cp1 = float(input('Insira uma nota da 1º Checkpoint: '))
while cp1 < 0 or cp1 > 10:
    cp1 = float(input('Insira uma nota válida da 1º Checkpoint: '))


cp2 = float(input('Insira uma nota da 2º Checkpoint: '))
while cp2 < 0 or cp2 > 10:
    cp2 = float(input('Insira uma nota válida da 2º Checkpoint: '))


cp3 = float(input('Insira uma nota da 3º Checkpoint: '))
if cp3 < 0 or cp3 > 10:
    cp3 = float(input('Insira uma nota válida da 3º Checkpoint: '))


if cp1 <= cp2 and cp2 <= cp3:
    cp1 = cp3
elif cp2 <= cp3 and cp2 <= cp1:
    cp2 = cp3

print(f'As duas maiores notas são {cp1} e {cp2}')