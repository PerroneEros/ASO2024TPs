
class Libro:
    def __init__(self,nombre:str,autor:str,editorial:str,categoria:chr):
        self.__nombre = nombre
        self.__autor = autor
        self.__editorial = editorial
        self.__categoria = categoria
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerAutor(self)->str:
        return self.__autor
    
    def obtenerEditorial(self)->str:
        return self.__editorial
    
    def obtenerCategoria(self)->str:
        return self.__categoria
    
    def toString(self)->str:
        return f"Nombre: {self.__nombre}, Autor: {self.__autor}, Editorial: {self.__editorial}, Categoria: {self.__categoria}"