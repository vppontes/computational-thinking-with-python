def verificar_numero_triangular(numero):
    if numero == None or numero <= 0:
        return False
    else:
        for i in range(numero):
            triangular = i * (i+1) * (i+2)
            if triangular == numero:
                return True
            elif triangular > numero:
                return False

print(verificar_numero_triangular(120))
print(verificar_numero_triangular(119))
print(verificar_numero_triangular(24))
print(verificar_numero_triangular(None))
print(verificar_numero_triangular(6))
print(verificar_numero_triangular(-2))