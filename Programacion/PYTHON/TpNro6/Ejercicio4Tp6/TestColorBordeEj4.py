"""
4) Dada la implementación de las clases Color y Borde, y el siguiente fragmento de
código:
C1 = Color(150, 150, 150)
C2 = Color(150, 150, 150)
B1 = Borde(1,C1)
B2 = Borde(1,C2)
B3 = B2.clonar()
B4 = Borde(B2.obtenerGrosor(), B2.obtenerColor())
print( B2 == B3)
print( B2 == B4)
print(B2.esIgualQue(B1))
print(B2.esIgualQue(B3))
print(B2.obtenerGrosor() == B1.obtenerGrosor() and
B2.obtenerColor() == B1.obtenerColor())
print(B2.obtenerGrosor() == B3.obtenerGrosor() and
B2.obtenerColor() == B3.obtenerColor())
print(B2.obtenerGrosor() == B1.obtenerGrosor() and
B2.obtenerColor().equals(B1.obtenerColor()))
print(B2.obtenerGrosor() == B4.obtenerGrosor() and
B2.obtenerColor().equals(B4.obtenerColor()))
"""

from ClaseColor import color
from ClaseBorde import borde

class testColorBorde:
    
    @staticmethod

    def test():
        C1 = color(150, 150, 150)
        C2 = color(150, 150, 150)
        B1 = borde(1,C1)
        B2 = borde(1,C2)
        B3 = B2.clonar()
        B4 = borde(B2.obtenerGrosor(), B2.obtenerColor())
        print( B2 == B3)
        print( B2 == B4)
        print(B2.esIgualQue(B1))
        print(B2.esIgualQue(B3))
        
        print(B2.obtenerGrosor() == B1.obtenerGrosor() and B2.obtenerColor() == B1.obtenerColor())

        print(B2.obtenerGrosor() == B3.obtenerGrosor() and B2.obtenerColor() == B3.obtenerColor())

        print(B2.obtenerGrosor() == B1.obtenerGrosor() and B2.obtenerColor() == B1.obtenerColor())

        print(B2.obtenerGrosor() == B4.obtenerGrosor() and B2.obtenerColor() == B4.obtenerColor())
        
        
if __name__ == "__main__":
    testColorBorde.test()        