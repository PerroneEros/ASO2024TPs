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

class Participante:
    def __init__ (self, nombre:str, telefono:str, correo:str):
        self.__nombre=nombre
        self.__telefono=telefono
        self.__correo=correo
        
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerTelefono(self)->str:
        return self.__telefono
    
    def obtenerCorreo(self)->str:
        return self.__correo
    
    #def eventosIncriptos(self)->Evento:
    #    return [Evento.obtenerNombre() for Evento in self.__eventos]
    
    #Comandos

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
            
    def establecerTelefono(self, telefono:str):
        if not isinstance(telefono, str):
            ValueError("El telefono debe ser string")
        else:
            self.__telefono=telefono     

