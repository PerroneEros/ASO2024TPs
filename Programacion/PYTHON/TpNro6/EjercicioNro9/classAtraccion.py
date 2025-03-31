"""
    Atracción: Cada atracción tiene un nombre, un tipo (por ejemplo, montaña rusa, casa
    embrujada), un nivel de emoción (bajo, medio, alto) y una estatura mínima requerida
    (por ejemplo: 1,40). Las atracciones pueden funcionar en uno o más turnos
    (“mañana”, “tarde” o “noche”)
"""

class Atraccion():

    def __init__ (self, nombre:str, tipo:str, nivelEmocion:str, estMinRequerida:float, turno:str):
        self.__nombre=nombre
        self.__tipo=tipo
        self.__nivelEmocion=nivelEmocion
        self.__estMinRequerida=estMinRequerida
        self.__turno=turno

    def obtenerNombre(self)->str:
        return self.__nombre

    def obtenerTipo(self)->str:
        return self.__tipo

    def obtenerNivelEmocion(self)->str:
        return self.__nivelEmocion

    def obtenerEstMinRequerida(self)->float:
        return self.__estMinRequerida

    def obtenerTurno(self)->str:
        return self.__turno

    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str):
            raise ValueError("El nombre que pasaste no es un str")
        else:    
            self.__nombre=nombre

    def establecerTipo(self, tipo:str):
        if not isinstance(tipo, str):
            raise ValueError("El tipo tiene que ser un string")        
        else:
            self.__tipo=tipo

    def establecerNivelEmocion(self, emocion:str):
        if not isinstance(emocion, str):
            raise ValueError("La emocion debe ser una string")
        else:
            self.__nivelEmocion=nivelEmocion

    def establecerEstMinRequerida(self, estMinRequerida:float):
        if not isinstance(estMinRequerida, float):
            raise ValueError("La altura minima requerida debe ser un float")
        else:
            self.__estMinRequerida=estMinRequerida

    def establecerTurno(self, turno:str):
        if not isinstance(turno, str):
            raise ValueError("El turno debe ser un string")
        else:
            self.__turno=turno
        



