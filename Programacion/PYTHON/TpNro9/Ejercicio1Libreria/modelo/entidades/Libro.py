"""
    1) En una biblioteca almacenan la siguiente información de los libros: título, autor,
    género, año de publicación e ISBN. ISBN son las siglas de International Standard
    Book Number (Número Internacional Normalizado del Libro), y es un número que
    permite identificar de forma unívoca a un libro en particular.
    Desarrolle una API REST que gestione la información de los libros de la biblioteca.
    El servicio deberá proveer endpoints (rutas) para:
    a) consultar todos los libros registrados (GET)
    b) buscar un libro en particular por ISBN (GET)
    c) agregar un nuevo libro (POST)
    d) modificar los datos de un libro ingresando su ISBN (PUT)
    e) eliminar un libro del sistema dado su ISBN (DELETE)
    Al agregar un nuevo libro no se debe duplicar la información existente, por lo tanto,
    hay que verificar que el libro no exista antes de agregarlo.
"""

class Libro:

    @classmethod
    def fromDiccionario(cls, data: dict) -> "Libro":
        if not isinstance(data, dict):
            raise ValueError("El parámetro data debe ser un diccionario.")
        return cls(data["ISBN"], data["titulo"], data["autor"], data["genero"], data["anio_publicacion"])
    
    #metodos de instancia
    def __init__(self, ISBN:int, titulo:str, autor:str, genero:str, anio_publicacion:int):
        if not isinstance(ISBN, int) or ISBN<0:
            raise ValueError("El ISBN debe ser un entero")
        if not isinstance(titulo, str) or titulo=="" or titulo.isspace():
            raise ValueError("El titulo debe ser un string")
        if not isinstance(autor, str) or autor=="" or autor.isspace():
            raise ValueError("El autor debe ser un string")
        if not isinstance(genero, str) or genero=="" or genero.isspace():
            raise ValueError("El genero debe ser un string")
        if not isinstance(anio_publicacion, int) or anio_publicacion<0:
            raise ValueError("El anio de publicacion debe ser un int valido")
        self.__ISBN = ISBN
        self.__titulo = titulo
        self.__autor = autor
        self.__genero=genero
        self.__anio_publicacion=anio_publicacion

    #consultas
    def obtenerISBN(self)->int:
        return self.__ISBN
    
    def obtenerTitulo(self)->str:
        return self.__titulo
    
    def obtenerAutor(self)->str:
        return self.__autor
    
    def obtenerGenero(self)->str:
        return self.__genero
    
    def obtenerAnioDePublicacion(self)->int:
        return self.__anio_publicacion
    
    def toDiccionario(self)->dict:
        return {
            "ISBN": self.__ISBN,
           "titulo": self.__titulo,
           "autor": self.__autor,
           "genero": self.__genero,
           "anio_publicacion": self.__anio_publicacion
           }

    def establecerTitulo(self, titulo:str):
        if not isinstance(titulo, str) or titulo=="" or titulo.isspace():
            raise TypeError(" El titulo debe ser un string valido ")
        self.__titulo = titulo
        
    def establecerAutor(self, autor:str):    
        if not isinstance(autor, str) or autor=="" or autor.isspace():
            raise TypeError(" El autor debe ser un string valido ")
        self.__autor = autor
        
    def establecerGenero(self, genero:str):
        if not isinstance(genero, str) or genero=="" or genero.isspace():
            raise TypeError("El genero debe ser un string valido")
        self.__genero = genero
        
    def establecerAnioDePublicacion(self, anio_publicacion:int):
        if not isinstance(anio_publicacion, int) or anio_publicacion<0:
            raise TypeError("El anio de publicacion no puede ser un entero negativo")
        self.__anio_publicacion = anio_publicacion        
    
    def toString(self)->str:
        return {f"ISBN:{self.__ISBN}, titulo:{self.__titulo}, autor:{self.__autor}, genero:{self.__genero},AnioDeLanzamiento:{self.__anio_publicacion}"}