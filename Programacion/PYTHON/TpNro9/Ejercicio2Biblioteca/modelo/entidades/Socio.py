"""
2) La biblioteca desea ahora implementar una API REST que permita gestionar la
información de los socios. Para registrarse en la biblioteca se le pide a cada socio la
siguiente información: número de DNI, nombre, apellido, un mail de contacto y su
fecha de nacimiento.
Cada vez que se registra un usuario el sistema debe controlar que no exista otro
socio registrado con el mismo DNI.
"""

class Socio:

    @classmethod
    def fromDiccionario(cls, data: dict) -> "Socio":
        if not isinstance(data, dict):
            raise ValueError("El parámetro data debe ser un diccionario.")
        return cls(data["DNI"], data["nombre"], data["apellido"], data["mail"], data["fechaDeNacimiento"])
    
    #metodos de instancia
    def __init__(self, DNI:int, nombre:str, apellido:str, mail:str, fechaDeNacimiento:str):
        if not isinstance(DNI, int) or DNI<0:
            raise ValueError("El DNI debe ser un entero")
        if not isinstance(nombre, str) or nombre=="" or nombre.isspace():
            raise ValueError("El nombre debe ser un string")
        if not isinstance(apellido, str) or apellido=="" or apellido.isspace():
            raise ValueError("El apellido debe ser un string")
        if not isinstance(mail, str) or mail=="" or mail.isspace():
            raise ValueError("El mail debe ser un string")
        if not isinstance(fechaDeNacimiento, str) or fechaDeNacimiento=="" or fechaDeNacimiento.isspace():
            raise ValueError("La fecha de nacimiento debe ser un str")
        self.__DNI = DNI
        self.__nombre = nombre
        self.__apellido = apellido
        self.__mail=mail
        self.__fechaDeNacimiento=fechaDeNacimiento

    #consultas
    def obtenerDNI(self)->int:
        return self.__DNI
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerApellido(self)->str:
        return self.__apellido
    
    def obtenerMail(self)->str:
        return self.__mail
    
    def obtenerFechaDeNacimiento(self)->str:
        return self.__fechaDeNacimiento
    
    def toDiccionario(self)->dict:
        return {
            "DNI": self.__DNI,
           "nombre": self.__nombre,
           "apellido": self.__apellido,
           "mail": self.__mail,
           "fechaDeNacimiento": self.__fechaDeNacimiento
           }

    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str) or nombre=="" or nombre.isspace():
            raise TypeError(" El nombre debe ser un string valido ")
        self.__nombre = nombre
        
    def establecerApellido(self, apellido:str):    
        if not isinstance(apellido, str) or apellido=="" or apellido.isspace():
            raise TypeError(" El apellido debe ser un string valido ")
        self.__apellido = apellido
        
    def establecerMail(self, mail:str):
        if not isinstance(mail, str) or mail=="" or mail.isspace():
            raise TypeError("El mail debe ser un string valido")
        self.__mail = mail
        
    def establecerFechaDeNacimiento(self, fechaDeNacimiento:str):
        if not isinstance(fechaDeNacimiento, str) or fechaDeNacimiento=="" or fechaDeNacimiento.isspace():
            raise TypeError("la fecha de nacimiento tiene que ser un string")
        self.__fechaDeNacimiento = fechaDeNacimiento        
    
    def toString(self)->str:
        return f"DNI:{self.__DNI}, nombre:{self.__nombre}, apellido:{self.__apellido}, mail:{self.__mail}, fechaDeNacimiento:{self.__fechaDeNacimiento}"