def a_segundos(valor, unidad):
    resultado = 0
    if unidad.lower() == 'segundo' or unidad == 'segundos':
        resultado = int(valor)
    if unidad.lower() == 'minuto' or unidad == 'minutos':
        resultado = int(valor) * 60
    elif unidad == 'hora' or unidad == 'horas':
        resultado = int(valor) * 3600
    elif unidad == 'dia' or unidad == 'dias':
        resultado = int(valor) * 86400
    elif unidad == 'mes' or unidad == 'meses':
        resultado = int(valor) * 2678400
    elif unidad == 'año' or unidad == 'años':
        resultado = int(valor) * 31536000
    else:
        return False

    return resultado

def de_segundos(valor, unidad):
    resultado = 0
    if unidad.lower() == 'minuto' or unidad == 'minutos':
        resultado = int(valor) / 60
    elif unidad == 'hora' or unidad == 'horas':
        resultado = int(valor) / 3600
    elif unidad == 'dia' or unidad == 'dias':
        resultado = int(valor) / 86400
    elif unidad == 'mes' or unidad == 'meses':
        resultado = int(valor) / 2678400
    elif unidad == 'año' or unidad == 'años':
        resultado = int(valor) / 31536000
    else:
        return False

    return resultado

def convertir_tiempo(valor, unidad1, unidad2):
    valor_en_segundos = a_segundos(valor, unidad1.lower())
    segundos_a_unidad = de_segundos(valor_en_segundos, unidad2.lower())

    if valor_en_segundos == False or segundos_a_unidad == False:
        return 'No puedo convertir este Tipo de Unidad '
    else:
        return f'El Resultado es {int(segundos_a_unidad)} {unidad2.lower()}'


print (convertir_tiempo(2, 'horas', 'miNutOs'))