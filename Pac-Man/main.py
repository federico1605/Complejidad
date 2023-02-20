import random

data = [".", "A", "O"]
matriz2 = []
contador = 0
contadorR = 0

matrizSize = int(input("Escriba el tamaña de la matriz: "))

matriz = [[0 for fila in range(matrizSize)] for columna in range(matrizSize)]


def addMatriz():
    for filas in range(matrizSize):
        matriz = [random.choice(data) for _ in range(matrizSize)]
        matriz2.append(matriz)


addMatriz()

if matriz2[0][0] == 'A':
    matriz2.clear()
    addMatriz()
elif matriz2[0][0] == 'O':
    matriz2.clear()
    addMatriz()

for x in matriz:
    if x == 'O':
        contador = contador + 1
    elif x == 'A':
        contador = 0

for x in reversed(matriz):
    if x == 'O':
        contadorR += contadorR
    elif x == 'A':
        contadorR = 0

if contador > contadorR:
    print("Mejor camnio el original", contador)
else:
    print("Mejor camino con el recorrido al reves ", contadorR)


print(matriz2)
