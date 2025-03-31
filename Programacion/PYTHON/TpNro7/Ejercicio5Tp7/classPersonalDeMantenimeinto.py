from classPersona import Persona

class PersonalDeMantenimiento(Persona):
    
    def __init__(self, nombre:str, apellido:str, dni:str, nroLegajo:int, area:str):
        super().__init__(nombre, apellido, dni, nroLegajo)
        self.__area=area
    
    def establecerArea(self, area:str):
        if not isinstance(area, str):
            raise ValueError("El area debe ser una string")
        else:
            self.__area=area
        
    def establecerNombre(self, nombre):
        return super().establecerNombre(nombre)
    
    def establecerDni(self, dni):
        return super().establecerDni(dni)
    
    def establecerApellido(self, apellido):
        return super().establecerApellido(apellido)
    
    def establecerNroLegajo(self, nroLegajo):
        return super().establecerNroLegajo(nroLegajo)
    
    def obtenerArea(self)->str:
        return self.__area
    
    def obtenerApellido(self):
        return super().obtenerApellido()
    
    def obtenerDni(self):
        return super().obtenerDni()
    
    def obtenerNombre(self):
        return super().obtenerNombre()
    
    def obtenerNroLegajo(self):
        return super().obtenerNroLegajo()
    
    