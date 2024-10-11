import random

corrida = [[0 for j in range(4)] for i in range(4)]

for i in range(4):
    for j in range(4):
        corrida[i][j] = random.uniform(3.1 , 6.9)

minutos = [[0 for j in range(4)] for i in range(4)]
segundos = [[0 for j in range(4)] for i in range(4)]

for i in range(4):
    for j in range(4):
        minutos[i][j] = int(corrida[i][j])
        segundos[i][j] = (corrida[i][j] - minutos[i][j]) * 100
        segundos[i][j] = int(segundos[i][j])

for i in range(4):
    for j in range(4):
        print(f"O tempo do corredor {i+1} na volta {j+1} foi de {minutos[i][j]}m : {segundos[i][j]} s .")