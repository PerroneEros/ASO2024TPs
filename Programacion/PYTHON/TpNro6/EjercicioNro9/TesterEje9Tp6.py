from classEntrada import Entrada
from classAtraccion import Atraccion
from classVisitante import Visitante
from classGuia import Guia
from Fecha import Fecha

class testerAtraccion:
    @staticmethod
    def test():
        fecha1=Fecha(11,10,2024)
        
        #Testear atraccion
        atraccion1 = Atraccion("LaIncreibleBetsy", "MontaniaRusa", "Manija", (1.45) , "Tarde")
        print(atraccion1.obtenerNombre())
        print(atraccion1.obtenerEstMinRequerida())

        #Tester entrada
        entrada1 = Entrada(1, fecha1, "VIP")
        print(entrada1.obtenerTipo())

        #Tester Visitante
        visitante1 = Visitante("Martin Peralta", 15, 1.65, "gordazo37@gmail.com", entrada1)
        print(visitante1.obtenerAltura())
        print(visitante1.obtenerNombre())
        print(visitante1.obtenerAtraccionesVisitadas())

        guia1 = Guia("Marcos Acunia", "Tarde")
        print(guia1.obtenerNombre())
        print(guia1.obtenerTurno())

        guia1.habilitarVisitante(visitante1,atraccion1)
        print(visitante1.obtenerAtraccionesVisitadas())



if __name__ == "__main__":
    testerAtraccion.test()
