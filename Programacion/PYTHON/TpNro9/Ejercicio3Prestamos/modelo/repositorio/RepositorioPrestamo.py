from modelo.entidades.Prestamo import Prestamo
from datetime import date
import json

class RepositorioPrestamo(): 

    __ruta_archivo = "datos/prestamos.json"

    def __init__(self):
        self.__prestamos = self.__cargarTodos()

    def __cargarTodos(self):
        lista = []
        try:
            with open(RepositorioPrestamo.__ruta_archivo, 'r') as file:
                prestamos = json.load(file)
                for p in prestamos:
                    lista.append(Prestamo.fromDiccionario(p))
        except FileNotFoundError:
            print("No se encontró el archivo con datos de prestamos.")
        except json.JSONDecodeError:
            print("Error en el formato del archivo JSON.")
        return lista

    def __guardarTodos(self):
        try:
            lista = [prestamo.toDiccionario() for prestamo in self.__prestamos]
            with open(RepositorioPrestamo.__ruta_archivo, 'w') as file:
                json.dump(lista, file, indent=4)
        except IOError:
            print("Error al guardar los datos de los socios.")
    
    def obtenerTodos(self) -> list:
        return self.__prestamos

    def agregar(self, nuevoPrestamo:'Prestamo'):
        if not isinstance(nuevoPrestamo, Prestamo):
            raise TypeError("El objeto debe ser de tipo prestamo")
        self.__prestamos.append(nuevoPrestamo)
        self.__guardarTodos()
        
    def estaDevuelto(self, otroPrestamo:'Prestamo') -> bool:
        if not isinstance(otroPrestamo, Prestamo):
            raise TypeError("El objeto debe ser de tipo prestamo")
        hoy = date.today()
        if otroPrestamo.obtenerFechaDeDevolucion() > hoy:
            return False
        else:
            return True
        
    def existe(self, socio_dni:int, libro_isbn:int, fecha_retiro:date)-> bool:
        for prestamo in self.__prestamos:
            if socio_dni == prestamo.obtenerSocioDNI() and libro_isbn==prestamo.obtenerISBN() and fecha_retiro==prestamo.obtenerFechaDeRetiro():
                return True
        return False  
    
    def existePrestamoConID(self, id:int)->bool:
        for prestamo in self.__prestamos:    
            if id == prestamo.obtenerID():
                return True
        return False          

    def obtenerPrestamo(self, socio_dni:int, libro_isbn:int, fecha_retiro:date)-> 'Prestamo':
        for prestamo in self.__prestamos:
            if socio_dni == prestamo.obtenerSocioDNI() and libro_isbn==prestamo.obtenerISBN() and fecha_retiro==prestamo.obtenerFechaDeRetiro(): 
                return prestamo
        return None
    
    def obtenerPrestamoPorID(self, id:int)->'Prestamo':
        for prestamo in self.__prestamos:    
            if id == prestamo.obtenerID():
                return prestamo
        return None 
    
    def modificarPorID(self, id:int, socio_dni:int, libro_isbn:int, fecha_retiro:date, cant_dias:int, fecha_devolucion:date):
        for prestamo in self.__prestamos:
            if id == prestamo.obtenerID():
                prestamo.establecerSocioDNI(socio_dni)
                prestamo.establecerLibroISBN(libro_isbn)
                prestamo.establecerFechaRetiro(fecha_retiro)
                prestamo.establecerCantDias(cant_dias)
                prestamo.establecerFechaDevolucion(fecha_devolucion)

    def eliminarID(self, id: int):
        for prestamo in self.__prestamos:
            if id == prestamo.obtenerID():
                self.__prestamos.remove(prestamo)
                self.__guardarTodos()
                return True
        return False
   

    def cantidadDeLibrosSinDevolver(self, ISBN: int) -> int:
        hoy = date.today()
        count = 0
        for prestamo in self.__prestamos:
            if prestamo.obtenerISBN() == ISBN and prestamo.obtenerFechaDeDevolucion() > hoy:
                count += 1    
        return count


    def actualizarPrestamos(self):
        self.__prestamos = self.__cargarTodos()