carrinho = {}
produto = ''

while produto != 'sair':
    produto = input('Produto: ')
    if produto == 'sair':
        print("\033[H\033[J", end="") # Dá um cls no console
        break
    preco = float(input('Preço: '))
    carrinho[produto] = preco

for produto, valor in carrinho.items():
    print(f'Produto: {produto.capitalize()}\tPreço: R${valor}')