cliente = {}
cliente['nome'] = 'Victor'
cliente['idade'] = 18
cliente['casado'] = 'sim'
cliente.update({'sexo': 'M'})
del cliente['casado']

print(cliente)