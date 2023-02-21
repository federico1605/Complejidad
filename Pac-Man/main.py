matriz = []
counter = 0
counterMax = 0
flag = True
matrizSize = 0

while flag:
    matrizSize = input()
    matrizSize = int(matrizSize)
    flag = False if (2 <= matrizSize <= 100) else "Please, try again the size is between 2 and 100"

for i in range(matrizSize):
    while True:
        column = input()
        if len(column) != matrizSize:
            pass
        else:
            break
    matriz.append(list(column))

size = len(matriz)

for x in range(size):
    if x % 2 == 0:
        for y in range(size):
            if matriz[x][y] == "o":
                counter += 1
                if counter > counterMax:
                    counterMax = counter
            elif matriz[x][y] == "a":
                counter = 0
    else:
        for y in range(size - 1, -1, -1):
            if matriz[x][y] == "o":
                counter += 1
                if counter > counterMax:
                    counterMax = counter
            elif matriz[x][y] == "a":
                counter = 0
print(counterMax)
