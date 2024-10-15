'''
8) Un organizador de eventos nos pide diseñar un sistema simple para gestionar los 
eventos. El sistema debe permitir registrar eventos, participantes y organizadores, y 
asignar participantes a eventos y organizadores a eventos. 
Requerimientos 

Evento: Cada evento tiene un nombre, una fecha y una descripción. Los eventos 
pueden tener múltiples participantes y un organizador asignado

Participante: Cada participante tiene un nombre, una dirección de correo electrónico 
y un número de teléfono. Los participantes pueden registrarse en uno o más 
eventos. 

Organizador: Cada organizador tiene un nombre, una dirección de correo electrónico 
y una especialidad (por ejemplo, planificación de eventos, catering, músico, DJ, etc.). 
Cada organizador puede estar a cargo de uno o más eventos. 

A. Crea un diagrama de clases que incluya tres clases principales: Evento, 
Participante y Organizador. 
B. Implementa las clases en python 
C.  Crea una clase tester para cada clase implementada '''

class Organizador:
    
    def __init__ (self, nombre:str, correo:str, especialidad:str):
        self.__nombre=nombre
        self.__correo=correo
        self.__especialidad=especialidad
        
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerCorreo(self)->str:
        return self.__correo    
    
    def obtenerEspecialidad(self)->str:
        return self.__especialidad
    

    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str):
            ValueError("El nombre debe ser un string")
        else:
            self.__nombre=nombre           
            
    def establecerCorreo(self, correo:str):
        if not isinstance(correo, str):
            ValueError("El correo debe ser un string")
        else:
            self.__correo=correo
            
    def establecerEspecialidad(self, especialidad:str):
        if not isinstance(especialidad, str):
            ValueError("El especialidad debe ser string")
        else:
            self.__especialidad=especialidad  
    
    def __str__(self):
        return f"Nombre: {self.__nombre}, Correo: {self.__correo}, Especialidad: {self.__especialidad}"