min = 0
max = 0

for i in range(10):
    valor = int(input(f'Insira o {i+1}º número: '))

    if valor > max:
        max = valor
    else:
        min = valor
print(f'O maior número digitado é {max} e o menor é {min}')

