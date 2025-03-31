from Ej1Prestamo import Prestamo
from Ej1Socio import Socio
from Ej1Fecha import Fecha
from Ej1Libro import Libro

class testPrestamoSocioFecha:

    @staticmethod

    def testNro1():
        
        libro_1=Libro("100 años de soledad","Garcia Marquez","DeBolsillo","A")
        
        print(f"Nombre:{libro_1.obtenerNombre()},Autor:{libro_1.obtenerAutor()},Editorial:{libro_1.obtenerEditorial()},Categoria:{libro_1.obtenerCategoria()}")
        print("*"*25)
        nSocio=Fecha(22,10,2004)
        socio_1=Socio("Fausto",nSocio)
        print(socio_1.__str__())
        print("*"*25)
        fechaActual=Fecha(2,10,2024)
        socio_1.establecerPenalizacion(fechaActual)
        fechaPrestamo=Fecha(27,1,2024)
        prestamo_1=Prestamo(libro_1,fechaPrestamo,3,socio_1)
        fechaDevolucion=Fecha(20,10,2024)
        prestamo_1.establecerFechaDevolucion(fechaDevolucion)
        print(prestamo_1.Penalizacion(socio_1)) 
        
        if prestamo_1.estaAtrasado(fechaActual):
            print("Te atrasaste man")
        else:
            print("Todavia estas a tiempo")
              
        if socio_1.estaHabilitado(fechaActual):
            print("Habilitadicimo")
        else:
            print("Garca! Oportunista!")    
        
            


if __name__ == "__main__":
    testPrestamoSocioFecha.testNro1()