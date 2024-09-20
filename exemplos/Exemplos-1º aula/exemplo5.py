codigo = int(input("Digite o código do funcionário "))
nome = input("DIgite o nome do funcionário ")
salario = float(input("Informe o salario "))
ativo = True

print("")
print("Código: %d " % codigo)
print("Nome: %s " % nome)
print("Salário: %.2f " % salario)
print("Ativo: %r " % ativo)

if salario <= 3000:
    salario = salario + (salario * 0.10)
else: 
    salario = salario + (salario * 0.05)


print("Novo salário: %.2f " % salario)