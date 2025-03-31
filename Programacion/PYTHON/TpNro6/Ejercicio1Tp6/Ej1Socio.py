"""
    Un socio puede retirar libros, cuando se realiza el préstamo se almacena al socio, el
    libro, la fecha en que se realiza el préstamo y la cantidad de días que se autoriza el
    préstamo. Cuando el socio devuelve el libro se almacena en el préstamo la fecha de
    la devolución y se revisa si el préstamo fue devuelto a tiempo o si se excedió en el
    plazo. En el caso que el libro se haya devuelto fuera del plazo permitido se calcula
    una penalización al socio, que puede ser de 3 días si se atrasó menos de una
    semana (menos de 7 días), 5 días si se atrasó menos de tres semanas (menos de
    21 días) y 10 días si se atrasó 3 semanas o más (21 días o más). Además, si el libro
    tiene categoría A los días de penalización se duplican.

    En la clase Socio:
    ○-> el constructor inicializa al socio sin fecha de penalizacion (None)
    ○-> establecer__fechaPenalizacion(fechaHasta: Fecha) actualiza el atributo de
    instancia __fechaPenalizacion.
    ○-> la Consulta estaHabilitado(fecha: Fecha) retorna True cuando no tiene
    __fechaPenalizacion o cuando ésta es anterior a la fecha recibida en el
    parámetro
"""    

from Ej1Fecha import Fecha

class Socio:

    # Constructor
    def __init__(self, nombre: str, nacimiento: 'Fecha'):
        self.__nombre = nombre
        self.__nacimiento = nacimiento
        self.__fechaPenalizacion = None 

    def establecerNombre(self, nombre: str):
        self.__nombre = nombre

    def establecerFechaNacimiento(self, fecha: 'Fecha'):
        self.__nacimiento = fecha

    def establecerPenalizacion(self, fechaHasta: 'Fecha'):
        self.__fechaPenalizacion = fechaHasta

    def estaHabilitado(self, fecha: 'Fecha') -> bool:
        habilitado = False 

        if self.__fechaPenalizacion is not None:
            if (fecha.obtenerAnio() > self.__fechaPenalizacion.obtenerAnio() or
                (fecha.obtenerAnio() == self.__fechaPenalizacion.obtenerAnio() and
                (fecha.obtenerMes() > self.__fechaPenalizacion.obtenerMes() or
                (fecha.obtenerMes() == self.__fechaPenalizacion.obtenerMes() and
                fecha.obtenerDia() > self.__fechaPenalizacion.obtenerDia())))):
                habilitado = True
            else:
                habilitado = False

        return habilitado


    def obtenerFechaNacimiento(self) -> 'Fecha':
        return self.__nacimiento

    def obtenerFechaPenalizacion(self) -> 'Fecha':
        return self.__fechaPenalizacion

    def __str__(self) -> str:
        return f"Socio: {self.__nombre}, Nacimiento: {self.__nacimiento}, Penalización: {self.__fechaPenalizacion}"
