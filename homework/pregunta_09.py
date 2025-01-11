"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    data = open("files\input\data.csv", "r").readlines()
    claves = {}
    for i in data:
        temp = i.split("\t")
        clave = temp[-1]
        clave = clave.split(",")
        for i in clave:
            clave = i.strip()
            clave_temp = clave.split(":")     
            clave = clave_temp[0]
            if clave in claves:
                claves[clave] += 1
            else:
                claves[clave] = 1
    return claves
print(pregunta_09())