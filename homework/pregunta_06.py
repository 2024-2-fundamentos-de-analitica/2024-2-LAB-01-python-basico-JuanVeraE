"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

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
            valor = int(clave_temp[1])

            if clave in claves:
                if valor > claves[clave][0]:
                    claves[clave] = (valor, claves[clave][1])
                if valor < claves[clave][1]:
                    claves[clave] = (claves[clave][0], valor)
            else:
                claves[clave] = (valor, valor)
    return sorted([(k, v[1], v[0]) for k, v in claves.items()])
print(pregunta_06())