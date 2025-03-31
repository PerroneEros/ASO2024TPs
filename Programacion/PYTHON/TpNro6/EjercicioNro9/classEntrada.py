"""
Entrada: Cada entrada tiene un número de entrada, una fecha y un tipo (por
ejemplo, entrada general, pase VIP). Cada entrada está asociada a un visitante.
"""

from Fecha import Fecha

class Entrada():

    def __init__ (self, nroEntrada:int, fecha:Fecha, tipo:str):
        self.__nroEntrada=nroEntrada
        self.__fecha=fecha
        self.__tipo=tipo

    def obtenerNroEntrada(self)->int:
        return self.__nroEntrada

    def obtenerFecha(self)->'Fecha':
        return self.__fecha

    def obtenerTipo(self)->str:
        return self.__tipo

    def establecerNroEntrada(self, nroEntrada:int):
        if not isinstance(nroEntrada, int) or nroEntrada<0:
            raise ValueError("El numero de entrada debe ser un entero positivo")
        else:
            self.__nroEntrada=nroEntrada

    def establecerFecha(self, fecha:'Fecha'):
        if not isinstance(fecha, 'Fecha'):
            raise ValueError("El objeto pasado por parametro debe ser un objeto de tipo fecha")
        else:
            self.__fecha=fecha

    def establecerTipo(self, tipo:str):
        if not isinstance(tipo, str):
            raise ValueError("El tipo debe ser un string")
        else:
            self.__tipo=tipo                                          




