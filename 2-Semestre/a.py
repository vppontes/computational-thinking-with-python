import os

lista_pessoas = []

for i in range(2):
    nome = input("Digite o nome da pessoa: ").capitalize()
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (H/M): ").upper()

    pessoa = [nome, idade, sexo]
    lista_pessoas.append(pessoa)
    os.system('cls')

for pessoa in lista_pessoas:
    print(f"Nome: {pessoa[0]}\nIdade: {pessoa[1]}\nSexo: {pessoa[2]}\n")