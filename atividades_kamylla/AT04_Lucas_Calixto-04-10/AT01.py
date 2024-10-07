quant = 0
import random

mat = [[0 for j in range(3)] for i in range(3)]

for i in range(3):
    for j in range(3):
        # num = int(input("(" + str(i + 1) + "," + str(j + 1) + "): "))
        mat[i][j] = random.radint(0, 10)
        print(mat[i][j], end=" ")

for i in range(3):
    for j in range(3):
        if mat[i][j] != 0:
            quant = quant + 1

print("Quantidade de elementos diferentes de zero: ", quant)