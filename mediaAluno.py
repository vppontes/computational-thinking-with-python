### ALGORITMO PARA MOSTRAR QUANTO O ALUNO PRECISA TIRAR NA GLOBAL SOLUTION 2 PARA PASSAR DE ANO

### PRIMEIRA MÉDIA: M1 = ((CP1 + CP2)/2) * 0.2 + ((SP1 + SP2)/2) * 0.2 + GS1 * 0.6

### SEGUNDA MÉDIA: M1 = ((CP4 + CP5)/2) * 0.2 + ((SP3 + SP4)/2) * 0.2 + GS2 * 0.6

### MÉDIA PRIMEIRO BIMESTRE

notasCheckpoint = []
notasSprint = []

def inserirNotasCP():
    for i in range(3):
        ### Inserção das notas através do input()
        nota = float(input(f'Insira a nota do {i + 1}º Checkpoint: '))

        ### Verificação do valor inserido
        if nota < 0 or nota > 10:
            print('Insira uma nota válida (de 0 à 10) !')
            break
        else:
            ### Inserir notas em uma lista
            notasCheckpoint.append(nota)

    retirarMenorNotaCP(notasCheckpoint)

def inserirNotasSP():
    for i in range(2):
        nota = float(input(f'Insira a nota da {i + 1}º Sprint: '))

        if nota < 0 or nota > 10:
            print('Insira uma nota válida (de 0 à 10) !')
            break
        else:
            notasSprint.append(nota)

def retirarMenorNotaCP(notas):
    notas.sort()
    notas.pop(0)

def mediaPrimeiroBimestre():
    inserirNotasCP()
    inserirNotasSP()

    notaGlobalSolution = float(input('Insira a nota da Global Solution: '))



    mediaBimestre = (notasCheckpoint / 2) * 0.2 + (notasSprint / 2) * 0.2 + notaGlobalSolution * 0.6
    print(f'A média do primeiro bimestre é de: {mediaBimestre}')

mediaPrimeiroBimestre()