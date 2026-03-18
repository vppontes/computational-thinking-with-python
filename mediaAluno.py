### ALGORITMO PARA MOSTRAR QUANTO O ALUNO PRECISA TIRAR NA GLOBAL SOLUTION 2 PARA PASSAR DE ANO

### PRIMEIRA MÉDIA: M1 = ((CP1 + CP2)/2) * 0.2 + ((SP1 + SP2)/2) * 0.2 + GS1 * 0.6

### SEGUNDA MÉDIA: M2 = ((CP4 + CP5)/2) * 0.2 + ((SP3 + SP4)/2) * 0.2 + GS2 * 0.6

### MÉDIA PRIMEIRO BIMESTRE

def mediaPrimeiroBimestre():
    ### Listas para organizar as notas
    notasCheckpoint = []
    notasSprint = []

    def inserirNotasCP():
        for i in range(3):
            ### Inserção das notas através do input()
            nota = float(input(f'Insira a nota do {i + 1}º Checkpoint: '))

            ### Verificação do valor inserido
            if nota < 0 or nota > 10 or nota == None:
                ### Aviso caso o usuário faça coisa errada
                print('Insira uma nota válida (de 0 à 10) !')
                break
            else:
                ### Inserir notas em uma lista
                notasCheckpoint.append(nota)

        ###  Ordenar as notas por ordem crescente e excluir a nota mais baixa
        notasCheckpoint.sort()
        notasCheckpoint.pop(0)

    def inserirNotasSP():
        for i in range(2):
            nota = float(input(f'Insira a nota da {i + 1}º Sprint: '))

            if nota < 0 or nota > 10 or nota == None:
                print('Insira uma nota válida (de 0 à 10) !')
                break
            else:
                notasSprint.append(nota)

    def mediaTotal():
        ### Chamada das funções
        inserirNotasCP()
        inserirNotasSP()

        ### Inserção da nota da GS
        notaGlobalSolution = float(input('Insira a nota da Global Solution: '))
        
        ### Verificação da nota da GS
        if notaGlobalSolution < 0 or notaGlobalSolution > 10 or notaGlobalSolution == None:
            print('Insira uma nota válida (de 0 à 10) !')

        ### Soma as notas dos checkpoints e sprints, dividindo pelo número de notas, aplicando os pesos e somando todas as notas para a média
        mediaBimestre = (sum(notasCheckpoint) / 2) * 0.2 + (sum(notasSprint) / 2) * 0.2 + notaGlobalSolution * 0.6
        
        ### Apresentação da média para o usuário
        print(f'A média do primeiro bimestre é de: {mediaBimestre}')

    ### Chamada da função
    mediaTotal()

def mediaSegundoBimestre():
    print('a')

def mediaTotal():
    ### Chamada das funções "pai"
    mediaPrimeiroBimestre()
    mediaSegundoBimestre()