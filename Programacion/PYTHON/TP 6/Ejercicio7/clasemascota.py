'''7) Un refugio de animales nos pide diseñar un sistema simple para gestionar las 
mascotas en el refugio. El sistema permitirá registrar mascotas y sus cuidadores, así 
como asignar y gestionar el cuidado de las mascotas. 
 
Mascota: Cada mascota tiene un nombre, una especie (por ejemplo, perro, gato), 
una edad y una descripción. Las mascotas pueden ser asignadas a un cuidador. 

Cuidador: Cada cuidador tiene un nombre, una dirección y un número de teléfono. 
Los cuidadores pueden ser asignados a una o más mascotas. 
 
A. Crea un diagrama de clases que incluya dos clases principales: Mascota y 
Cuidador. 
La clase Mascota debe tener los atributos: nombre, especie, edad, 
descripción. 
La clase Cuidador debe tener los atributos: nombre, dirección, teléfono y un 
método para asignar mascotas. 
B. Implementar las clases con python '''

class Mascota():
    def __init__(self,nombre:str,especie:str,edad:int,descripcion:str):
        self.__nombre = nombre
        self.__especie = especie
        self.__edad = edad
        self.__descripcion = descripcion

    #comandos
    def establecerNombre(self,nombre:str):
        if isinstance not in self.__nombre:
            raise ValueError("El nombre debe ser una cadena de caracteres.")
        else:
            self.__nombre = nombre
    
    def establecerEspecie(self, especie:str):
        if isinstance not in self.__especie:
            raise ValueError("La especie debe ser una cadena de caracteres.")
        else:
            self.__especie = especie
    
    def establecerEdad(self, edad:int):
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("La edad debe ser un número entero positivo.")
        else:
            self.__edad = edad
    
    def establecerDescripcion(self, descripcion:str):
        if isinstance not in self.__descripcion:
            raise ValueError("La descripción debe ser una cadena de caracteres.")
        else:
            self.__descripcion = descripcion
            
    #comandos
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerEspecie(self) -> str:
        return self.__especie
    
    def obtenerEdad(self) -> int:
        return self.__edad
    
    def obtenerDescripcion(self) -> str:
        return self.__descripcion
    
    def __str__(self):
        return f"Mascota: {self.__nombre}, Especie: {self.__especie}, Edad: {self.__edad}, Descripción: {self.__descripcion}"
    
