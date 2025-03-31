from classPersona import Persona

class Administrativo(Persona):
    
    def __init__(self, nombre:str, apellido:str, dni:str, nroLegajo:int, posicion:str):
        super().__init__(nombre, apellido, dni, nroLegajo)
        self.__posicion=posicion
        
    def establecerNombre(self, nombre):
        return super().establecerNombre(nombre)
    
    def establecerDni(self, dni):
        return super().establecerDni(dni)
    
    def establecerApellido(self, apellido):
        return super().establecerApellido(apellido)
    
    def establecerNroLegajo(self, nroLegajo):
        return super().establecerNroLegajo(nroLegajo)
    
    def obtenerApellido(self):
        return super().obtenerApellido()
    
    def obtenerDni(self):
        return super().obtenerDni()
    
    def obtenerNombre(self):
        return super().obtenerNombre()
    
    def obtenerNroLegajo(self):
        return super().obtenerNroLegajo()
    
    def establecerPosicion(self, posicion:str):
        if isinstance(posicion, str):
            raise ValueError("La posicion debe ser un string")
        else:
            self.__posicion=posicion
            
    def obtenerPosicion(self)->str:
        return self.__posicion            