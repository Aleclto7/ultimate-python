print('Vamos a calcular tu descuento')

def calcular_descuento():
    cuenta = int(input('Ingresa el total a pagar \n'))
    descuento = int(input('Ahora ingresa tu descuento \n'))

    valor_descuento = cuenta * descuento / 100
    return cuenta - valor_descuento

total = calcular_descuento()
print(f'El total a pagar es {int(total)}')
