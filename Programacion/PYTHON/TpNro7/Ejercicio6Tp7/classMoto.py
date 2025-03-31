from classVehiculo import Vehiculo

class Auto(Vehiculo):
    
    def __init__(self, marca:str, modelo:str, patente:str, color:str, anioFabricacion:int, precio:float, kilometraje:int, combustible:str, anchoManubrio:float, cilindrado:str):
        super().__init__(marca, modelo, patente, color, anioFabricacion, precio, kilometraje, combustible)
        self.__anchoManubrio=anchoManubrio
        self.__cilindrado=cilindrado

    #Comandos
    def establecerAnchoManubrio(self, ancho:float):
        if not isinstance(ancho, float) or ancho<=0:
            raise ValueError("El ancho del manubrio debe ser un real positivo")
        else:
            self.__anchoManubrio=ancho
            
    def establecerAireAcondicionado(self, cilindrado:str):
        if not isinstance(cilindrado, str):
            raise ValueError("Cilindrado debe ser un string")
        else:
            self.__cilindrado=cilindrado       
            
    #Consultas
    
    def obtenerCantidadPuertas(self)->float:
        return self.__anchoManubrio
    
    def obtenerAireAcondicionado(self)->str:
        return self.__cilindrado
    
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