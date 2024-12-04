#  My Solution
# def es_palindromo(texto):
#     s_espacios = ""

#     for ch in texto:
#         if ch == " ":
#             None
#         else:
#             s_espacios += ch.lower()


#     length = len(s_espacios) -1
#     reverse = s_espacios


#     for ch in s_espacios:
#         reverse = ch + reverse[:length]

#     return(reverse in s_espacios)




# Professor Solution
def no_space(texto):
    nuevo_texto = ''
    for ch in texto:
        if ch != ' ':
            nuevo_texto += ch
    return nuevo_texto

def reverse(texto):
    texto_al_revez = ''
    for ch in texto:
        texto_al_revez = ch + texto_al_revez
    return texto_al_revez

def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_revez = reverse(texto)
    return texto.lower() == texto_al_revez.lower()



print("Abba", es_palindromo("Abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola Mundo", es_palindromo("Hola Mundo"))
print("Somos o no Somos", es_palindromo("Somos o no Somos"))
