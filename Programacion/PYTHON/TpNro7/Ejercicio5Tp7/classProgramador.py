from classPersona import Persona
from classProyecto import Proyecto

class Programador(Persona):
    
    def __init__(self, nombre:str, apellido:str, dni:str, nroLegajo:int, proyecto:'Proyecto'):
        super().__init__(nombre, apellido, dni, nroLegajo)
        self.__proyecto=proyecto
    
    def establecerProyecto(self, proyecto:'Proyecto'):
        if not isinstance(proyecto, Proyecto):
            raise ValueError("El proyecto debe ser de tipo Proyecto")
        else:
            self.__proyecto=proyecto
            
    def obtenerProyecto(self):
        return self.__proyecto.obtenerNombre()        
        
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
    
    