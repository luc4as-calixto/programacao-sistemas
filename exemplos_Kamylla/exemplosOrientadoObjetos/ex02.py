from datetime import datetime
import pytz

class ContaCorrente():

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))
        pass

    def depositar_dinheiro(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
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
            self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))
        pass

    def consultar_historico_transacoes(self):
        print("Histórico de transações:")
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))

#Programa

conta_lira = ContaCorrente("Lira", "111.222.333.45", "1", "1234567")
conta_lira.consultar_saldo()

conta_maelira = ContaCorrente("beth", "222.333.444.55", 5555, 656565)
conta_maelira.consultar_saldo()
conta_lira.transferir(1000, conta_maelira)

#Depositar um dinheirinho na conta:
conta_lira.depositar_dinheiro(10000)
conta_lira.consultar_saldo()

#Sacando um dinheirinho da conta:
conta_lira.sacar_dinheiro(1000)
conta_lira.consultar_saldo()


print('Saldo da conta é',conta_lira.saldo)
print(conta_lira.cpf) 

conta_lira.consultar_historico_transacoes() 