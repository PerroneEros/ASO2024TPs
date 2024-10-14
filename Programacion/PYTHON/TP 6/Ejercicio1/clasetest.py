from clasePrestamo import Prestamo
from claseSocio import Socio
from claseFecha import Fecha
from claseLibro import Libro


class testPrestamoSocioFecha:
    @staticmethod
    def testNro1():
        # Crear y mostrar información del libro
        libro_1 = Libro("100 años de soledad", "Garcia Marquez", "DeBolsillo", "A")
        print(f"Libro: Nombre:{libro_1.obtenerNombre()}, Autor:{libro_1.obtenerAutor()}, "
              f"Editorial:{libro_1.obtenerEditorial()}, Categoria:{libro_1.obtenerCategoria()}")
        print("*"*25)
        
        # Crear y mostrar información del socio
        fecha_nacimiento_socio = Fecha(22, 10, 2004)
        socio_1 = Socio("Fausto", fecha_nacimiento_socio)
        print(f"Socio: {socio_1}")
        print("*"*25)
        
        # Definir fechas relevantes
        fecha_actual = Fecha(2, 10, 2024)
        fecha_prestamo = Fecha(27, 1, 2024)
        fecha_devolucion = Fecha(20, 10, 2024)
        
        # Crear préstamo
        prestamo_1 = Prestamo(libro_1, fecha_prestamo, 3, socio_1)
        
        # Mostrar fechas
        print(f"Fecha de préstamo: {fecha_prestamo}")
        print(f"Fecha actual: {fecha_actual}")
        print(f"Fecha de devolución: {fecha_devolucion}")
        
        # Establecer fecha de devolución y calcular penalización
        prestamo_1.establecerFechaDevolucion(fecha_devolucion)
        fecha_penalizacion = prestamo_1.penalizacion()
        print(f"Fecha de penalización: {fecha_penalizacion}")
        
        # Verificar si el préstamo está atrasado
        if prestamo_1.estaAtrasado(fecha_actual):
            print("El préstamo está atrasado")
        else:
            print("El préstamo está a tiempo")
        
        # Verificar si el socio está habilitado
        if socio_1.estaHabilitado(fecha_actual):
            print("El socio está habilitado")
        else:
            print("El socio no está habilitado")


if __name__ == "__main__":
    testPrestamoSocioFecha.testNro1()