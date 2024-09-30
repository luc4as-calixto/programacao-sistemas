paisA = 80000
paisB = 200000

taxaA = 0.03
taxaB = 0.015

anos = 0

while paisA < paisB:
    paisA = paisA + (paisA * taxaA)
    paisB= paisB + (paisB * taxaB)
    anos = anos + 1 

print("Para o país A utrapasse ou iguale o país B serão necessários {} anos ".format(anos))