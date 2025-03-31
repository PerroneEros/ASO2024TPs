from classDepartamento import Departamento
from classInmueble import Inmueble
from classPropietario import Propietario
from classQuinta import Quinta

class TesterDepartamento():

    def test():

        propietario1 = Propietario("Marta")

        print("Probar inmueble")
        inmueble1 = Inmueble(122,"Salta 365", propietario1, 12, 10)
        print(inmueble1.precioVenta(1000.0))
        print(inmueble1.costoAlquiler(1000))

        Depa1 = Departamento(123, "Salta 365", propietario1, 5, 10, 16000, False)
        print(f"La venta de el departamento de {Depa1.obtenerDomicilio()} cerro en {Depa1.precioVenta(1000.0)}")
        print(Depa1.costoAlquiler(10000))

        Depa2 = Departamento(124, "Salta 221", propietario1, 5, 10, 16000, True)
        print(Depa2.precioVenta(1000.0))
        print(f"El costo del alquiler de {Depa2.obtenerDomicilio()} es de {Depa2.costoAlquiler(10000)}")

        Quinta1 = Quinta(125, "LaQuinta de Palito", propietario1, 5, 10, 200)
        print(Depa1.precioVenta(1000.0))
        print(f"El costo del alquiler de {Quinta1.obtenerDomicilio()} es de {Quinta1.costoAlquiler(10000)}")

        

if __name__ == "__main__":
    TesterDepartamento.test()