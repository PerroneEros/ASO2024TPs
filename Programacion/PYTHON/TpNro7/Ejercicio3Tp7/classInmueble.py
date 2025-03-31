from classPropietario import Propietario

"""
    3. Reutilizando el código del punto anterior, adáptalo para implementar en Python el
    diagrama de clases que sigue incluyendo sólo los métodos triviales que se
    requieran, considerando lo siguiente:

    a. El costo del alquiler de cualquier inmueble se calcula a partir del valor base
    recibido como parámetro más $100 por metro cuadrado de superficie del
    inmueble. El costo del alquiler de una quinta es el de cualquier inmueble más
    $500 por cada 15 metros cuadrados de parque y el de los departamentos es
    el costo de cualquier inmueble más $2000 si tiene cochera.

    b. El precio de venta de cualquier inmueble se calcula como cantidad de metros
    cuadrados por el valor del metro cuadrado, el cual es recibido por parámetro.
    En el caso de las quintas cada metro cuadrado de parque es igual a la mitad
    del valor del metro cuadrado construido. El precio de venta de los
    departamentos, suma al costo del inmueble el equivalente a 3 metros
    cuadrados en caso de tener cochera.
"""

class Inmueble():

    VALOR_METRO_CUADRADO=100

    #<<Constructor>>
    def __init__ (self, codigo:int, domicilio:str, propietario:'Propietario', metrosCuadrados:int, estado:int):
        self._codigo=codigo
        self._domicilio=domicilio
        self._propietario=propietario
        self._metrosCuadrados=metrosCuadrados
        self._estado=estado

    #<<Comandos>>
    def establecerCodigo(self, codigo:int):
        pass

    def establecerDomicilio(self, domicilio:str):
        pass

    def establecerPropietario(self, propietario:'Propietario'):
        pass

    def establecerMetrosCuadrados(self, metrosCuadrados:int):
        pass

    def establecerEstado(self, estado:int):
        pass

    #<<Consultas>>
    def obtenerCodigo(self)->int:
        return self._codigo

    def obtenerDomicilio(self)->str:
        return self._domicilio

    def obtenerPropietario(self)->'Propietario':
        return self._propietario

    def obtenerMetrosCuadrados(self)->int:
        return self._metrosCuadrados

    def obtenerEstado(self)->int:
        return self._estado

    """
        El costo del alquiler de cualquier inmueble se calcula a partir del valor base
        recibido como parámetro más $100 por metro cuadrado de superficie del
        inmueble.
    """

    def costoAlquiler(self, base:int)->float:
        if not isinstance(base, int) or base<0:
            raise ValueError("El costo base debe ser un entero positivo")
        else:
            Costo=base+(self.VALOR_METRO_CUADRADO*self._metrosCuadrados)
            return Costo

    """    
        b. El precio de venta de cualquier inmueble se calcula como cantidad de metros
        cuadrados por el valor del metro cuadrado, el cual es recibido por parámetro.
    """        

    def precioVenta(self, ValorDelMetroCuadrado:float)->float:
        if not isinstance(ValorDelMetroCuadrado, float) or ValorDelMetroCuadrado<0:
            raise ValueError("Los metros cuadrados debe ser reales positivos")
        else:
            return ValorDelMetroCuadrado * self._metrosCuadrados
            