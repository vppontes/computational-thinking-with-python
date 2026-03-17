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