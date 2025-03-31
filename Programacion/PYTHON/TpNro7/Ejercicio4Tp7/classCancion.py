from classPlaylist import Playlist

class Cancion(Playlist):
    
    def __init__ (self, codigo:int, nombre:str, canCodigo:int, canNombre:str, duracion:int, genero:str):
        super().__init__(codigo, nombre)
        self.__canCodigo=canCodigo
        self.__canNombre=canNombre
        self.__duracion=duracion
        self.__genero=genero
        
    #Comando
    def reproducir(self):
        pass
    
    def establecerCanCodigo(self, codigo:int):
        pass
    
    def establecerCanNombre(self, nombre:str):
        pass
    
    def establecerDuracion(self, duracion:int):
        pass
    
    def establecerGenero(self, genero:str):
        pass
    
    #Consultas
    def obtenerCanCodigo(self)->int:
        return self.__canCodigo
    
    def obtenerCanNombre(self)->str:
        return self.__canNombre
    
    def obtenerDuracion(self)->int:
        return self.__duracion
    
    def obtenerGenero(self)->str:
        return self.__genero
    
    
       