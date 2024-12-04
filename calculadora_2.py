print('Bienvenido a la calculadora')
print('Para salir escribe Salir')
print('Las opes son suma, multi, div y resta')

v1 = False
v2 = False

while True:
    if not v1:
        v1 = input('Ingrese Numero: ')
    if v1 == "salir":
        break

    op = input('Ingresa operacion: ')
    if op.lower() == "salir":
        break
    if op not in ['suma', 'multi', 'div', 'resta']:
        op = input('Ingresa operacion: ')

    v2 = input('Ingresa siguiente Numero: ')
    if v2.lower() == 'salir':
        break
    v1 = int(v1)
    v2 = int(v2)

    if op == "suma":
        resultado = v1 + v2
    elif op == "multi":
        resultado = v1 * v2
    elif op == "div":
        resultado = v1 / v2
    elif op == "resta":
        resultado = v1 - v2
    print(f'El resultado es {resultado}')
    v1 = resultado
