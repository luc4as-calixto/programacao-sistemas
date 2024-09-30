#classe que reprensenta um contato individual
class Contato:
    #inicializa os atributos do contato
    def __init__(self, nome, endereco, email):
        self.nome = nome
        self.endereco = endereco
        self.email = email

class Agenda:
    def __init__(self):
        #inicializa a lista
        self.contatos = []
    #adiciona o contato
    def adicionar_contato(self, contato):
        self.contatos.append(contato)
     #remore o contato
    def remover_contato(self, contato):
        self.contatos.remove(contato)
    #lista dos contatos
    def listar_contatos(self):
        for contato in self.contatos:
            print("Nome:", contato.nome)
            print("Endereço:", contato.endereco)
            print("E-mail:", contato.email)

#refere-se um objeto na classe
agenda = Agenda()
#cria dois contatos
contato1 = Contato("João", "Rua A, 123", "joao@example.com")
contato2 = Contato("Maria", "Rua B, 456", "maria@example.com")

#adiciona os contatos a agenda
agenda.adicionar_contato(contato1)
agenda.adicionar_contato(contato2)
#lista os contatos
agenda.listar_contatos()
#remove o 1º contato
agenda.remover_contato(contato1)
#lista o contato restante
agenda.listar_contatos()