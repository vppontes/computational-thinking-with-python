# Victor Paes Pontes - RM 572781
# Sávio Pessôa Afonso - RM 570789

tarifaBase = 2.5
categoriaPassageiro = input('\nCalculadora de Tarifas de Transporte, bem vindo !\n1 - Estudante \n2 - Trabalhador \n3 - Idoso \n4 - Comum: \nOpção: ')
distancia = float(input('\nInsira a distância que percorreu (em KM): '))

if distancia <= 0  or distancia == None:
    print('\nInsira um valor de verdade para a distância !')
else:
    match categoriaPassageiro:
        case '1':
            print(f'\nA sua categoria é de Estudante, o desconto é de 50%, para {distancia}km percorrida, o valor é de R${((tarifaBase * distancia) * 0.5):0.2f}')
        case '2':
            print(f'\nA sua categoria é de Trabalhador, o desconto é de 20%, para {distancia}km percorrida, o valor é de R${((tarifaBase * distancia) * 0.8):0.2f}')
        case '3':
            print(f'\nA sua categoria é de Idoso, o desconto é de 100%, para {distancia}km percorrida, a passagem é gratuita ! ')
        case '4':
            print(f'\nA sua categoria é de Comum, não há desconto, para {distancia}km percorrida, o valor é de R${((tarifaBase * distancia)):0.2f}') 
        case _:
            print('\nInsira uma opção válida (1 à 4) !')

# O senhor não ensinou como formatar o valor em duas casas decimais, nós sabemos fazer, porém é um conhecimento que não foi dado em sala de aula