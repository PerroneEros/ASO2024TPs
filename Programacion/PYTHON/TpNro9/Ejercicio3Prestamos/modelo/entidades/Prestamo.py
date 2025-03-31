"""
Cada préstamo tiene un número de identificación, que es único y se genera de forma
incremental. El préstamo lo registra el personal de la biblioteca cuando un socio
retira un libro de la biblioteca y en ese momento se registra el DNI del socio, el ISBN
del libro que retira, y la fecha. Luego cuando el libro es devuelto se le establece la
fecha de devolución (mediante la ruta de modificación de un préstamo).

Cada vez que se intenta registrar un préstamo se debe verificar que el libro
solicitado posea ejemplares disponibles para ser prestados, y en caso que no
hubiera ejemplares disponibles debe mostrar un mensaje indicando “El libro
solicitado no tiene ejemplares disponibles para prestar”.

Observación: Como los préstamos contienen datos que referencian a libros y socios
se debe tener precaución con la eliminación de las instancias de libros y socios:
antes de eliminar una instancia se debe verificar que no esté registrada en un
préstamo. Es decir: no se debe poder eliminar un socio (o un libro) que está
registrado en un préstamo
"""

from datetime import date

class Prestamo:
    
    __ultimoID=0
    
    @classmethod
    def obtenerNuevoId(cls)->int:
        cls.__ultimoID+=1
        return cls.__ultimoID
    
    @classmethod
    def obtenerUltimoID(cls)->int:
        return cls.__ultimoID
    
    @classmethod
    def establecerUltimoID(cls, id):
        if not isinstance(id, int) or id<0:
            raise ValueError
        cls.__ultimoID = id
        
    @classmethod
    def fromDiccionario(cls, data:dict)->"Prestamo":
        if "id" in data:
            return cls(data["socio_dni"], data["libro_isbn"], data["fecha_retiro"], data["cant_dias"], data["fecha_devolucion"], data["id"])
        else:
            return cls(data["socio_dni"], data["libro_isbn"], data["fecha_retiro"], data["cant_dias"], data["fecha_devolucion"])  
    
    def __init__(self, socio_dni:int, libro_isbn:int, fecha_retiro:date, cant_dias:int, fecha_devolucion:date, id:int=None):
        if not isinstance(socio_dni, int) or socio_dni<0:
            raise TypeError("El nro de dni del socio debe ser un valor entero positivo")
        if not isinstance(libro_isbn, int) or libro_isbn<0:
            raise TypeError("Isbn del libro debe ser un entero positivo")
        if not isinstance(fecha_retiro, date):
            raise TypeError("La fecha de retiro debe ser de tipo date")
        if not isinstance(cant_dias, int) or cant_dias<0:
            raise TypeError("La cantidad de dias debe ser un entero positivo")
        if not isinstance(fecha_devolucion, date):
            raise TypeError("La fecha de devolucion debe ser un date")
        if id != None:
            self.__id=id
        else:
            self.__id = Prestamo.obtenerNuevoId()
        self.__socio_dni=socio_dni
        self.__libro_isbn=libro_isbn
        self.__fecha_retiro=fecha_retiro
        self.__cant_dias=cant_dias
        self.__fecha_devolucion=fecha_devolucion
       
    #Setters   
        
    def establecerSocioDNI(self, dni:int):
        if isinstance(dni,int) or dni<0:
            return TypeError("El dni debe ser un entero positivo")
        self.__socio_dni=dni
        
    def establecerLibroISBN(self, libro_isbn:int):
        if isinstance(libro_isbn, int) or libro_isbn<0:
            return TypeError("El ISBN del libro debe ser un entero positivo") 
        self.__libro_isbn=libro_isbn
        
    def establecerFechaRetiro(self, fecha:date):
        if isinstance(fecha, date):
            return TypeError("La fecha debe ser de tipo date")
        self.__fecha_retiro=fecha
        
    def establecerCantDias(self, cant:int):
        if isinstance(cant, int) or cant<0:
            return TypeError("La cantidad de dias debe ser un entero positivo")
        self.__cant_dias=cant
        
    def establecerFechaDevolucion(self, fecha:date):
        if isinstance(fecha, date):
            raise TypeError("La fecha debe ser de tipo date")
        self.__fecha_devolucion=fecha
                       
    #Getters                   
                       
    def obtenerSocioDNI(self)->int:
        return self.__socio_dni
    
    def obtenerISBN(self)->int:
        return self.__libro_isbn
    
    def obtenerFechaDeRetiro(self)->date:
        return self.__fecha_retiro
    
    def obtenerCantDias(self)->int:
        return self.__cant_dias
    
    def obtenerFechaDeDevolucion(self)->date:
        return self.__fecha_devolucion  
    
    def obtenerID(self)->int:
        return self.__id
    
    def esIgual(self, otro:'Prestamo')->bool:
        if self.__id == otro.obtenerID() and self.__socio_dni == otro.obtenerSocioDNI():
            return True
        else:
            return False
        
    def toString(self):
        return (f"Id: {self.__id}, socioDni: {self.__socio_dni}, libroIsbn: {self.__libro_isbn}, "
                f"fechaRetiro: {self.__fecha_retiro}, cantDias: {self.__cant_dias}, "
                f"fechaDevolucion: {self.__fecha_devolucion or 'No devuelto'}")

def toDiccionario(self) -> dict:
        return {
            "id": self.__id,
            "socio_dni": self.__socio_dni,
            "libro_isbn": self.__libro_isbn,
            "fecha_retiro": self.__fecha_retiro,
            "cant_dias": self.__cant_dias,
            "fecha_devolucion": self.__fecha_devolucion
        }
              