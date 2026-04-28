import random

## 27 de Abril de 2026
## Victor Paes Pontes - RM 572781

## EXERCÍCIO 01
pares = []
impares = []

for i in range(10):
    numero = int(input('Insira um número: '))

    if numero != 0:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

print(f'Pares: {pares}\nÍmpares: {impares}')

## EXERCÍCIO 02
numeros = []

for i in range(10):
    numero = int(input('Insira um número: '))

    if numero != 0:
        numeros.append(numero)

media = 0
for x in numeros:
    media += x
        
somaPares = 0
for z in numeros:
    if z % 2 == 0:
        somaPares += z

print(f'Média aritmética: {media/10}\nSoma dos pares: {somaPares}')

## EXERCÍCIO 03

numerosAleatorios = []

for i in range(20):
    numeroAleatorio = random.randint(1, 50)
    numerosAleatorios.append(numeroAleatorio)

print(f'Lista de números: {numerosAleatorios}\nSoma: {sum(numerosAleatorios)}\nMaior número: {max(numerosAleatorios)}\nMenor número: {min(numerosAleatorios)}')
## Utilizei min(), max() e sum(), não lembro do senhor ter passado, porém são nativos do Python e era o que eu já sabia

## EXERCÍCIO 04
nomes = []
idades = []
maioresIdade = []

for i in range(10):
    nome = input('Insira um nome: ')
    idade = int(input('Insira a idade dessa pessoa: '))

    if nome != None and idade > 0:
        nomes.append(nome)
        idades.append(idade)

    if idade >= 18:
        maioresIdade.append(nome)

print(f'Maiores de idade: {maioresIdade}')

## EXERCÍCIO 05
numeros = []

for i in range(10):
    numeroAleatorio = random.randint(1, 10) ## No exercício não diz o intervalo dos números aleatórios
    numeros.append(numeroAleatorio)

escolha = int(input('Insira um número entre 1 e 10: '))

if escolha >= 1 and escolha <= 10:
    vezesRepetidos = 0
    for i in numeros:
        if i == escolha:
            vezesRepetidos += 1
else: 
    print('Escolha um número válido !')

vezes = 'vez'
if vezesRepetidos > 1 or vezesRepetidos == 0:
    vezes = 'vezes'

print(f'{numeros}\nO número {escolha} aparece {vezesRepetidos} {vezes} !')

## EXERCÍCIO 06
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