from classInmueble import Inmueble

class Departamento(Inmueble):

    VALOR_COCHERA_MES=50000

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

    def costoAlquiler(self, base:int)->float:
        if not isinstance(base, int) or base<0:
            raise ValueError("El costo base debe ser un entero positivo")
        else:
            Inflacion=0.05
            Costo=base+Inflacion*base+self.__gastosComunes
            if self.__cochera:
                Costo+=self.VALOR_COCHERA_MES    
            return Costo

    def precioVenta(self, ValorDelMetroCuadrado:float)->float:
        if not isinstance(ValorDelMetroCuadrado, float) or ValorDelMetroCuadrado<0:
            raise ValueError("Los metros cuadrados debe ser reales positivos")
        else:
            if self.__cochera:
                CostoPorCochera=self.VALOR_COCHERA_MES * 12 
            else:
                CostoPorCochera=0    
            return ValorDelMetroCuadrado * self._metrosCuadrados + CostoPorCochera          