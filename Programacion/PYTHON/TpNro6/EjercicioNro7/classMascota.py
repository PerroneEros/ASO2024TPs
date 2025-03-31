"""
La clase Mascota debe tener los atributos: nombre, especie, edad,
descripción.
"""

class Mascota():
    #Constructor
    
    def __init__ (self, nombre:str, especie:str, edad:int, descripcion:str):
        self.__nombre=nombre
        self.__especie=especie
        self.__edad=edad
        self.__descripcion=descripcion
        
    #Comandos
    
    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str):
            ValueError("El nombre debe ser un string")
        else:
            self.__nombre=nombre
            
    def establecerEspecie(self, especie:str):
        if not isinstance(especie, str):
            ValueError("La especie debe ser un string")
        else:
            self.__especie=especie
            
    def establecerEdad(self, edad:int):
        if not isinstance(edad, int) or edad<0:
            ValueError("La edad debe ser un entero positivo")
        else:
            self.__edad=edad
            
    def establecerDescripcion(self, descripcion:str):
        if not isinstance(descripcion, str):
            ValueError("El descripcion debe ser un string")
        else:
            self.__descripcion=descripcion
            
    #Consultas
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerEspecie(self)->str:
        return self.__especie
    
    def obtenerEdad(self)->int:
        return self.__edad
    
    def obtenerDescripcion(self)->str:
        return self.__descripcion
                                    