from flask import Blueprint, request, jsonify
from modelo.entidades.Libro import Libro
from modelo.repositorio.repositorios import obtenerRepositorioLibro

repo_libros = obtenerRepositorioLibro()

libros_bp = Blueprint('libros_bp', __name__)

"""
a) consultar todos los libros registrados (GET)
b) buscar un libro en particular por ISBN (GET)
c) agregar un nuevo libro (POST)
d) modificar los datos de un libro ingresando su ISBN (PUT)
e) eliminar un libro del sistema dado su ISBN (DELETE)
"""

@libros_bp.route('/libros', methods=['GET'])
def obtener_libros():
    return jsonify([l.toDiccionario() for l in repo_libros.obtenerTodos()])

@libros_bp.route('/libros/<int:ISBN>', methods=['GET'])
def obtener_libro(ISBN):
    libro_encontrado = repo_libros.obtenerLibroPorISBN(ISBN)
    if isinstance(libro_encontrado, Libro):
        return jsonify(libro_encontrado.toDiccionario())
    else:
        return jsonify({'error': 'No se encontró el libro'}), 404
    
@libros_bp.route('/libros', methods=['POST'])
def agregar_libro():
    if request.is_json:
        datos = request.get_json()
        try:
            libro = Libro.fromDiccionario(datos)
            if repo_libros.existeLibroConISBN(libro.obtenerISBN()):
                return jsonify({'error': 'El libro con ese ISBN ya existe'}), 409
            repo_libros.agregar(libro)
            return jsonify(libro.toDiccionario()), 201
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'El contenido debe ser JSON'}), 400


@libros_bp.route('/libros/<int:ISBN>', methods=['PUT'])
def modificar_libro(ISBN):
    if request.is_json:
        datos = request.get_json()
        if "titulo" in datos and "autor" in datos:
            titulo = datos['titulo']
            autor = datos['autor']
            genero = datos['genero']
            anio_publicacion = datos['anio_publicacion']
            
            if repo_libros.modificarPorISBN(ISBN, titulo, autor, genero, anio_publicacion):
                return jsonify({'mensaje': 'Libro modificado'}), 200
            else:
                return jsonify({'error': 'No se encontró el libro'}), 404
        else:
            return jsonify({'error': 'Faltan datos'}), 400
    else:
        return jsonify({'error': 'El contenido debe ser JSON'}), 400
    
    
@libros_bp.route('/libros/<int:ISBN>', methods=['DELETE'])
def eliminar_libro(ISBN):
    if repo_libros.eliminarPorISBN(ISBN):
        return jsonify({'mensaje': 'Libro eliminado'}), 200
    else:
        return jsonify({'error': 'No se encontró el libro'}), 404    

