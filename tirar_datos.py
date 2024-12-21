import random

def dame_numero(desde, hasta):
    return random.randint(desde, hasta)

def calcula_porcentaje(valor, total):
    resultado = (valor * 100) / total
    return int(resultado)

def tirar_dado(veces):

    uno = 0
    dos= 0
    tres= 0
    cuatro= 0
    cinco= 0
    seis= 0

    for num in range(veces):
        resultado = dame_numero(1, 6)
        if resultado == 1:
            uno += 1
        if resultado == 2:
            dos += 1
        if resultado == 3:
            tres += 1
        if resultado == 4:
            cuatro += 1
        if resultado == 5:
            cinco += 1
        if resultado == 6:
            seis += 1
        
    print(f"""Las cantidades de repeticiones fueron:
1 = {uno} 
2 = {dos}  
3 = {tres} 
4 = {cuatro} 
5 = {cinco} 
6 = {seis} \n""")

    print(f"""Los porcentajes de cada cara fueron:
El 1 tuvo {calcula_porcentaje(uno, veces)}% de ocurrencia
El 2 tuvo {calcula_porcentaje(dos, veces)}% de ocurrencia
El 3 tuvo {calcula_porcentaje(tres, veces)}% de ocurrencia
El 4 tuvo {calcula_porcentaje(cuatro, veces)}% de ocurrencia
El 5 tuvo {calcula_porcentaje(cinco, veces)}% de ocurrencia
El 6 tuvo {calcula_porcentaje(seis, veces)}% de ocurrencia
""")
tirar_dado(10)
