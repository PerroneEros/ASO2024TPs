"""
    Guía de Aventura: Cada guía tiene un nombre y un turno de trabajo (“mañana”,
    “tarde” o “noche”). Los guías deben autorizar al visitante cada vez que desee utilizar
    una atracción en base a su estatura.
"""

from classVisitante import Visitante
from classAtraccion import Atraccion

class Guia():

    def __init__ (self, nombre:str, turno:str):
        self.__nombre=nombre
        self.__turno=turno

    def obtenerNombre(self)->str:
        return self.__nombre

    def obtenerTurno(self)->str:
        return self.__turno

    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str):
            raise ValueError("Nombre debe ser de tipo string")
        else:
            self.__nombre=nombre

    def establecerTurno(self, turno:str):
        if not isinstance(turno, str):
            raise ValueError("Turno debe ser de tipo string")
        else:
            self.__turno=turno

    def habilitarVisitante(self, visitante:'Visitante', atraccion:'Atraccion'):
        if not isinstance(visitante, Visitante) or not isinstance(atraccion, Atraccion):
            raise ValueError("Funcion con parametros mal pactados")
        else:
            if (visitante.obtenerAltura() >= atraccion.obtenerEstMinRequerida()):
                visitante.anotarAtracVisit(atraccion)
            else:
                print("El visitante no cumplio con las caracteristicas necesarias") 