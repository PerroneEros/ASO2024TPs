from classPolizaInmueble import PolizaInmueble

class Aseguradora():
    def __init__(self):
        self.__seguros = []

    # Comandos

    def insertar(self, poliza: 'PolizaInmueble'):
        if not isinstance(poliza, PolizaInmueble):
            raise ValueError("La poliza debe ser de tipo PolizaInmueble")
        
        # Insertar manteniendo la lista ordenada por número de póliza
        if poliza not in self.__seguros:
            self.__seguros.append(poliza)
            self.__seguros.sort(key=lambda x: x.obtenerNumero())
        else:
            print(f"La póliza {poliza.obtenerNumero()} ya está asignada a esta aseguradora.")

    def eliminar(self, poliza: 'PolizaInmueble'):
        if not isinstance(poliza, PolizaInmueble):
            raise ValueError("La póliza debe ser de tipo PolizaInmueble")
        
        if poliza in self.__seguros:
            self.__seguros.remove(poliza)
            print(f"La póliza {poliza.obtenerNumero()} fue eliminada.")
        else:
            print("La póliza no existe en la aseguradora.")

    # Consultas

    def existePoliza(self, poliza: 'PolizaInmueble') -> bool:
        return poliza in self.__seguros

    def hayPolizas(self) -> bool:
        return len(self.__seguros) > 0

    def costoTotal(self) -> float:
        return sum(poliza.obtenerCosto() for poliza in self.__seguros)

    def esIgual(self, aseguradora: 'Aseguradora') -> bool:
        if not isinstance(aseguradora, Aseguradora):
            raise ValueError("Debe ser una instancia de Aseguradora")
        
        # Verificar si ambas listas de seguros tienen las mismas referencias
        return set(self.__seguros) == set(aseguradora.__seguros)



