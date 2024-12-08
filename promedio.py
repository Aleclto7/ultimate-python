# My Solution
def promedio (*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma / len(numeros)

print(promedio(2, 3, 3, 5, 7, 10))

# Professor solution
# def calcular_media(*numeros):
#     if not numeros:
#         return 0
#     return sum(numeros) / len(numeros)
# print(calcular_media(1, 2, 3, 4, 5))