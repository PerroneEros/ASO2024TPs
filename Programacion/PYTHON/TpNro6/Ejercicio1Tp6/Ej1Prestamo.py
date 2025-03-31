    
from Ej1Fecha import Fecha
from Ej1Socio import Socio
from Ej1Libro import Libro

from datetime import date

class Prestamo():

    #Atributos

    #Contructor
    def __init__ (self,libro:'Libro',fechaPrestamo:'Fecha', cantDias:int,socio:'Socio'):
        self.__libro=libro
        self.__fechaPrestamo=fechaPrestamo
        self.__cantDias=cantDias
        self.__socio=socio
        self.__fechaDevolucion=None

    #Comando

    """
    ○-> EstablecerFechaDevolucion recibe como parámetro la fecha en la que
    efectivamente se realizó la devolución del libro, y controla si el socio debe
    recibir una penalización, en caso afirmativo se le asigna al socio la fecha de
    penalización.
    """    

    def establecerFechaDevolucion(self,fechaDev:'Fecha'):
        self.__fechaDevolucion=fechaDev

    #Consulta
    def obtenerLibro(self)->'Libro':
        return self.__libro

    def obtenerFechaPrestamo(self)->'Fecha':
        return self.__fechaPrestamo

    """
    ○-> ObtenerFechaDevolución retorna la fecha en la que efectivamente se realizó
    la devolución del libro.
    """    

    def obtenerFechaDevolucion(self)->'Fecha':
        return self.__fechaDevolucion

    """
    ○-> EstaAtrasado recibe como parámetro la fecha actual y retorna verdadero si el
    libro no se devolvió y ya debería haberse devuelto de acuerdo a la fecha de
    préstamo y la cantidad de días.
    """

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


    """
    ○-> Penalizacion calcula la cantidad de días de penalización y devuelve la fecha
    hasta la que corresponde aplicar la penalización, a partir de la fecha de
    devolución, que tiene que estar ligada. La penalización es de 3 días si se
    atrasó menos de una semana, 5 días si se atrasó menos de tres semanas y
    10 días si se atrasó 3 semanas o más. Si el libro tiene categoría A los días de
    penalización se duplican.
    """

    def Penalizacion(self, esteSocio:'Socio')->'Fecha':
        fechaPenalizable=esteSocio.obtenerFechaPenalizacion()
        fecha1 = date(self.__fechaDevolucion.obtenerAnio(), self.__fechaDevolucion.obtenerMes(), self.__fechaDevolucion.obtenerDia())
        fecha2 = date(fechaPenalizable.obtenerAnio(), fechaPenalizable.obtenerMes(), fechaPenalizable.obtenerDia())
        
        diferencia = (fecha2 - fecha1).days
        
        diasPenalizacion=0
        
        if diferencia<=0:
            print("El libro fue entregado en tiempo y forma")
            diasPenalizacion=0
        elif diferencia < 7:
            diasPenalizacion=3
        elif diferencia >=7 and diferencia < 21:
            diasPenalizacion=5
        else:
            diasPenalizacion=10
            
        if self.__libro.obtenerCategoria()=='A':
            diasPenalizacion=diasPenalizacion*2
        
        print(diasPenalizacion)
        
        DiasMeses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if (fechaPenalizable.obtenerAnio() % 4 == 0 and (fechaPenalizable.obtenerAnio() % 100 != 0 or fechaPenalizable.obtenerAnio() % 400 == 0)):
            DiasMeses[1] = 29 

        Dia=fechaPenalizable.obtenerDia()
        Mes=fechaPenalizable.obtenerMes()
        Anio=fechaPenalizable.obtenerAnio()
        
        while diasPenalizacion > 0:
            diasRestantesMes = DiasMeses[fechaPenalizable.obtenerMes() - 1] - fechaPenalizable.obtenerDia()
        
            if diasPenalizacion > diasRestantesMes:  
                diasPenalizacion -= (diasRestantesMes + 1)  
                Dia = 1
                Mes += 1

                if Mes > 12:  
                    Mes = 1
                    Anio += 1
            else:
                Dia += diasPenalizacion
                diasPenalizacion = 0  
                
        fechaPostPenalizacion=Fecha(Dia,Mes,Anio)
                
        return fechaPostPenalizacion                         