frutas = "maça", "banana", "laranja", "uva", "melancia"

preco = {0:5.00, 1:2.50, 2:3.00, 3:4.00, 4:7.00}

for i in frutas:
        print(f"Fruta: {i} - Preço: R${preco[frutas.index(i)]:.2f}")