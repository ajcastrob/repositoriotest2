import numpy as np


def calcular_promedio_temperatura(datos):
    # Columnas: temperatura, humedad, presión atmosférica, meses del año.
    # Separar los meses.
    meses = datos[:, 3].astype(int)

    temperatura_promedio_mes = np.zeros(12)
    for mes in range(12):
        datos_mes = datos[mes + 1 == meses]
        # Calcular la tempeartura promedio.
        temperatura_mes = datos_mes[:, 0].astype(float)
        temperatura_promedio_mes[mes] = sum(temperatura_mes) / len(temperatura_mes)

    return temperatura_promedio_mes


def calcular_promedio_humedad(datos):
    # Columnas: temperatura, humedad, presión atmosférica, meses del año.
    # Separar los meses.
    meses = datos[:, 3].astype(int)

    humedad_promedio_mes = np.zeros(12)
    for mes in range(12):
        datos_mes = datos[mes + 1 == meses]
        # Calcular la humedad promedio.
        humedad_mes = datos_mes[:, 1].astype(float)
        humedad_promedio_mes[mes] = sum(humedad_mes) / len(humedad_mes)

    return humedad_promedio_mes


def calcular_promedio_presion(datos):
    # Columnas: temperatura, humedad, presión atmosférica, meses del año.
    # Separar los meses.
    meses = datos[:, 3].astype(int)

    presion_promedio_mes = np.zeros(12)
    for mes in range(12):
        datos_mes = datos[mes + 1 == meses]
        # Calcular la presión mes.
        presion_mes = datos_mes[:, 2].astype(float)
        presion_promedio_mes[mes] = sum(presion_mes) / len(presion_mes)

    return presion_promedio_mes


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
