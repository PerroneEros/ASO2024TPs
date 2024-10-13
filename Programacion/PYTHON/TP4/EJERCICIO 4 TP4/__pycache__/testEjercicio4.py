from Ejercicio4 import Automovil
import random 

class TestAutomovil:
    @staticmethod

    def test():
        marca = input("ingresa la marca del auto:")
        modelo = input("ingrese modelo del auto:")
        anio =int(input("ingrese el año del auto:"))
        VelocidadMaxima = float(input("ingrese la velocidad maxima:"))
    
        auto1 = Automovil(marca,modelo,anio,VelocidadMaxima,0)
    
        cantidad = int(input("ingrese la cantidad de interacciones:"))

        for i in range(cantidad):
            numero = random.randint(0,3)

            if numero == 0:
                print(f"el auto esta yendo a a {auto1.obtenerVelocidadActual()} ")
                auto1.acelerar(20)
                print(f"ahora el auto esta yendo a {auto1.obtenerVelocidadActual()}")
            elif numero == 1:
                print(f"el auto esta yendo a b {auto1.obtenerVelocidadActual()}")
                auto1.desacelerar(15)
                print(f"el auto desaselero, ahora esya yendo a b {auto1.obtenerVelocidadActual()}")
            elif numero == 2:
                print(f"agarrate que freno a 0 pa")
                auto1.frenarPorCompleto()
                print(f"el auto freno a 0")
            elif numero == 3:
                print(f"faltan {auto1.calcularMinutosParaLlegar(50)} minutos para llegar")

if __name__ == "__main__":
    TestAutomovil.test()