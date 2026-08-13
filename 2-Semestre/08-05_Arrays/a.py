import os

lista_pessoas = []

for i in range(1):
    nome = input("Digite o nome da pessoa: ").title().strip()
    idade = int(input("Digite a idade da pessoa: ")).strip()
    sexo = input("Digite o sexo da pessoa (H/M): ").upper().strip()

    pessoa = [nome, idade, sexo]
    lista_pessoas.append(pessoa)
    print("\033[H\033[J", end="")

for pessoa in lista_pessoas:
    print(f"Nome: \t{pessoa[0]}\nIdade: \t{pessoa[1]}\nSexo: \t{pessoa[2]}\n")