def paises():
    paisA = int(input("Digite a população A para ultrapassar o país B: "))
    paisB = int(input("Digite a população B que será ultrapassada pelo país A: "))

    if paisA < paisB:

        def taxas():
            taxaA = float(input("Digite a taxa de crescimento do país A em %: "))
            taxaB = float(input("Digite a taxa de crescimento do país B em %: "))

            if taxaA > taxaB:
                taxaA1 = taxaA / 100
                taxaB1 = taxaB / 100

                anos = 0

                def quant():
                    nonlocal paisA, paisB, anos  
                    while paisA < paisB:
                        paisA += paisA * taxaA1
                        paisB += paisB * taxaB1
                        anos += 1

                quant()

                print(f"Para o país A ultrapassar ou igualar o país B serão necessários {anos} anos.")

            else:
                print("")
                print("A taxa do país A deve ser maior que a taxa do país B.")
                taxas() 

        taxas()

    else:
        print("")
        print("A população do país A deve ser menor que a do país B.")
        paises()  

paises()
