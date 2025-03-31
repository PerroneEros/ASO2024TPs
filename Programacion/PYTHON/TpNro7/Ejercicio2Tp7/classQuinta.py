from classInmueble import Inmueble

class Quinta(Inmueble):

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

    def costoAlquiler(self, base:int)->float:
        if not isinstance(base, int) or base<0:
            raise ValueError("El costo base debe ser un entero positivo")
        else:
            Inflacion=0.05
            Costo=base+Inflacion*base+self.__metrosParque*1000  
            return Costo

    def precioVenta(self, ValorDelMetroCuadrado:float)->float:
        if not isinstance(ValorDelMetroCuadrado, float) or ValorDelMetroCuadrado<0:
            raise ValueError("Los metros cuadrados debe ser reales positivos")
        else:
            return ValorDelMetroCuadrado * self._metrosCuadrados + self.__metrosParque*1000            