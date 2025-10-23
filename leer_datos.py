archivo = "datos.txt"

with open(archivo, "r") as file:
    for line in file:
        datos = line.strip().split(", ")
        print(datos)
