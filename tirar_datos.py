import random

def dame_numero(desde, hasta):
    return random.randint(desde, hasta)

def calcula_porcentaje(valor, total):
    resultado = (valor * 100) / total
    return int(resultado)

def tirar_dado(veces):

    cara_1 = 0
    cara_2= 0
    cara_3= 0
    cara_4= 0
    cara_5= 0
    cara_6= 0

    for num in range(veces):
        resultado = dame_numero(1, 6)
        if resultado == 1:
            cara_1 += 1
        if resultado == 2:
            cara_2 += 1
        if resultado == 3:
            cara_3 += 1
        if resultado == 4:
            cara_4 += 1
        if resultado == 5:
            cara_5 += 1
        if resultado == 6:
            cara_6 += 1
        
    print(f"""Las cantidades de repeticiones fueron:
1 = {cara_1} 
2 = {cara_2}  
3 = {cara_3} 
4 = {cara_4} 
5 = {cara_5} 
6 = {cara_6} \n""")

    print(f"""Los porcentajes de cada cara fueron:
El 1 tuvo {calcula_porcentaje(cara_1, veces)}% de ocurrencia
El 2 tuvo {calcula_porcentaje(cara_2, veces)}% de ocurrencia
El 3 tuvo {calcula_porcentaje(cara_3, veces)}% de ocurrencia
El 4 tuvo {calcula_porcentaje(cara_4, veces)}% de ocurrencia
El 5 tuvo {calcula_porcentaje(cara_5, veces)}% de ocurrencia
El 6 tuvo {calcula_porcentaje(cara_6, veces)}% de ocurrencia
""")
tirar_dado(10)
