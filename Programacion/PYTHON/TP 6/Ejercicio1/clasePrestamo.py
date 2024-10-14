from claseFecha import Fecha
from claseLibro import Libro
from claseSocio import Socio

'''
En la clase Prestamo: 
establecerFechaDevolucion recibe como parámetro la fecha en la que 
efectivamente se realizó la devolución del libro, y controla si el socio debe 
recibir una penalización, en caso afirmativo se le asigna al socio la fecha de 
penalización. 
○ obtenerFechaDevolución retorna la fecha en la que efectivamente se realizó 
la devolución del libro. 
def estaAtrasado(self, fecha_actual: 'Fecha') -> bool:
    if self.__fechaDevolucion is None:
        fecha_limite = self.__fechaPrestamo + self.__cantDias
        return fecha_actual > fecha_limite
    return False
○ penalizacion calcula la cantidad de días de penalización y devuelve la fecha 
hasta la que corresponde aplicar la penalización, a partir de la fecha de 
devolución, que tiene que estar ligada. La penalización es de 3 días si se 
atrasó menos de una semana, 5 días si se atrasó menos de tres semanas y 
10 días si se atrasó 3 semanas o más. Si el libro tiene categoría A los días de 
penalización se duplican'''

class Prestamo:
    def __init__(self,libro:'Libro',fechaPrestamo:'Fecha',cantDias:int,socio:'Socio'):
         self.__libro = libro
         self.__socio = socio
         self.__fechaPrestamo = fechaPrestamo
         self.__cantDias = cantDias
         self.__fechaDevolucion = None

    def establecerFechaDevolucion(self,fechaDev:'Fecha'):
         self.__fechaDevolucion = fechaDev
         if self.__libro.getCategoria() == 'A' and self.__libro.estaAtrasado(fechaDev):
             penalidad = 3 * self.__libro.penalizacion(fechaDev)
             self.__socio.establecerFechaPenalizacion(self.__fechaDevolucion + penalidad)
    
    def obtenerLibro(self)->'Libro':
         return self.__libro
    
    def obtenerFechaPrestamo(self)->'Fecha':
         return self.__fechaPrestamo
    
    def obtenerFechaDevolucion(self)->'Fecha':
         return self.__fechaDevolucion
    
    def estaAtrasado(self, fechaActual: 'Fecha') -> bool:
        if self.__fechaDevolucion is not None:
            if fechaActual.obtenerAnio() > self.__fechaDevolucion.obtenerAnio():
                atrasado = True
            elif fechaActual.obtenerAnio() == self.__fechaDevolucion.obtenerAnio():
                if fechaActual.obtenerMes() > self.__fechaDevolucion.obtenerMes():
                    atrasado = True
                elif fechaActual.obtenerMes() == self.__fechaDevolucion.obtenerMes(): 
                    
                    if fechaActual.obtenerDia() > self.__fechaDevolucion.obtenerDia():
                        atrasado = True
                    else:
                        atrasado = False
                else:
                    atrasado = False
            else:
                atrasado = False
            
            return atrasado
        return False
    
    def penalizacion(self) ->'Fecha':
        penalidad = 0
        if self.__libro.estaAtrasado(self.__fechaDevolucion):
            if self.__libro.getCategoria() == 'A':
                penalidad = 3 * self.__libro.penalizacion(self.__fechaDevolucion)
            else:
                penalidad = self.__libro.penalizacion(self.__fechaDevolucion)
        return Fecha(self.__fechaDevolucion.obtenerAnio(), self.__fechaDevolucion.obtenerMes(), self.__fechaDevolucion.obtenerDia() + penalidad)

    def toString(self):
        return f"Prestamo: Libro: {self.__libro.getTitulo()}, Fecha de prestamo: {self.__fechaPrestamo}, Fecha de devolución: {self.__fechaDevolucion}, Socio: {self.__socio.obtenerNombre()}"