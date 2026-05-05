## Victor Paes Pontes - RM 572781
## 1ESPY - 04/05/2026

## Exercício 1 - Como usar a condição do while pra que ele possa ficar repetindo até o número não ser igual
import random

numeros_aleatorios = []
for i in range(10):
    numero = random.randint(1, 20)
    while numeros_aleatorios.count(numero) == 1:
        numero = random.randint(1, 20)
    numeros_aleatorios.append(numero)

print(numeros_aleatorios)

## Exercício 2 - Lembrar como verificar o número primo
lista_numeros = []
numeros_primos = []

for i in range(30):
    numero = random.randint(1, 50)
    lista_numeros.append(numero)

for j in lista_numeros:
    if j >= 1:
        for k in range(2, j):
            if j % k == 0:
                break
        else:
            numeros_primos.append(j)
print(numeros_primos)

## Exercício 3 - Não entendi se era pra verificar se os números aleatórios já existem na lista
lista_30 = []

for i in range(30):
    numero = random.randint(1, 50)
    lista_30.append(numero)

fator = int(input('Insira um número: '))
print(f'Antes:\t{lista_30}')

for j in range(len(lista_30)):
    lista_30[j] = lista_30[j] * fator

print(f'Depois:\t{lista_30}')

## Exercício 4
lista_palindromo = []

for i in range(10):
    numero = random.randint(1, 55)
    lista_palindromo.append(numero)

## Exercício 5 - Nenhuma
lista1 = []
lista2 = []
lista_final = []

for i in range(10):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    lista1.append(num1)
    lista2.append(num2)

for i in range(10):
    lista_final.append(lista1[i])
    lista_final.append(lista2[i])

print(f'Lista 1:\t{lista1}')
print(f'Lista 2:\t{lista2}')
print(f'\nLista final\t{lista_final}')