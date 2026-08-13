dados = [[], [], [], [], []]

contador = 0
while contador < 2:
    marca = input('Marca: ').title()
    versao = input('Versão: ').title()
    ano = int(input('Ano: '))
    cor = input('Cor: ').capitalize()
    ipva  = input('IPVA pago? (S/N): ').upper()

    print("\033[H\033[J", end="")
    carro = [marca, versao, ano, cor, ipva]

    cont = 0
    for info in carro:
        dados[cont].append(info)
        cont += 1

    contador += 1

print(dados)