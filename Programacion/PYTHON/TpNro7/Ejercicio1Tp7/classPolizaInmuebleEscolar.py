from classPolizaInmueble import PolizaInmueble

class PolizaInmuebleEscolar(PolizaInmueble):

    def __init__(self, numero: int, incendio: float, explosion: float, robo: float, 
                 cantPersonas: int, montoEquipamiento: float, montoMobiliario: float, montoPersona: float):
        super().__init__(numero, incendio, explosion, robo)
        self.__cantPersonas = cantPersonas
        self.__montoEquipamiento = montoEquipamiento
        self.__montoMobiliario = montoMobiliario
        self.__montoPersona = montoPersona

    def obtenerCantPersonas(self) -> int:
        return self.__cantPersonas

    def obtenerMontoEquipamiento(self) -> float:
        return self.__montoEquipamiento

    def obtenerMontoMobiliario(self) -> float:
        return self.__montoMobiliario

    def obtenerMontoPersona(self) -> float:
        return self.__montoPersona

    def costoPoliza(self) -> float:
        return super().costoPoliza() + self.__montoEquipamiento + self.__montoMobiliario + self.__montoPersona

    def toString(self) -> str:
        return (super().toString() + 
                f", Cantidad de personas: {self.__cantPersonas}, "
                f"Monto equipamiento: {self.__montoEquipamiento}, "
                f"Monto mobiliario: {self.__montoMobiliario}, "
                f"Monto persona: {self.__montoPersona}")

    def establecerCantPersonas(self, cantPersonas: int):
        if not isinstance(cantPersonas, int) or cantPersonas < 0:
            raise ValueError("La cantidad de personas debe ser un entero positivo")
        self.__cantPersonas = cantPersonas

    def establecerMontoEquipamiento(self, montoEquipamiento: float):
        if not isinstance(montoEquipamiento, float) or montoEquipamiento < 0:
            raise ValueError("El monto equipamiento debe ser un real positivo")
        self.__montoEquipamiento = montoEquipamiento    

    def establecerMontoMoviliario(self, montoMobiliario: float):
        if not isinstance(montoMobiliario, float) or montoMobiliario < 0:
            raise ValueError("El monto mobiliario debe ser un real positivo")                             
        self.__montoMobiliario = montoMobiliario

    def establecerMontoPersona(self, montoPersona: float):
        if not isinstance(montoPersona, float) or montoPersona < 0:
            raise ValueError("El monto persona debe ser un real positivo")
        self.__montoPersona = montoPersona
                
