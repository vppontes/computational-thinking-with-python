### EXERCÍCIO DA LANCHONETE
escolha = input('Lanchonete CARCARÁ, seja bem vindo!\n\nFaça o seu pedido:\n1. Lanche\n2. Bebida\n3. Sobremesa\n4. Sair\nOpção: ')

valor = 0

match escolha:
    case '1':
        lanche = input('\nEscolha seu lanche:\n\n1. Cachorro-Quente: R$15,00\n2. Hambúrguer: R$20,00\nOpção: ')
        
        quantidade = int(input('Insira a quantidade: '))

        if quantidade > 0:    
            match lanche:
                case '1':
                    print(f'\nO valor para {quantidade} de cachorro-quente ficará: R${float(quantidade*15)}')

                    valor = 15
                case '2':
                    print(f'\nO valor para {quantidade} de hambúrguer ficará: R${float(quantidade*20)}')

                    valor = 20
                case _:
                    print('Insira uma opção válida !')
        else:
            print('\nInsira uma quantidade válida !')
        
    case '2':
        bebida = input('\nEscolha sua bebida:\n\n1. Refrigerante: R$6,00\n2. Suco natural: R$10,00\nOpção: ')
        
        quantidade = int(input('Insira a quantidade: '))
        
        if quantidade > 0:   
            match bebida:
                case '1':
                    print(f'\nO valor para {quantidade} de refrigerante ficará: R${float(quantidade*6)}')

                    valor = 6
                case '2':
                    print(f'\nO valor para {quantidade} de suco natural ficará: R${float(quantidade*10)}')

                    valor = 10
                case _:
                    print('Insira uma opção válida !')
        else:
            print('\nInsira uma quantidade válida !')

    case '3':
        sobremesa = input('\nEscolha sua sobremesa: \n\n1. Açaí: R$25,00 \n2. Sorvete: R$18,00\nOpção: ')
        
        quantidade = int(input('Insira a quantidade: '))
        
        if quantidade > 0:   
            match sobremesa:
                case '1':
                    print(f'\nO valor para {quantidade} de açaí ficará: R${float(quantidade*25)}')

                    valor = 25
                case '2':
                    print(f'\nO valor para {quantidade} de sorvete ficará: R${float(quantidade*18)}')

                    valor = 18
                case _:
                    print('Insira uma opção válida !')
        else:
            print('\nInsira uma quantidade válida !')

    case '4':
        print('\nObrigado pela preferência, até logo !')

    case _:
        print('\nInsira uma opção válida (1 à 4)!')

if valor > 0:
    print(f'\nO total do seu pedido é de R${float(quantidade*valor)} !')