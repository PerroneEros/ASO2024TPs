"""
 1. Paquete grupal: Cada paquete de viaje grupal tiene una ciudad, fechas de ida y vuelta, una
    descripción del viaje, un tipo de viaje (entre las opciones: turismo, educativo o aventura), y
    un precio. También se debe mantener información sobre el cupo máximo y el cupo actual de
    personas en cada paquete grupal. Cada paquete tiene un número que lo identifica.
"""

from enum import Enum

class Transporte(Enum):
    AVION = 1
    COLECTIVO = 2
    TREN = 3
    CRUCERO = 4

    def toDiccionario(self):
        return self.value

    @classmethod
    def fromDiccionario(cls, data):
        return cls(data)
    
class TipoViaje(Enum):
    TURISMO = 1
    AVENTURA = 2
    EDUCATIVO = 3
    EGRESADOS = 4
    
    def toDiccionario(self):
        return self.value

    @classmethod
    def fromDiccionario(cls, data):
        return cls(data)
        
    
from Hotel import Hotel
from Hotel import Pension
from Ciudad import Ciudad

class ParqueGrupal:
    
    @classmethod
    def fromDiccionario(cls, data):
        return cls(
            nroDeParque=data['nroDeParque'],
            cupoMax=data['cupoMax'],
            cupoAct=data['cupoAct'],
            ciudad=Ciudad.fromDiccionario(data['ciudad']),
            hotel=Hotel.fromDiccionario(data['hotel']),
            fechaDeIda=data['fechaDeIda'],
            fechaDeVuela=data['fechaDeVuelta'],
            tipoDeViaje=TipoViaje.fromDiccionario(data['tipoDeViaje']),
            transporte=Transporte.fromDiccionario(data['transporte'])
        )
    
    def __init__(self, nroDeParque:int, cupoMax:int, cupoAct:int, ciudad:'Ciudad', hotel:'Hotel', fechaDeIda:str, fechaDeVuela:str, tipoDeViaje:'TipoViaje', transporte:'Transporte'):
        if not isinstance(nroDeParque, int) or nroDeParque<0:
            raise TypeError("El nro de parque debe ser un entero positivo")
        if not isinstance(cupoMax, int) or cupoMax<0:
            raise TypeError("El cupo maximo debe ser un entero positivo")
        if not isinstance(cupoAct, int) or cupoAct > cupoMax:
            raise TypeError("El cupo actual debe ser un entero menor al cupo maximo")
        if not isinstance(ciudad, Ciudad):
            raise TypeError("La ciudad debe ser de tipo ciudad") 
        if not isinstance(hotel, Hotel):
            raise TypeError("El hotel debe ser de tipo hotel")    
        if not isinstance(fechaDeIda, str) or fechaDeIda=="" or fechaDeIda.isspace():
            raise TypeError("La fecha debe ser especificada como str")
        if not isinstance(fechaDeVuela, str) or fechaDeVuela=="" or fechaDeVuela.isspace():
            raise TypeError("La fecha debe ser especificada como str")
        if not isinstance(tipoDeViaje, TipoViaje):
            raise TypeError("El tipo de vieje debe ser TipoViaje")
        if not isinstance(transporte, Transporte):
            raise TypeError("El transporte debe ser de tipo transporte")    
        self.__nroDeParque=nroDeParque
        self.__cupoMax=cupoMax
        self.__cupoAct=cupoAct
        self.__ciudad=ciudad
        self.__hotel=hotel
        self.__fechaDeIda=fechaDeIda
        self.__fechaDeVuelta=fechaDeVuela
        self.__tipoDeViaje=tipoDeViaje
        self.__transporte=transporte
        
    def toDiccionario(self):
        return {
            'nroDeParque': self.__nroDeParque,
            'cupoMax': self.__cupoMax,
            'cupoAct': self.__cupoAct,
            'ciudad': self.__ciudad.toDiccionario(),
            'hotel': self.__hotel.toDiccionario(),
            'fechaDeIda': self.__fechaDeIda,
            'fechaDeVuelta': self.__fechaDeVuelta,
            'tipoDeViaje': self.__tipoDeViaje.toDiccionario(),
            'transporte': self.__transporte.toDiccionario()
        }
    
    def capacidadDisponible(self)->int:
        return self.__cupoMax-self.__cupoAct
    
    def inscribirPasajeros(self, cantidad:int):
        if (self.__cupoMax-self.__cupoAct) > 0:
            print("Se ha inscripto un pasajero")
            self.__cupoAct += 1
        else:
            print("No hay mas lugar")            
                               
import json
import os

class TesterSerializacion:
    @staticmethod
    def crearYGuardarPaquetes():
        
        ciudad1 = Ciudad("Puan", "BsAs", "La Laguna")
        hotel1 = Hotel("Mito", ciudad1, "Es lindo", "Medio pelo 2 estrellas", Pension.DESAYUNO)
        
        paquete1 = ParqueGrupal(1, 50, 20, ciudad1, hotel1, "2024-12-01", "2024-12-10", TipoViaje.TURISMO, Transporte.AVION)
        paquete2 = ParqueGrupal(2, 40, 10, ciudad1, hotel1, "2024-12-05", "2024-12-15", TipoViaje.AVENTURA, Transporte.TREN)
        
        # Serializar los paquetes a diccionarios
        paquetes = [paquete1.toDiccionario(), paquete2.toDiccionario()]
        
        # Guardar en archivo JSON
        with open("paquetes.json", "w") as archivo:
            json.dump(paquetes, archivo)
        print("Paquetes guardados en paquetes.json")


class TesterDeserializacion:
    @staticmethod
    def cargarPaquetes():
        if os.path.exists("paquetes.json"):
            with open("paquetes.json", "r") as archivo:
                paquetes_data = json.load(archivo)
            
            paquetes = []
            for data in paquetes_data:
                # Usar el método fromDiccionario para recrear el objeto
                paquete = ParqueGrupal.fromDiccionario(data)
                paquetes.append(paquete)
                
            print("Paquetes cargados desde paquetes.json")
            return paquetes
        else:
            print("No existe el archivo paquetes.json")
            return []

# Ejemplo de uso
TesterSerializacion.crearYGuardarPaquetes()
paquetes_cargados = TesterDeserializacion.cargarPaquetes()
        