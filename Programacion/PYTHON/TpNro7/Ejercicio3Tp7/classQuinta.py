from classInmueble import Inmueble
from classPropietario import Propietario

class Quinta(Inmueble):

    VALOR_METRO_CUADRADO=100
    VALOR_EXTRA_QUINTA=500

    #Constructor
    def __init__ (self, codigo:int, domicilio:str, propietario:'Propietario', metrosCuadrados:int, estado:int, metrosParque:int):
        super().__init__(codigo, domicilio, propietario, metrosCuadrados, estado)
        self.__metrosParque=metrosParque

    #Comandos
    def establecerMetrosParque(self, metros:int):
        pass

    #Consultas
    def obtenerMetrosParque(self)->int:
        pass

    """    
        El costo del alquiler de cualquier inmueble se calcula a partir del valor base
        recibido como parámetro más $100 por metro cuadrado de superficie del
        inmueble. El costo del alquiler de una quinta es el de cualquier inmueble más
        $500 por cada 15 metros cuadrados de parque
    """

    def costoAlquiler(self, base:int)->float:
        if not isinstance(base, int) or base<0:
            raise ValueError("El costo base debe ser un entero positivo")
        else:
            Costo=base+(self._metrosCuadrados*self.VALOR_METRO_CUADRADO)+(self.__metrosParque*self.VALOR_EXTRA_QUINTA)  
            return Costo
    
    """
        b. El precio de venta de cualquier inmueble se calcula como cantidad de metros
        cuadrados por el valor del metro cuadrado, el cual es recibido por parámetro.
        En el caso de las quintas cada metro cuadrado de parque es igual a la mitad
        del valor del metro cuadrado construido.
    """

    def precioVenta(self, ValorDelMetroCuadrado:float)->float:
        if not isinstance(ValorDelMetroCuadrado, float) or ValorDelMetroCuadrado<0:
            raise ValueError("Los metros cuadrados debe ser reales positivos")
        else:
            return (ValorDelMetroCuadrado * self._metrosCuadrados) + (self.__metrosParque*0.5*ValorDelMetroCuadrado)           