import numpy as np
m = np.ones((2, 3))
m = m * 4
print(m)    

print()

n = np.ones((2, 3))
n = n + 1
n = n ** 3
print(n)

print()

A = np.array([[1,1], [0,1]])
B = np.array([[2,0], [3,4]])
C= A*B
print(C)

print()	

A = np.array([[1,1], [0,1]])
B = np.array([[2,0], [3,4]])
C = np.dot(A,B) # multiplicação de matrizes
print(C)