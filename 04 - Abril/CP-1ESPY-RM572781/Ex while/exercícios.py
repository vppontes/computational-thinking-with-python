### EXERCÍCIO DE DESCONTO

valorProduto = float(input('Insira o valor do produto: '))
valorDesconto = float(input('Insira o valor do desconto: '))/100

valorFinal = valorProduto - (valorProduto * valorDesconto)
print(f'R${valorFinal}')

### EXERCÍCIO DE TEMPO

tempo = int(input('Insira um valor de tempo em segundos: '))
if tempo < 0:
    print('Insira um número válido (maior que 0)')
else:
    horas = tempo // 3600
    minutos = (tempo - (horas * 3600)) // 60
    segundos = tempo % 60

    print(f'{horas} hora, {minutos} minutos e {segundos} segundos')

"""
    COMENTÁRIO:
    '//' é a divisão que deixa resto
"""

### EXERCÍCIO DE TRANSFORMAR NÚMERO
numero = int(input('Insira um número inteiro: '))

if numero < 0:
    numero = numero * (-1)
print(numero)

### EXERCÍCIO DAS LETRAS
letra = input('Digite uma letra: ')

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print(f'A letra {letra} é uma vogal')
else:
    print(f'A letra {letra} é uma consoante')

### EXERCÍCIO DE CHECKPOINTS
cp1 = float(input('Insira a nota da checkpoint: '))
cp2 = float(input('Insira a nota da checkpoint: '))
cp3 = float(input('Insira a nota da checkpoint: '))

if cp1 <= cp2 and cp2 <= cp3:
    cp1 = cp3
elif cp2 <= cp3 and cp2 <= cp1:
    cp2 = cp3

print(f'As duas maiores notas são {cp1} e {cp2}')

### EXERCÍCIO DE TRIÂNGULO
lado1 = float(input('Insira um valor do triângulo: '))
lado2 = float(input('Insira um valor do triângulo: '))
lado3 = float(input('Insira um valor do triângulo: '))

if lado1 == lado2 and lado1 == lado3:
    print('O triângulo é equilátero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('O triângulo é isósceles')
else:
    print('O triângulo é escaleno')

# OUTRA FORMA

if lado1 == lado2 and lado2 == lado3:
    print('O triângulo é equilátero')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print('O triângulo é escaleno')
else:
    print('O triângulo é isósceles')

### EXERCÍCIO MATCH CASE
input = input('''
    Digite um número para uma operação:
    1. Verificar nota
    2. Editar nota
    3. Inserir nota
    4. Excluir nota
    5. Sair
''')

match input:
    case '1':
        print('Você escolheu a opção de verificar a nota do aluno.')
    case '2':
        print('Você escolheu a opção de editar a nota do aluno.')
    case '3':
        print('Você escolheu a opção de inserir a nota do aluno.')
    case '4':
        print('Você escolheu a opção de excluir a nota do aluno.')
    case '5':
        print('Você escolheu a opção de sair, obrigado !')
    case _:
        print('Insira uma opção válida !')