import sys
import os
from leer_datos import obtener_datos
from operaciones import (
    calcular_promedio_humedad,
    calcular_promedio_presion,
    calcular_promedio_temperatura,
    imprimir_humedad,
    imprimir_presion,
    imprimir_temperatura,
)


def main():
    if len(sys.argv) > 1:
        archivo = sys.argv[1]
        if not os.path.exists(archivo):
            print(f"Error: El archivo '{archivo}' no fue encontrado.")
            return
    else:
        archivo = "datos.txt"
        if not os.path.exists(archivo):
            print(f"Error: El archivo por defecto '{archivo}' no fue encontrado.")
            return

    comprobar, data_base = obtener_datos(archivo)

    if comprobar:
        # Llamar a las funciones
        promedio_temperatura = calcular_promedio_temperatura(data_base)
        imprimir_temperatura(promedio_temperatura)
        promedio_humedad = calcular_promedio_humedad(data_base)
        imprimir_humedad(promedio_humedad)
        promedio_presion = calcular_promedio_presion(data_base)
        imprimir_presion(promedio_presion)


if __name__ == "__main__":
    main()
