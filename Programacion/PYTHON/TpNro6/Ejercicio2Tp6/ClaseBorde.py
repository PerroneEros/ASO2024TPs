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

class borde():
    
    #Constructor
    
    def __init__(self,grosor:int, color:'color'):
        self.__grosor=grosor
        self.__color=color
        
    #Comandos
    
    def copiarValores(self, Borde:'borde')->'borde':
        self.__grosor=Borde.obtenerGrosor()
        self.__color=Borde.obtenerColor()
        
    #Consultas
    
    def obtenerGrosor(self)->int:
        return self.__grosor
    
    def obtenerColor(self)->'color':
        return self.__color
    
    def clonar(self)->'borde':
        rBorde=(self.__grosor, self.__color)
        
        return rBorde
    
    def esIgualQue(self,Borde:'borde')->bool:
        if (self.__grosor==Borde.obtenerGrosor() and self.__color==Borde.obtenerColor()):
            esIgual=True
        else:
            esIgual=False       
        return esIgual     
        