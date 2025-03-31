"""
2.      Ciudad: Cada paquete de viaje tiene una ciudad, la ciudad tiene un nombre, la provincia
    donde se ubica, y los puntos turísticos a donde se puede ir a pasear. Cada ciudad se puede
    identificar mediante el nombre y la provincia, ya que puede haber ciudades con el mismo
    nombre en distintas provincias.
"""

class Ciudad:
    #metodos de clase -------------------------------------------------------------------------------------------------
    @classmethod
    def fromDiccionario(cls, data: dict)->"Ciudad":
        if not isinstance(data, dict):
            raise ValueError("El parametro data debe ser un diccionario.")
        return cls(data["nombre"], data["provincia"], data["puntosTuristicos"])
    
    #Constructor..
    def __init__ (self, nombre:str, provincia:str, puntosTuristicos:str):
        if not isinstance(nombre, str) or nombre=="" or nombre.isspace():
            raise TypeError("El nombre debe ser un string")
        if not isinstance(provincia, str) or provincia=="" or provincia.isspace():
            raise TypeError("La provincia debe ser un string")
        if not isinstance(puntosTuristicos, str) or puntosTuristicos=="" or puntosTuristicos.isspace():
            raise TypeError("Los puntos turisticos deben ser un string")
        self.__nombre=nombre
        self.__provincia=provincia
        self.__puntosTuristicos=puntosTuristicos
        
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerProvincia(self)->str:
        return self.__provincia
    
    def obtenerPuntosTuristicos(self)->str:
        return self.__puntosTuristicos    
    
    def esIgualProf(self, otra:'Ciudad')->bool:
        return self.__nombre == otra.obtenerNombre() and self.__provincia == otra.obtenerProvincia()
        
    def toDiccionario(self):
        return {"nombre":self.__nombre,
                "provincia":self.__provincia,
                "puntosTuristicos":self.__puntosTuristicos
            }
        
        
    
          
        
        
           