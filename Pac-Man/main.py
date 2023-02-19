import random

data = [".", "A", "O"]
matriz2 = []
contador = 0
contadorR = 0

matrizSize = int(input("Escriba el tamaña de la matriz: "))

matriz = [[0 for fila in range(matrizSize)] for columna in range(matrizSize)]

for filas in range(matrizSize):
    matriz = [random.choice(data) for _ in range(matrizSize)]
    matriz2.append(matriz)
    print(matriz2)


def counter_matriz():
    global contador, contadorR
    for x in matriz2:
        if x == "O":
            contador += contador
        if x == "A":
            contador = 0

    for x in reversed(matriz2):
        if x == "O":
            contadorR += contadorR
        if x == "A":
            contadorR = 0

    if contador > contadorR:
        print(contador)
        return contador
    else:
        print("R", contadorR)
        return contadorR


counter_matriz()
