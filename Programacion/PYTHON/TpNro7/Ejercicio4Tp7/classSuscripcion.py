from abc import ABC, abstractmethod

class Suscripcion(ABC):
    
    def __init__ (self, nombre:str, email:str, telefono:str):
        self._nombre=nombre
        self._email=email
        self._telefono=telefono
        
    #Comandos
    def establecerNombre(self, nombre:str):
        pass
    
    def establecerEmail(self, email:str):
        pass
    
    def establecerTelefono(self, telefono:str):
        pass
    
    #Consultas
    
    def obtenerNombre(self)->str:
        return self._nombre
    
    def obtenerEmail(self)->str:
        return self._email
    
    def obtenerTelefono(self)->str:
        return self._telefono
    
    @abstractmethod
    def reproducirMusica(self):
        pass    