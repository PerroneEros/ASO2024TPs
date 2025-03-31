class Pais():
    
    def __init__ (self, codigo:int, nombre:str, cantidadDispositivos:int):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__cantidadDispositivos=cantidadDispositivos
        
    #Comandos
    def establecerCodigo(self, codigo:int):
        pass
    
    def establecerNombre(self, nombre:str):
        pass
    
    def establecerCantidadDispositivos(self, cantidadDispositivos:int):
        pass
    
    #Consultas
    def obtenerCodigo(self)->int:
        return self.__codigo
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerCantidadDispositivos(self)->int:
        return self.__cantidadDispositivos    