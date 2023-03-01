"""
Federico Zapata Serna -- fede.zapata16@gmail.com
Para desarollar el programa se inicio iniciando variables
con las cuales se pide el tamaño de la matriz, se crea un ciclo
for que va hasta el tamaño de la matriz y con este while se ingresa
la matriz se puede ingresar dato a dato o toda la matriz ya armada,
se inician mas variables y se entra a un ciclo for donde se empieza
a evaluar hasta el tamaño de la matriz, con los condicionales se
guardando la informacion de la mayor cantidad de comidad que pudo comer
y cual fue la mejor ruta
"""

matriz = []
matrizSize = int(input())
for i in range(matrizSize):
    while True:
        column = input()
        if len(column) == matrizSize:
            break
    matriz.append(list(column))
size = len(matriz)
counter = 0
counterMax = 0
for x in range(size):
    if x % 2 == 0:
        for y in range(size):
            if matriz[x][y] == "o":
                counter += 1
                if counter > counterMax:
                    counterMax = counter
            elif matriz[x][y] == "A":
                counter = 0
    else:
        for y in range(size - 1, -1, -1):  # Se invierte la lista para contador de comida inverso
            if matriz[x][y] == "o":
                counter += 1
                if counter > counterMax:
                    counterMax = counter
            elif matriz[x][y] == "A":
                counter = 0
print(counterMax)
