class Propietario():

    #Cosntructor
    def __init__(self, nombre:str):
        self.__nombre=nombre

    #Comandos
    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un string")
        else:
            self.__nombre=nombre

    def obtenerNombre(self)->str:
        return self.__nombre                