lista = [4, 6, 7, 2, 3, 3, 9, 3, 2]

# len: retorna o tamanho de uma lista
print(len(lista))

# sum: retorna o somatório dos itens da lista
print(sum(lista))

# max: retorna o maior item da lista
print(max(lista))

# min: retorna o menor item da lista
print(min(lista))

# count: contar quantas vezes um item aparece na lista
print(lista.count(3))

# index: retornar o índice onde um item se encontra (apenas a primeira ocorrencia)
try:
    print(lista.index(2))
except ValueError:
    print('O item não está na lista')

# append: insere um item no final da lista
lista = [3, 5, 6, 2, 2, 5, 2, 8, 9]
lista.append(10)
print(lista)

# insert: insere um item na lista em uma posição específica
lista.insert(4, 20)
print(lista)

# pop: remove um item de um índice específico e retorna o valor removido
try:
    item = lista.pop(3)
    print(lista)
    print(item)
except IndexError:
    print('O índice nao existe na lista')

# remove: remove a primeira ocorrencia de um item
try:
    lista.remove(2)
    print(lista)
except ValueError:
    print('O valor não se encontra na lista')

# sort: ordena uma lista em ordem crescente
lista.sort()
print(lista)

# sort(reverse=True): ordena uma lista em ordem decrescten
lista.sort(reverse=True)
print(lista)

nomes = ['João', 'Ana', 'Paulo', 'Ana Maria']
nomes.sort()
print(nomes)

# in: verifica se um item existe na lista (Retorna True ou False
n = int(input('Digite um numero: '))
if n in lista:
    print('O número existe na lista')
else:
    print('O número não exite na lista')

# concatenação de listas
lista1 = [10, 20]
lista2 = [60, 70, 20]

lista3 = lista1 + lista2
print(lista3)


# copy (realiza a cópia de uma lista)
lista1 = [1, 2, 3]
lista2 = lista1.copy()

print(lista1)
print(lista2)

lista2[0] = 100

print(lista1)
print(lista2)
