class ContaCorrente():

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))
        pass

    def depositar_dinheiro(self, valor):
        self.saldo += valor
        pass

    def limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self.limite_conta():
            print('Você não tem saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
            self.saldo -= valor
        pass

#Programa

conta_lira = ContaCorrente("Lira", "111.222.333.45")
conta_lira.consultar_saldo()

#Depositar um dinheirinho na conta:
conta_lira.depositar_dinheiro(10000)
conta_lira.consultar_saldo()

#Sacando um dinheirinho da conta:
conta_lira.sacar_dinheiro(100000)
conta_lira.consultar_saldo()

print('Saldo da conta é',conta_lira.saldo)
print(conta_lira.cpf)