def vender_passagem():
    lugar = int(input("Digite o lugar que deseja comprar: (0-49)"))
    if lugar < 0 or lugar > 49:
        print("Lugar inválido")
        vender_passagem()

    print()

    if lugares[lugar] == "vendido":
        print("Lugar indisponível")
        print("Tente outro lugar")
        vender_passagem()
    else:
        lugares[lugar] = "vendido"
        print("Lugar vendido com sucesso")
    for i in range(50):
            print(f"{i}º lugar: {lugares[i]}")
    
    print()
        
    resp = str(input("deseja comprar outra passagem?(S/N)")).upper()

    if resp == "S":
        vender_passagem()
    elif resp == "N":
        print("Obrigado por comprar conosco")
        print(f"{i}º lugar: {lugares[i]}")
    else:
        print("Opção inválida")
        vender_passagem()

lugares = ["disponivel" for j in range(50)]

for i in range(50):
    print(f"{i}º lugar: {lugares[i]}")
vender_passagem()