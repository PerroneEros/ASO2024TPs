from classInmueble import Inmueble
from classDepartamento import Departamento
from classPropietario import Propietario
from classQuinta import Quinta
from classInmoviliaria import Inmoviliaria

class TesterInmobiliaria():

    def test():

        propietario1 = Propietario("Marta")
        propietario2 = Propietario("Juan")

        print("Probar Inmobiliaria")
        inmobiliaria = Inmoviliaria(None)

        inmueble1 = Inmueble(122, "Salta 365", propietario1, 100, 120)
        depa1 = Departamento(123, "Salta 365", propietario1, 5, 10, 16000, False)
        quinta1 = Quinta(125, "Quinta de Palito", propietario2, 300, 500, 200)

        # Insertar propiedades
        inmobiliaria.insertar(inmueble1)
        inmobiliaria.insertar(depa1)
        inmobiliaria.insertar(quinta1)

        # Eliminar propiedad
        inmobiliaria.eliminar(inmueble1)

        # Comprobar si hay inmuebles
        print(f"¿Hay inmuebles? {inmobiliaria.hayInmuebles()}")

        # Contar propiedades con menos de 200 metros
        print(f"Propiedades con menos de 200 metros cuadrados: {inmobiliaria.contarPropiedadesMasMetros(200)}")

        # Propiedad con mayor precio de venta
        mayor_precio = inmobiliaria.mayorPrecioVenta()
        if mayor_precio:
            print(f"Propiedad con mayor precio de venta: {mayor_precio.obtenerDomicilio()}")
        else:
            print("No hay propiedades disponibles.")

if __name__ == "__main__":
    TesterInmobiliaria.test()
