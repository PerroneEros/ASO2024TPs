"""
    Visitante: Cada visitante tiene un nombre, una edad, una altura y una dirección de
    correo electrónico. Los visitantes pueden comprar entradas y disfrutar de las
    atracciones, y llevan un registro de las atracciones a las que pudieron ingresar.
"""    
from classAtraccion import Atraccion
from classEntrada import Entrada

class Visitante():

    def __init__(self, nombre:str, edad:int, altura:float, correo:str, entrada:'Entrada'):
        self.__nombre=nombre
        self.__edad=edad
        self.__altura=altura
        self.__correo=correo
        self.__entrada=entrada
        self.__atraccionesVisitadas=None

    def obtenerNombre(self)->str:
        return self.__nombre

    def obtenerEdad(self)->int:
        return self.__edad

    def obtenerAltura(self)->float:
        return self.__altura

    def obtenerCorreo(self)->str:
        return self.__correo

    def obtenerAtraccionesVisitadas(self) -> list:
        if not self.__atraccionesVisitadas:
            return []
        return [atraccion.obtenerNombre() for atraccion in self.__atraccionesVisitadas]

    def obtenerNroEntrada(self)->'Entrada':
        return self.__entrada

    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str):
            raise ValueError("Nombre debe ser string")
        else:
            self.__nombre=nombre

    def establerEdad(self, edad:int):
        if not isinstance(edad, int) or edad<0:
            raise ValueError("Edad debe ser un entero positivo")
        else:
            self.__edad=edad                

    def establecerAltura(self, altura:float):
        if not isinstance(altura, float) and altura<0:
            raise ValueError("La altura debe ser logica")
        else: 
            self.__altura=altura

    def establecerCorreo(self, correo:str):
        if not isinstance(correo, str):
            raise ValueError("El correo debe ser un string")
        else:
            self.__correo=correo

    def establecerEntrada(self, entrada: 'Entrada'):
        if not isinstance(entrada, Entrada):
            raise ValueError("La entrada debe ser de tipo Entrada")
        self.__entrada = entrada


    def anotarAtracVisit(self, atraccion:'Atraccion'):
        if not isinstance(atraccion, Atraccion):  # Atraccion ya está entre comillas simples
            raise ValueError("La atracción debe ser de tipo Atraccion")
        if self.__atraccionesVisitadas is None:
            self.__atraccionesVisitadas = []
        if atraccion not in self.__atraccionesVisitadas:
            self.__atraccionesVisitadas.append(atraccion)
        else:
            print(f"{atraccion.obtenerNombre()} ya está asignada a este visitante.")
