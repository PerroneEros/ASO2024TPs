from modelo.entidades.Libro import Libro
import json

class RepositorioLibro:
    __ruta_archivo = "datos/libros.json"

    def __init__(self):
        self.__libros = self.__cargarTodos()

    def __cargarTodos(self):
        lista = []
        try:
            with open(RepositorioLibro.__ruta_archivo, 'r') as file:
                libros = json.load(file)
                for l in libros:
                    lista.append(Libro.fromDiccionario(l))
        except FileNotFoundError:
            print("No se encontró el archivo con datos de libros.")
        except json.JSONDecodeError:
            print("Error en el formato del archivo JSON.")
        return lista

    def __guardarTodos(self):
        try:
            lista = [libro.toDiccionario() for libro in self.__libros]
            with open(RepositorioLibro.__ruta_archivo, 'w') as file:
                json.dump(lista, file, indent=4)
        except FileNotFoundError:
            print("No se encontró el archivo con datos de libros.")
    
    def obtenerTodos(self) -> list:
        return self.__libros

    def existeLibroConISBN(self, ISBN: int) -> bool:
        for libro in self.__libros:
            if ISBN == libro.obtenerISBN():
                return True
        return False

    def agregar(self, libro: Libro) -> bool:
        if not self.existeLibroConISBN(libro.obtenerISBN()):
            self.__libros.append(libro)
            self.__guardarTodos()
            return True
        return False

    def obtenerLibroPorISBN(self, ISBN: int) -> Libro:
        for libro in self.__libros:
            if ISBN == libro.obtenerISBN():
                return libro
        return None

    def eliminarPorISBN(self, ISBN: int) -> bool:
        for libro in self.__libros:
            if ISBN == libro.obtenerISBN():
                self.__libros.remove(libro)
                self.__guardarTodos()
                return True
        return False

    def modificarPorISBN(self, ISBN: int, titulo: str, autor: str, genero: str, anio_publicacion: int) -> bool:
        for libro in self.__libros:
            if libro.obtenerISBN() == ISBN:
                libro.establecerTitulo(titulo)
                libro.establecerAutor(autor)
                libro.establecerGenero(genero)
                libro.establecerAnioDePublicacion(anio_publicacion)
                self.__guardarTodos()
                return True
        return False
