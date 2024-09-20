def nm():
    nome = input("Digite seu nome: ")
    return nome

def id():
    idade = int(input("Digite sua idade: "))
    return idade

def sal():
    salario = int(input("Digite seu salário: "))
    return salario

def sex():
    sexo = input("Digite seu sexo (M/F): ")
    return sexo

def estciv():
    estadocivil = input("Digite seu estado civil, solteiro(S); Casado(C); Viuvo(V); divorsiado(D): ")
    return estadocivil

nome = nm()
idade = id()
salario = sal()
sexo = sex()
estadocivil = estciv()

if(len(nome) > 3):
    print("Nome valido, ",nome)
else:
    print("Nome inválido")
    nm()

if(idade >= 0) and (idade <=150):
    print("idade valida, ",idade," anos")
else:
    print("idade inválida")
    id()

if(salario >= 0) :
    print("salário valido, R$",salario)
else:
    print("salário inválido")
    sal()

if(sexo == "M") or (sexo == "m") or (sexo == "F") or (sexo == "f"): 
    print("sexo valido, ",sexo)
else:
    print("sexo inválido")
    sex()

if(sexo == "S") or (sexo == "C") or (sexo == "V") or (sexo == "D") or (sexo == "s") or (sexo == "c") or (sexo == "v") or (sexo == "d"): 
    print("estado civil valido, ",estadocivil)
else:
    print("estado civil inválido")
    estciv()