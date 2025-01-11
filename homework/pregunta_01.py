"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data = open("files\input\data.csv", "r").readlines()
    suma = 0
    for i in data:
        temp = i.split(",")[0]
        numero = temp.split("\t")
        suma += int(numero[1])
    return suma
print(pregunta_01())