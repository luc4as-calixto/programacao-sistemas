n1 = 0
n2 = 1
n3 = 0

print(n1, end = " ")
print(n2, end = " ")
for i in range(0, 14):
    n3 = n1 + n2
    n1 = n2
    n2 = n3

    print(n3, end = " ")