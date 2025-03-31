"""
    2) Dada la clase Color implementada en el práctico 5, implemente la clase Borde de
    acuerdo al siguiente diagrama. El borde tiene un grosor y es de un determinado
    color. Cuando se crea un borde recibe un valor para el grosor y un color. Tiene los
    comandos y consultas triviales, y agrega:
    ○ un comando copiarValores que le permita copiar los valores de otro borde
    ○ una consulta clonar que retorna un clon del borde
    ○ una consulta esIgualQue que devuelve True si el borde recibido es igual a la
    instancia que recibe el mensaje
"""

from ClaseColor import color

class borde:

    # Constructor
    def __init__(self, grosor: int, color: 'color'):
        self.__grosor = grosor
        self.__color = color

    #Cosultas y metodos
    def clonar_a(self) -> 'borde':
        return borde(self.__grosor, self.__color.clonar())

    def esIgualQue_a(self, otro_borde: 'borde') -> bool:
        return self.__grosor == otro_borde.obtenerGrosor() and self.__color is otro_borde.obtenerColor()

    def clonar_b(self) -> 'borde':
        return borde(self.__grosor, self.__color)

    def esIgualQue_b(self, otro_borde: 'borde') -> bool:
        return self.__grosor == otro_borde.obtenerGrosor() and self.__color.esIgualQue(otro_borde.obtenerColor())

    def clonar_c(self) -> 'borde':
        return borde(self.__grosor, self.__color.clonar())

    def esIgualQue_c(self, otro_borde: 'borde') -> bool:
        return self.__grosor == otro_borde.obtenerGrosor() and self.__color.esIgualQue(otro_borde.obtenerColor())

    def obtenerGrosor(self) -> int:
        return self.__grosor

    def obtenerColor(self) -> 'color':
        return self.__color
 
        