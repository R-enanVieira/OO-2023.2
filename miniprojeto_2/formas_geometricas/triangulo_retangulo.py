from OO.miniprojeto2.formas_geometrica.forma import Forma

class TrianguloRetangulo(Forma):
    def __init__(self, c_oposto, c_adjacente, hipotenusa, altura):
        self.c_oposto = c_oposto
        self.c_adjacente = c_adjacente
        self.hipotenusa = hipotenusa
        self.altura = altura

    def calcular_area(self):
        return 0.5 * self.hipotenusa * self.altura

    def calcular_perimetro(self):
        return self.c_adjacente + self.c_oposto + self.hipotenusa
