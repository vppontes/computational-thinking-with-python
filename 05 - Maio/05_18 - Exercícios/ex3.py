def bhaskara(a, b, c):
    if a == 0 or b == 0:
        print('Raízes irracionais !')
        return
    
    delta = (b ** 2) - (4 * a * c)
    x1 = (- b + delta ** (1/2)) / (2 * a)
    x2 = (- b - delta ** (1/2)) / (2 * a)

    print(f'X1 = {x1}\nX2 = {x2}')

bhaskara(1, -4, -5)