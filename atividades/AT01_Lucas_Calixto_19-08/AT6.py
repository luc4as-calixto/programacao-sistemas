def converter_quilometros_para_metros(quilometros):
    #converte km para metros
    metros = quilometros * 1000
    return metros

try:
    #solicita o km para o usuário
    quilometros = float(input("Digite a distância em quilômetros: "))   
    #chama a função
    metros = converter_quilometros_para_metros(quilometros)
    print("metros:", metros)
    #se tiver um erro ele coloca a mensagem
except ValueError:
    print("Entrada inválida!")