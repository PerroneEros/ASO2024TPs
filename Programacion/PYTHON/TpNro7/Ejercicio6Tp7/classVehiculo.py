"""
Cada vehículo tiene una marca, modelo, patente, color, año de fabricación, precio y un 
determinado kilometraje
"""

class Vehiculo():
    
    def __init__ (self, marca:str, modelo:str, patente:str, color:str, anioFabricacion:int, precio:float, kilometraje:int, combustible:str):
        self._marca=marca
        self._modelo=modelo
        self._patente=patente
        self._color=color
        self._anioFabricacion=anioFabricacion
        self._precio=precio
        self._kilometraje=kilometraje
        self._combustible=combustible
        
    #Comandos
    
    def establecerMarca(self, marca:str):
        if not isinstance(marca, str):
            raise ValueError("Marca tiene que ser un string")
        else:
            self._marca=marca
            
    def establecerModelo(self, modelo:str):
        if not isinstance(modelo, str):
            raise ValueError("Modelo tiene que ser un str")
        else:
            self._modelo=modelo                
    
    def establecerPatente(self, patente:str):
        if not isinstance(patente, str):
            raise ValueError("Patente tiene que ser un str")
        else:
            self._patente
            
    def establecerColor(self, color:str):
        if not isinstance(color, str):
            raise ValueError("Color tiene que ser un str")            
        else:
            self._color=color
            
    def establecerAnioFabricacion(self, anio:int):
        if not isinstance(anio, int):
            raise ValueError("Año de fabricacion debe ser un entero")
        else:
            self._anioFabricacion=anio            
        
    def establecerPrecio(self, precio:float):
        if not isinstance(precio, float) or precio < 0:
            raise ValueError("El precio debe ser un real positivo")
        else:
            self._precio=precio
            
    def establecerKilometraje(self, kilometraje:int):
        if not isinstance(kilometraje, int) or kilometraje < 0:        
            raise ValueError("El kilometraje es un entero positivo")
        else:
            self._kilometraje=kilometraje
            
    def establecerCombustible(self, combustible:str):        
        if not isinstance(combustible, str):
            raise ValueError("El combustible debe ser un string")
        else:
            self._combustible=combustible
            
    #Comandos
    def obtenerMarca(self)->str:
        return self._marca
    
    def obtenerModelo(self)->str:
        return self._patente
    
    def obtenerPatente(self)->str:
        return self._patente
    
    def obtenerColor(self)->str:                    
        return self._color
    
    def obtenerAnioFabricacion(self)->int:
        return self._anioFabricacion
    
    def obtenerPrecio(self)->float:
        return self._precio
    
    def obtenerKilometraje(self)->int:
        return self._kilometraje
    
    def obtenerCombustible(self)->str:
        return self._combustible