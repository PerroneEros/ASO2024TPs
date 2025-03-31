from classSuscripcionGratuita import SuscripcionGratuita
from classSuscripcionPaga import SuscripcionPaga

class Dispositivo():
    
    def __init__(self, id:int, nombre:str, tipo:str):
        self.__id=id
        self.__nombre=nombre
        self.__tipo=tipo
        
    #Comandos
    def establecerId(self, id:int):
        pass
    
    def establecerNombre(self, nombre:str):
        pass
    
    def establecerTipo(self, tipo:str):
        pass
    
    #Consultas
    def obtenerId(self)->int:
        return self.__id
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerTipo(self)->str:
        return self.__tipo    