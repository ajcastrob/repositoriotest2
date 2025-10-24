import numpy as np


def obtener_datos(datos):
    datos_clima = np.array([])
    with open(datos, "r") as file:
        counter = 0
        for line in file:
            datos = line.strip().split(", ")
            datos_clima = np.append(datos_clima, datos)
            counter += 1

    filas = counter
    columnas = 4
    datos_clima = datos_clima.reshape(filas, columnas)
    return datos_clima
