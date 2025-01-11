"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    data = open("files\input\data.csv", "r").readlines()
    letras = []
    for i in data:
        temp = i.split("\t")
        letra = temp[0]
        num_1 = temp[3].split(",")
        num_2 = temp[4].split(",")
        letras.append((letra, len(num_1), len(num_2)))
    return letras
print(pregunta_10())