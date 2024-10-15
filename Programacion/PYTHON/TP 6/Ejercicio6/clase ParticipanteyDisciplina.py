'''
Un club de deportes está organizando un torneo de atletismo, y nos pide que le 
ayudemos a gestionar la información de los participantes y las disciplinas. El sistema 
debe permitir registrar a los participantes y las disciplinas en las que compiten Cada Participante tiene un nombre, una edad y una nacionalidad. 
Un Participante puede competir en varias Disciplinas. 
Cada Disciplina tiene un nombre (como carreras de 100 metros, carreras de 400 
metros, salto de longitud, salto en alto, lanzamiento de jabalina, etc.) y una 
descripción (que explica las reglas o características de esa disciplina). 
Varios Participantes pueden competir en la misma Disciplina, y un Participante 
puede competir en varias disciplinas. 
Se pide: 
A. Diseñar el diagrama UML de las clases. 
B. Implementar las clases en python. 
C.  Desarrollar una clase tester que pida al usuario los datos para registrar las 
disciplinas, y los datos de los participantes. Luego debe permitir al usuario 
ver todos los participantes inscriptos en una disciplina y las disciplinas en las 
que participa cada competidor'''

class Participante():
    def __init__(self,nombre:str,edad:int,nacionalidad:str):
        self.__nombre = nombre
        self.__edad = edad
        self.__nacionalidad = nacionalidad
        self.__disciplinas = []
    #comandos
    def agregar_disciplina(self, disciplina):
        self.__disciplinas.append(disciplina)
    
    def desanotar_participante(self,participante):
        if participante in self.__disciplinas:
            self.__disciplinas.remove(participante)

    def establecerNombre(self,nombre:str):
        if not isinstance(nombre,str):
            raise ValueError("el nombre tiene que ser un cadena de texto")
        self.__nombre = nombre

    def establecerEdad(self, edad:int):
        if not isinstance(edad, int) or edad < 0:
            raise ValueError("la edad tiene que ser un número entero positivo")
        self.__edad = edad

    def establecerNacionalidad(self, nacionalidad:str):
        if not isinstance(nacionalidad, str):
            raise ValueError("la nacionalidad tiene que ser un cadena de texto")
        self.__nacionalidad = nacionalidad
           
    #CONSULTAS
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerEdad(self)->str:
        return self.__edad
    
    def obtenerNacionalidad(self)->str:
        return self.__nacionalidad 

    def obtenerDisciplina(self)->str:
        return self.__disciplinas
    
    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}, Nacionalidad: {self.__nacionalidad}"

class Disciplina():
    def __init__(self,nombre:str,descripcion:str):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__participantes = []
    
    #comandos
    def establecerNombre(self,nombre:str):
        if not isinstance(nombre, str):
            raise ValueError("el nombre tiene que ser un cadena de texto")
        self.__nombre = nombre

    def establecerDescripcion(self, descripcion:str):
        if not isinstance(descripcion, str):
            raise ValueError("la descripcion tiene que ser un cadena de texto")
        self.__descripcion = descripcion

    def agregar_participante(self, participante):
        self.__participantes.append(participante)
        