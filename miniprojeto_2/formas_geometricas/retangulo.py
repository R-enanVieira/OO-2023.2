from OO.miniprojeto2.formas_geometrica.forma import Forma

class Retangulo(Forma):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura

