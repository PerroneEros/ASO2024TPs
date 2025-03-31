"""
Un club de deportes está organizando un torneo de atletismo, y nos pide que le
ayudemos a gestionar la información de los participantes y las disciplinas. El sistema
debe permitir registrar a los participantes y las disciplinas en las que compiten.

Cada Participante tiene un nombre, una edad y una nacionalidad.
Un Participante puede competir en varias Disciplinas.

"""

class Participantes:
    
    def __init__(self, nombre: str, edad: int, nacionalidad: str):
        self.__nombre = nombre
        self.__edad = edad
        self.__nacionalidad = nacionalidad
        self.__disciplinas = []  # Cambiado a plural para consistencia
    
    # Consultas
    
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerEdad(self) -> int:
        return self.__edad
    
    def obtenerNacionalidad(self) -> str:
        return self.__nacionalidad
    
    def obtenerDisciplinas(self):
        return [disciplina.obtenerNombre() for disciplina in self.__disciplinas]
    
    # Comandos
    def establecerNombre(self, nombre: str):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un string")
        self.__nombre = nombre
        
    def establecerEdad(self, edad: int):
        if not isinstance(edad, int):
            raise ValueError("La edad debe ser un número entero")
        self.__edad = edad    
        
    def establecerNacionalidad(self, nacionalidad: str):
        if not isinstance(nacionalidad, str):
            raise ValueError("La nacionalidad debe ser un string")
        self.__nacionalidad = nacionalidad
    
    # Inscribir en disciplina
    def inscribirEnDisciplina(self, disciplina: 'Disciplina'):
        # Importamos Disciplina dentro del método para evitar la importación circular

        # Verificamos si el participante ya está inscrito en la disciplina
        if disciplina not in self.__disciplinas:
            self.__disciplinas.append(disciplina)
            disciplina.agregarParticipante(self)
            print(f"{self.obtenerNombre()} ha sido inscrito en la disciplina {disciplina.obtenerNombre()}.")
        else:
            print(f"{self.obtenerNombre()} ya está inscrito en la disciplina {disciplina.obtenerNombre()}.")
        

class Disciplina:
    
    # Constructor
    def __init__(self, nombre: str, descripcion: str):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__competidores = []
        
    # Consultas
    def obtenerNombre(self) -> str:
        return self.__nombre
    
    def obtenerDescripcion(self) -> str:
        return self.__descripcion
    
    def obtenerParticipantes(self):
        return [participante.obtenerNombre() for participante in self.__competidores]
    
    # Comandos
    def establecerNombre(self, nombre: str):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un string")
        self.__nombre = nombre
            
    def establecerDescripcion(self, descripcion: str):
        if not isinstance(descripcion, str):
            raise ValueError("La descripción debe ser un string")
        self.__descripcion = descripcion
            
    # Agregar participante
    def agregarParticipante(self, participante: 'Participantes'):
        # Importamos Participantes dentro del método para evitar la importación circular

        # Verificamos si el participante ya está inscrito
        if participante not in self.__competidores:
            self.__competidores.append(participante)
            print(f"Participante {participante.obtenerNombre()} agregado a la disciplina {self.__nombre}.")
        else:
            print(f"El participante {participante.obtenerNombre()} ya está inscrito en {self.__nombre}.")
