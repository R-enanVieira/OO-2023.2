from OO.miniprojeto2.formas_geometrica.forma import Forma

class Trapezio(Forma):
    def __init__(self, base_maior, base_menor, altura):
        self.base_maior = base_maior
        self.base_menor = base_menor
        self.altura = altura

    def calcular_area(self):
        return 0.5 * (self.base_maior + self.base_menor) * self.altura

