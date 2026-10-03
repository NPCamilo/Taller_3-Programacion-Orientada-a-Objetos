"""
Cree una clase “Triangulo” donde me calcule área, perímetro y un método que me diga que tipo de triangulo es.
"""

import math

class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def es_valido(self):
        return (self.a + self.b > self.c and
                self.a + self.c > self.b and
                self.b + self.c > self.a)

    def perimetro(self):
        if not self.es_valido():
            return 0
        return self.a + self.b + self.c

    def area(self):
        if not self.es_valido():
            return 0
        s = self.perimetro() / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

    def tipo_triangulo(self):
        if not self.es_valido():
            return "No es un triángulo válido"
        if self.a == self.b == self.c:
            return "Equilátero"
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            return "Isósceles"
        else:
            return "Escaleno"


if __name__ == "__main__":
    t1 = Triangulo(3, 4, 5)
    print(f"Tipo: {t1.tipo_triangulo()}, Área: {t1.area():.2f}, Perímetro: {t1.perimetro()}")
    t2 = Triangulo(5, 5, 5)
    print(f"Tipo: {t2.tipo_triangulo()}, Área: {t2.area():.4f}, Perímetro: {t2.perimetro()}")
