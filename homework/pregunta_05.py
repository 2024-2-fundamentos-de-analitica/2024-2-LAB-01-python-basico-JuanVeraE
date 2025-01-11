"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    data = open("files/input/data.csv", "r").readlines()
    letras = {}
    for i in data:
        temp = i.split(",")[0]
        letra = temp[0]
        temp_num = i.split(",")[0]
        numero = temp_num.split("\t")
        numero = int(numero[1])

        if letra in letras:
            if numero > letras[letra][0]:
                letras[letra] = (numero, letras[letra][1])
            if numero < letras[letra][1]:
                letras[letra] = (letras[letra][0], numero)
        else:
            letras[letra] = (numero, numero)
    return sorted([(k, v[0], v[1]) for k, v in letras.items()])
print(pregunta_05())