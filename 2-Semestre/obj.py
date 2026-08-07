dados = [[], [], []]
contador = 0

while contador <= 2:
    nome = input('nome: ')
    idade = int(input('idade: '))
    pessoa = {'nome': nome, 'idade': idade}
    dados[contador].append(pessoa['nome'])
    dados[contador].append(pessoa['idade'])
    print("\033[H\033[J", end="")
    contador += 1

print(dados)