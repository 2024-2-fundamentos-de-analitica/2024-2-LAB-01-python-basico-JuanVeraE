"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    data = open("files\input\data.csv", "r").readlines()
    letras = {}
    for i in data:
        temp = i.split("\t")
        letra = temp[0]
        num = temp[4].split(",")
        num = [int(i.split(":")[1]) for i in num]
        if letra in letras:
            letras[letra] += sum(num)
        else:
            letras[letra] = sum(num)
    return letras
print(pregunta_12())