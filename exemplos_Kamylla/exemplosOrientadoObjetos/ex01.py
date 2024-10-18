class TV():

    def __init__(self, cor, tamanho):
        self.cor = cor
        self.ligada = False
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 10

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal

    def mudar_volume(self):
        pass

    def ligar_desligar(self):
        pass

#programa
tv_sala = TV(cor = "preta", tamanho = 55)
tv_quarto = TV("branca", 29)

tv_sala.mudar_canal("Globo")
tv_quarto.mudar_canal("Youtube")


# tv_sala.mudar_canal()

print(tv_sala.canal)
print(tv_quarto.canal)