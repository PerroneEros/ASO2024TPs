from classInmueble import Inmueble
from classPropietario import Propietario

class Departamento(Inmueble):

    #Constructor
    def __init__(self, codigo:int, domicilio:str, propietario:'Propietario', metrosCuadrados:int, estado:int, gastosComunes:float, cochera:bool):
        super().__init__(codigo, domicilio, propietario, metrosCuadrados, estado)
        self.__gastosComunes = gastosComunes
        self.__cochera = cochera

    #Comandos
    def establecerGastosComunes(self, gastoComun:float):
        pass

    def establecerCochera(self, cochera:bool):
        pass

    #Consultas
    def obtenerGastosComunes(self):
        return self.__gastosComunes

    def obtenerCochera(self):
        return self.__cochera

    """
        El costo del alquiler de cualquier inmueble se calcula a partir del valor base
        recibido como parámetro más $100 por metro cuadrado de superficie del
        inmueble. El de los departamentos es el costo de cualquier inmueble más $2000 si tiene cochera.
    """    

    def costoAlquiler(self, base:int)->float:
        if not isinstance(base, int) or base<0:
            raise ValueError("El costo base debe ser un entero positivo")
        else:
            Costo=base+(self.VALOR_METRO_CUADRADO*self._metrosCuadrados)   
            if self.__cochera:
                Costo+=self.VALOR_COCHERA_MES
            return Costo

    """
        b. El precio de venta de cualquier inmueble se calcula como cantidad de metros
        cuadrados por el valor del metro cuadrado, el cual es recibido por parámetro. 
        El precio de venta de los departamentos, suma al costo del inmueble el equivalente a 3 metros
        cuadrados en caso de tener cochera.       
    """

    def precioVenta(self, ValorDelMetroCuadrado:float)->float:
        if not isinstance(ValorDelMetroCuadrado, float) or ValorDelMetroCuadrado<0:
            raise ValueError("Los metros cuadrados debe ser reales positivos")
        else:
            if self.__cochera:
                CostoPorCochera=3 * ValorDelMetroCuadrado
            else:
                CostoPorCochera=0    
            return ValorDelMetroCuadrado * self._metrosCuadrados + CostoPorCochera          