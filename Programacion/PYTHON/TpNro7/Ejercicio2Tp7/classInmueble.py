from classPropietario import Propietario

class Inmueble():

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

    def establecerMetrosCuadrados(self)->int:
        return self._metrosCuadrados

    def establecerEstado(self)->int:
        return self._estado

    def costoAlquiler(self, base:int)->float:
        if not isinstance(base, int) or base<0:
            raise ValueError("El costo base debe ser un entero positivo")
        else:
            Inflacion=0.05
            Costo=base+Inflacion*base
            return Costo

    def precioVenta(self, ValorDelMetroCuadrado:float)->float:
        if not isinstance(ValorDelMetroCuadrado, float) or ValorDelMetroCuadrado<0:
            raise ValueError("Los metros cuadrados debe ser reales positivos")
        else:
            return ValorDelMetroCuadrado * self._metrosCuadrados
            
                    



            
