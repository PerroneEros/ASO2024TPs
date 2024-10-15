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
from claseFecha import Fecha
from calseOrganizador import Organizador
from claseParticipante import Participante

class Evento:
    
    def __init__ (self, nombre:str, fecha:'Fecha', descripcion:str, organizadorAsignado:'Organizador'=None):
        self.__nombre=nombre
        self.__fecha=fecha
        self.__descripcion=descripcion
        self.__organizadorAsignado=organizadorAsignado
        self.__participantes=None
        
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerFecha(self)->Fecha:
        return self.__fecha
    
    def obtenerDescripcion(self)->str:
        return self.__descripcion
    
    def obtenerParticipantesNombres(self) -> list:
        """Retorna una lista con los nombres de los participantes del evento."""
        if not self.__participantes:
            return []
        return [participante.obtenerNombre() for participante in self.__participantes]
    
    
    def obtenerOrganizador(self)->Organizador:
        return self.__organizadorAsignado
    
    #Comandos

    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str):
            ValueError("El nombre debe ser un string")
        else:
            self.__nombre=nombre
            
    def establecerFecha(self, fecha:'Fecha'):
        if not isinstance(fecha, Fecha):
            ValueError("El objeto pasado por parametro debe ser de tipo fecha")
        else:
            self.__fecha=fecha            
            
    def establecerDescripcion(self, descripcion:str):
        if not isinstance(descripcion, str):
            ValueError("El descripcion debe ser un string")
        else:
            self.__descripcion=descripcion
            
    def anotarParticipante(self, participante: 'Participante'):
        """Anota un participante al evento."""
        if not isinstance(participante, Participante):
            raise ValueError("El objeto que intentas ingresar no es un participante")
        else:
            if self.__participantes==None:
                self.__participantes=[]
                self.__participantes.append(participante)
            elif participante not in self.__participantes:
                self.__participantes.append(participante)
            else:
                print(f"{participante.obtenerNombre()} ya está asignado a este evento.")
                
    def asignarOrganizador(self, organizador: 'Organizador'):
        """Asigna un organizador al evento."""
        if not isinstance(organizador, Organizador):
            raise ValueError("El objeto que intentas ingresar no es un organizador")
        self.__organizadorAsignado = organizador
    
    def __str__(self):
        return f"Nombre: {self.__nombre}, Fecha: {self.__fecha}, Descripcion: {self.__descripcion}, Participantes: {self.__participantes}, Organizador: {self.__organizador}"