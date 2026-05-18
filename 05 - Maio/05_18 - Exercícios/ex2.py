import random

vezes = 1000

def lancar_dados(total_de_vezes):
    um = 0
    dois = 0
    tres = 0
    quatro = 0
    cinco = 0
    seis = 0

    for i in range(total_de_vezes):
        rolada = random.randint(1, 6)
        if rolada == 1:
            um += 1
        elif rolada == 2:
            dois += 1
        elif rolada == 3:
            tres += 1
        elif rolada == 4:
            quatro += 1
        elif rolada == 5:
            cinco += 1
        elif rolada == 6:
            seis += 1

    print(f'Número 1: {um} vezes')
    print(f'Número 2: {dois} vezes')
    print(f'Número 3: {tres} vezes')
    print(f'Número 4: {quatro} vezes')
    print(f'Número 5: {cinco} vezes')
    print(f'Número 6: {seis} vezes')

lancar_dados(vezes)

print('\n', '*' * 20, 'outra resolução', '*' * 20, '\n')

def lancar_dados2(total_de_vezes):
    dado = [0, 0, 0, 0, 0, 0]

    for i in range(total_de_vezes):
        rolada = random.randint(1, 6)

        match rolada:
            case 1:
                dado[0] += 1
            case 2:
                dado[1] += 1
            case 3:
                dado[2] += 1
            case 4:
                dado[3] += 1
            case 5:
                dado[4] += 1
            case 6:
                dado[5] += 1

    print(f'Número 1: {dado[0]} vezes\nNúmero 2: {dado[1]} vezes\nNúmero 3: {dado[2]} vezes\nNúmero 4: {dado[3]} vezes\nNúmero 5: {dado[4]} vezes\nNúmero 6: {dado[5]} vezes\n')

lancar_dados2(vezes)