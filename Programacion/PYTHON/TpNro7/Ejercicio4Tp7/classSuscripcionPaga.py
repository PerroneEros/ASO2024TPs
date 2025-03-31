"""
Clase Suscripcion Paga
"""
from classSuscripcion import Suscripcion

class SuscripcionPaga(Suscripcion):
    
    def __init__(self, nombre:str, email:str, telefono:str, maxDispositivos:int, dispositivos:list):
        super().__init__(nombre, email, telefono)
        self.__maxDispositivos=maxDispositivos
        self.__dispositivos=dispositivos
        
    #Comandos
    def reproducirMusica(self):
        pass
    
    def descargarMusica(self):
        pass
    
    def elegirCancion(self):
        pass
    
    def elegirCancion(self):
        pass
    
    def habilitarDispositivo(self):
        pass
    
    def establecerMaxDispositivos(self, maxDispositivos:int):
        pass
    
    def establecerDispositivos(self, dispositivos:list):
        pass
    
    #Consultas
    
    def obtenerMaxDispositivos(self)->int:
        return self.__maxDispositivos
    
    def obtenerDispositivos(self)->list:
        pass    
        
