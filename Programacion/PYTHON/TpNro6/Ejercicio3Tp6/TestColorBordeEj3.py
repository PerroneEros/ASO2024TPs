"""
3) Dada la implementación de las clases Color y Borde, y el siguiente fragmento de
código:

C1 = Color(150, 150, 150)
C2 = Color(150, 150, 150)
B1 = Borde(1,C1)
B2 = Borde(1,C2)
print(C1 == C2)
print(B1 == B2)
print(C1.esIgualQue(C2))
print(B1.esIgualQue(B2))

A. Dibuje el diagrama de objetos al terminar el bloque de asignaciones.
B. Muestre la salida.
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
        print(C1 == C2)
        print(B1 == B2)
        print(C1.esIgualQue(C2))
        print(B1.esIgualQue(B2))
        
        
if __name__ == "__main__":
    testColorBorde.test()        