from classInmueble import Inmueble

class Inmoviliaria():

    #Constructor
    def __init__(self, propiedades:'Inmueble'):
        self.__propiedades=None

    #Comandos
    def insertar(self, propiedades: 'Inmueble'):
        if not isinstance(propiedades, Inmueble):
            raise ValueError("La propiedad debe ser de tipo Inmueble")
        else:
            if self.__propiedades==None:
                self.__propiedades=[]
                self.__propiedades.append(propiedades)    
            else:
                # Insertar manteniendo la lista ordenada por número de póliza
                if propiedades not in self.__propiedades:
                    self.__propiedades.append(propiedades)
                else:
                    print(f"La póliza {propiedades.obtenerCodigo()} ya está asignada a esta aseguradora.")

    def eliminar(self, propiedad: 'Inmueble'):
        if not isinstance(propiedad, Inmueble):
            raise ValueError("La póliza debe ser de tipo PolizaInmueble")
        
        if propiedad in self.__propiedades:
            self.__propiedades.remove(propiedad)
            print(f"La póliza {propiedad.obtenerCodigo()} fue eliminada.")
        else:
            print("La póliza no existe en la aseguradora.")

    def estaInmueble(self, codigo: int) -> bool:
        for propiedad in self.__propiedades:
            if propiedad.obtenerCodigo() == codigo:
                return True
        return False

    def estaInmueble(self, propiedad: 'Inmueble') -> bool:
        return propiedad in self.__propiedades

    def hayInmuebles(self) -> bool:
        return len(self.__propiedades) > 0

    def contarPropiedadesMasMetros(self, metros: int) -> int:
        contador = 0
        for propiedad in self.__propiedades:
            if propiedad.obtenerMetrosCuadrados() < metros:
                contador += 1
        return contador

    def mayorPrecioVenta(self) -> 'Inmueble':
        if not self.__propiedades:
            return None
        else:
            Maximo=0
            for propiedad in self.__propiedades:    
                if propiedad.precioVenta(10.0) > Maximo:
                    Maximo=propiedad.precioVenta(10.0)
                    propiedad_maxPrecio = propiedad

            return propiedad_maxPrecio        
    
        
    
        


       