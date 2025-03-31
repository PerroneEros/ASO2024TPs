from classVehiculo import Vehiculo

class Auto(Vehiculo):
    
    def __init__(self, marca:str, modelo:str, patente:str, color:str, anioFabricacion:int, precio:float, kilometraje:int, combustible:str, cantPuertas:int, aireAcondicionado:bool):
        super().__init__(marca, modelo, patente, color, anioFabricacion, precio, kilometraje, combustible)
        self.__cantPuertas=cantPuertas
        self.__aireAcondicionado=aireAcondicionado

    #Comandos
    def establecerCantPuertas(self, cantPuertas:int):
        if not isinstance(cantPuertas, int) or cantPuertas<=0:
            raise ValueError("El auto debe tener una cantidad de puertas mayores a 0")
        else:
            self.__cantPuertas=cantPuertas
            
    def establecerAireAcondicionado(self, aire:bool):
        if not isinstance(aire, bool):
            raise ValueError("Si tiene o no tiene debe ser True or False")
        else:
            self.__aireAcondicionado=aire        
            
    #Consultas
    
    def obtenerCantidadPuertas(self)->int:
        return self.__cantPuertas
    
    def obtenerAireAcondicionado(self)->bool:
        return self.__aireAcondicionado
    
    #Comandos Heredados
    def establecerMarca(self, marca):
        return super().establecerMarca(marca)
    
    def establecerModelo(self, modelo):
        return super().establecerModelo(modelo)
    
    def establecerPatente(self, patente):
        return super().establecerPatente(patente)
    
    def establecerColor(self, color):
        return super().establecerColor(color)
    
    def establecerAnioFabricacion(self, anio):
        return super().establecerAnioFabricacion(anio)
    
    def establecerPrecio(self, precio):
        return super().establecerPrecio(precio)
    
    def establecerKilometraje(self, kilometraje):
        return super().establecerKilometraje(kilometraje)
    
    def establecerCombustible(self, combustible):
        return super().establecerCombustible(combustible)
    
    #Consultas Heredadas
    def obtenerMarca(self):
        return super().obtenerMarca()
    
    def obtenerModelo(self):
        return super().obtenerModelo()
    
    def obtenerPatente(self):
        return super().obtenerPatente()
    
    def obtenerColor(self):
        return super().obtenerColor()
        
    def obtenerAnioFabricacion(self):
        return super().obtenerAnioFabricacion()
    
    def obtenerPrecio(self):
        return super().obtenerPrecio()
    
    def obtenerCombustible(self):
        return super().obtenerCombustible()
    
    def obtenerKilometraje(self):
        return super().obtenerKilometraje()    