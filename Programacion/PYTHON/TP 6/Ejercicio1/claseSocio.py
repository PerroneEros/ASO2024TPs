'''1) En una Biblioteca se tiene un sistema que mantiene información de los libros, los 
socios, y los préstamos que se realizan. De los libros se mantiene el nombre, su 
autor, la editorial y la categoría a la que pertenecen, que puede ser A, B o C. De los 
socios se mantiene el nombre, la fecha de nacimiento y la fecha de penalización (si 
es que hubiere) indicando hasta qué fecha no puede retirar libros. 
Un socio puede retirar libros, cuando se realiza el préstamo se almacena al socio, el 
libro, la fecha en que se realiza el préstamo y la cantidad de días que se autoriza el 
préstamo. Cuando el socio devuelve el libro se almacena en el préstamo la fecha de 
la devolución y se revisa si el préstamo fue devuelto a tiempo o si se excedió en el 
plazo. En el caso que el libro se haya devuelto fuera del plazo permitido se calcula 
una penalización al socio, que puede ser de 3 días si se atrasó menos de una 
semana (menos de 7 días), 5 días si se atrasó menos de tres semanas (menos de 
21 días) y 10 días si se atrasó 3 semanas o más (21 días o más). Además, si el libro 
tiene categoría A los días de penalización se duplican. 
El préstamo de un libro se modela de acuerdo al siguiente diagrama (se utiliza la 
clase Fecha del práctico 5). 
 
En la clase Socio: 
○ el constructor inicializa al socio sin fecha de penalizacion (None) 

○ establecerFechaPenalizacion(fechaHasta: Fecha) actualiza el atributo de 
instancia fechaPenalizacion. 

○ la Consulta estaHabilitado(fecha: Fecha) retorna True cuando no tiene 
fechaPenalizacion o cuando ésta es anterior a la fecha recibida en el 
parámetro. 
'''
from claseFecha import Fecha

class Socio:
    def __init__(self,nombre:str,nacimineto:'Fecha'):
        self.__nombre = nombre
        self.__fechaNacimiento = nacimineto
        self.__fechaPenalizacion = None
    
    def establecerNombre(self,nombre:str):
        self.__nombre = nombre
    
    def establecerFechaNacimiento(self, fecha:'Fecha'):
        self.__fechaNacimiento = fecha
    
    def establecerFechaPenalizacion(self, fechaHasta:'Fecha'):
        self.__fechaPenalizacion = fechaHasta
    #consultas
    def estaHabilitado(self, fecha:'Fecha') -> bool:
        habilitado = False
        if self.__fechaPenalizacion is None or self.__fechaPenalizacion < fecha:
            habilitado = True
        return habilitado
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerFechaNacimiento(self)->'Fecha':
        return self.__fechaNacimiento
    
    def obtenerFechaPenalizacion(self)->'Fecha':
        return self.__fechaPenalizacion
    
    def __str__(self):
        return f"Socio: {self.__nombre}, Fecha de nacimiento: {self.__fechaNacimiento}, Fecha de penalización: {self.__fechaPenalizacion}"








































