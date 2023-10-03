import math
from OO.miniprojeto2.formas_geometrica.forma import Forma

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio

    def calcular_diametro(self):
        return 2 * self.raio
