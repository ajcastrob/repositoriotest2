import numpy as np


def _calcular_promedio_por_columna(datos, columna):
    meses = datos[:, 3].astype(int)
    promedio_mes = np.zeros(12)

    for mes in range(1, 13):
        datos_mes = datos[meses == mes]
        if datos_mes.size > 0:
            columna_mes = datos_mes[:, columna].astype(float)
            promedio_mes[mes - 1] = np.mean(columna_mes)
    return promedio_mes


def calcular_promedio_temperatura(datos):
    # Columnas: temperatura, humedad, presión atmosférica, meses del año.
    return _calcular_promedio_por_columna(datos, 0)


def calcular_promedio_humedad(datos):
    # Columnas: temperatura, humedad, presión atmosférica, meses del año.
    return _calcular_promedio_por_columna(datos, 1)


def calcular_promedio_presion(datos):
    # Columnas: temperatura, humedad, presión atmosférica, meses del año.
    return _calcular_promedio_por_columna(datos, 2)


def imprimir_temperatura(promedio_temperatura):
    for i in range(len(promedio_temperatura)):
        print(
            f"La temperatura durante el mes {i+1} fue de {promedio_temperatura[i]} grados."
        )

    print("")
    print(
        f"Promedio por año: {sum(promedio_temperatura)/len(promedio_temperatura):.2f} grados."
    )
    print("-" * 50)


def imprimir_humedad(promedio_humedad):
    for i in range(len(promedio_humedad)):
        print(f"La humedad durante el mes {i+1} fue de {promedio_humedad[i]:.2f}%.")

    print("")
    print(f"Promedio por año: {sum(promedio_humedad)/len(promedio_humedad):.2f}%.")
    print("-" * 50)


def imprimir_presion(promedio_presion):
    for i in range(len(promedio_presion)):
        print(f"La presión durante el mes {i+1} fue de {promedio_presion[i]:.2f} Pa.")

    print("")
    print(f"Promedio por año: {sum(promedio_presion)/len(promedio_presion):.2f} Pa.")
    print("-" * 50)
