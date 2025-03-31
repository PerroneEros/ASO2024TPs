"""
 3. Hotel: Cada paquete incluye un alojamiento que ofrece información sobre el nombre del
    hotel, la ciudad donde se ubica, una breve descripción, la categoría de estrellas del
    alojamiento y el tipo de pensión (entre las opciones: desayuno, media pensión, pensión
    completa). Los hoteles se identifican mediante el nombre y la ciudad donde se encuentran
    ubicados.
"""

from enum import Enum

class Pension(Enum):
    DESAYUNO = 1
    MEDIA_PENSION = 2
    PENSION_COMPLETA = 3
    
    def toDiccionario(self):
        return self.value
    
    @classmethod
    def fromDiccionario(cls, data):
        return cls(data)

from Ciudad import Ciudad

class Hotel:
    
    #metodos de clase -------------------------------------------------------------------------------------------------
    @classmethod
    def fromDiccionario(cls, data: dict)->"Ciudad":
        if not isinstance(data, dict):
            raise ValueError("El parametro data debe ser un diccionario.")
        return cls(data["nombre"], Ciudad.fromDiccionario(data["ciudad"]), data["descripcion"], data["categoria"], Pension.fromDiccionario(data["pension"]))
    
    #Constructor
    def __init__(self, nombre:str, ciudad:'Ciudad', descripcion:str, categoria:str, pension:'Pension'):
        if not isinstance(nombre, str) or nombre=="" or nombre.isspace():
            raise TypeError("El nombre debe ser un string")
        if not isinstance(ciudad, Ciudad):
            raise TypeError("La ciudad debe ser de tipo ciudad")
        if not isinstance(descripcion, str) or descripcion=="" or descripcion.isspace():
            raise TypeError("La descripcion debe ser de tipo string")
        if not isinstance(categoria, str) or categoria=="" or categoria.isspace():
            raise TypeError("La categoria debe ser un string")
        if not isinstance(pension, Pension):
            raise TypeError("El tipo de la pension debe Pension")
        self.__nombre=nombre
        self.__ciudad=ciudad
        self.__descripcion=descripcion
        self.__categoria=categoria
        self.__pension=pension
        
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerCiudad(self)->'Ciudad':
        return self.__ciudad
    
    def obtenerDescripcion(self)->str:
        return self.__descripcion
    
    def obtenerCategoria(self)->str:
        return self.__categoria
    
    def obtenerTipoPension(self)->str:
        return self.__pension
    
    def esIgualProf(self, otra:"Hotel")->bool:
        return self.__nombre == otra.obtenerNombre() and self.__ciudad == otra.obtenerCiudad()
    
    def toDiccionario(self):
        return {
            "nombre": self.__nombre,
            "ciudad": self.__ciudad.toDiccionario(),
            "descripcion": self.__descripcion,
            "categoria": self.__categoria,
            "pension": self.__pension.toDiccionario()
        }
        