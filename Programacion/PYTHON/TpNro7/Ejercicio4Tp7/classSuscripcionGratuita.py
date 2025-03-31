"""
Class Suscripcion Gratuita
"""

from classSuscripcion import Suscripcion

class SuscripcionGratuita(Suscripcion):
    
    def __init__(self, nombre:str, email:str, telefono:str, tiempoSinPublicidad:int, tiempoReproducido:int):
        super().__init__(nombre, email, telefono)
        self.__tiempoSinPublicidad=tiempoSinPublicidad
        self.__tiempoReproducido=tiempoReproducido
        
    #Comandos
    def reproducirMusica(self):
        pass
    
    def interrumpirConPublicidad(self):
        pass
    
    def establecerTiempoSinPublicidad(self, tiempo:int):
        pass
    
    def establecerTiempoReproducido(self, tiempo:int):
        pass
    
    #Consultas
    
    def obtenerTiempoSinPublicidad(self)->int:
        return self.__tiempoSinPublicidad
    
    def obtenerTiempoReproducido(self)->int:
        return self.__tiempoReproducido    