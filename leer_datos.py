import numpy as np


def obtener_datos(datos):
    lista_datos = []
    with open(datos, "r") as file:
        for line in file:
            try:
                datos_linea = [float(x) for x in line.strip().split(",")]
                if len(datos_linea) == 4:
                    lista_datos.append(datos_linea)
            except ValueError:
                print(f"Advertencia: Omitiendo línea mal formada: {line.strip()}")

    if not lista_datos:
        print("Error: No se encontraron datos válidos en el archivo.")
        return False, np.array([])

    try:
        datos_clima = np.array(lista_datos)
        return True, datos_clima
    except Exception as e:
        print(f"No se cumple los requisitos para formar la base de datos {e}")
        return False, np.array([])
