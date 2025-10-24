import numpy as np


def obtener_datos(datos):
    datos_clima = np.array([])
    comprobar = False
    with open(datos, "r") as file:
        counter = 0
        for line in file:
            datos = line.strip().split(", ")
            datos_clima = np.append(datos_clima, datos)
            counter += 1
    try:
        filas = counter
        columnas = 4
        datos_clima = datos_clima.reshape(filas, columnas)
        comprobar = True
        return comprobar, datos_clima
    except Exception as e:
        print(f"No se cumple los requisitos para formar la base de datos {e}")
