alunos = {}
notas = {}

nome = input('Nome: ')

cont = 1
contNotas = 0
for i in range(3):
    nota = float(input(f'{cont}ª Nota: '))
    notas[contNotas] = nota

    cont += 1
    contNotas += 1
alunos[nome] = notas

for aluno, notas in alunos.items():
    media = 0
    for valor in notas.values():
        media += valor
    status = ''
    # alunos["media"] = (media/3) NÃO DÁ PRA ADICIONAR MAIS UMA CHAVE ENQUANTO ESTÁ SENDO LIDA
    if (media/3) < 6:
        status = 'reprovado'
    else:
        status = 'aprovado'
    print(f'Aluno {aluno.capitalize()} está {status}!')