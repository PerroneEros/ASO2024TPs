"""
1. Crea una clase Libro que contenga los atributos de tipo elemental (titulo, autor y género de
tipo string, año de publicación e ISBN de tipo entero) y que contenga métodos para
serializar/deserializar el objeto utilizando los métodos toDiccionario() y fromDiccionario(dic:
dict) vistos en clase.

Crea de forma manual un archivo JSON “libros.json” que contenga información de varios
libros (título, autor, género, año de publicación, ISBN) en formato JSON.
En la clase tester:
    a. Carga los datos del JSON en objetos de clase Libro y muestra por pantalla valores
de los objetos de clase Libro.
    b. Pedile al usuario un año de publicación para buscar todos los libros publicados ese
año, y mostrá por pantalla los resultados de la búsqueda. 
"""

import json

class Libro:
    
    @classmethod
    def fromDiccionario(cls, data: dict)->"Libro":
        if not isinstance(data, dict):
            raise ValueError("El parametro data debe ser un diccionario.")
        return cls(data["titulo"], data["autor"], data["genero"], data["anio"], data["ISBN"])
    
    def __init__(self, titulo:str, autor:str, genero:str, anio:int, ISBN:int):
        if not isinstance(titulo, str) or titulo == "" or titulo.isspace():
            raise ValueError("El titulo debe ser un string valido")
        if not isinstance(autor, str) or autor == "" or autor.isspace():
            raise ValueError("El autor debe ser un string valido.")
        if not isinstance(genero, str) or genero == "" or genero.isspace():
            raise ValueError("El genero debe ser un string valido.")
        if not isinstance(anio, int) or anio < 0:
            raise ValueError("El anio debe ser un entero positivo.")
        if not isinstance(ISBN, int) or ISBN < 0:
            raise ValueError("El ISBN debe ser un entero positivo.")
        self.__titulo=titulo
        self.__autor=autor
        self.__genero=genero
        self.__anio=anio
        self.__ISBN=ISBN
        
    def obtenerAnio(self) -> int:
        return self.__anio
        
    def toDiccionario(self) -> dict:
        return {
                "titulo":self.__titulo,
                "autor":self.__autor, 
                "genero":self.__genero, 
                "anio":self.__anio, 
                "ISBN":self.__ISBN
        }  
        
class Tester:
    
    @staticmethod
    def cargar_libros(desde_archivo: str) -> list:
        """Carga los libros desde un archivo JSON y crea instancias de la clase Libro."""
        try:
            with open(desde_archivo, 'r', encoding='utf-8') as file:
                datos_libros = json.load(file)
                libros = [Libro.fromDiccionario(data) for data in datos_libros]
                return libros
        except FileNotFoundError:
            print(f"Error: El archivo '{desde_archivo}' no existe.")
            return []
        except json.JSONDecodeError:
            print("Error: El archivo JSON tiene un formato incorrecto.")
            return []
    
    @staticmethod
    def mostrar_libros(libros: list):
        """Muestra la información de cada libro en la lista."""
        if not libros:
            print("No hay libros para mostrar.")
            return
        for libro in libros:
            print(libro.toDiccionario())
    
    @staticmethod
    def buscar_libros_por_anio(libros: list, anio: int):
        """Busca y muestra libros publicados en el año especificado."""
        libros_encontrados = [libro for libro in libros if libro.obtenerAnio() == anio]
        
        if libros_encontrados:
            print(f"Libros publicados en el año {anio}:")
            for libro in libros_encontrados:
                print(libro.toDiccionario())
        else:
            print(f"No se encontraron libros publicados en el año {anio}.")

# Ejecución de pruebas
if __name__ == "__main__":
    # Cargar los libros desde el archivo JSON
    libros = Tester.cargar_libros("libros.json")
    
    # Mostrar información de todos los libros cargados
    print("Libros cargados:")
    Tester.mostrar_libros(libros)
    
    # Pedir al usuario un año de publicación y buscar libros de ese año
    try:
        anio_busqueda = int(input("Ingrese un año de publicación para buscar libros: "))
        Tester.buscar_libros_por_anio(libros, anio_busqueda)
    except ValueError:
        print("Error: Debe ingresar un número entero para el año.")        
    
      
        
             