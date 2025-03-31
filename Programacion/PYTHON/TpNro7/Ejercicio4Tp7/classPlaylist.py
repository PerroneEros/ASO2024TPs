from classCancion import Cancion

class Playlist():
    
    def __init__(self, codigo:int, nombre:str):
        self._codigo=codigo
        self._nombre=nombre
        
    #Comandos
    def establecerCodigo(self, codigo:int):
        pass
    
    def establecerNombre(self, nombre:str):
        pass
    
    def agregarCancion(cancion:'Cancion'):
        pass
    
    def eliminarCancion(cancion:'Cancion'):
        pass
    
    #Consultas
    def obtenerCodigo(self)->int:
        return self._codigo
    
    def obtenerNombre(self)->str:
        return self._nombre   