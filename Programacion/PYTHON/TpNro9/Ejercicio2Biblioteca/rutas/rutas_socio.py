from flask import Blueprint, request, jsonify
from modelo.entidades.Socio import Socio
from modelo.repositorio.repositorios import obtenerRepositorioSocio

repo_socios = obtenerRepositorioSocio()

socios_bp = Blueprint('socios_bp', __name__)

"""
Desarrolle una API REST que gestione la información de los socios de la biblioteca.
    El servicio deberá proveer endpoints (rutas) para:
    a) consultar todos los socios registrados (GET)
    b) buscar un socio en particular por número de DNI (GET)
    c) agregar un nuevo socio (POST)
    d) modificar los datos de un socio por su DNI(PUT)
    e) eliminar un socio del sistema dado su DNI (DELETE).
"""

@socios_bp.route('/socios', methods=['GET'])
def obtener_socios():
    return jsonify([l.toDiccionario() for l in repo_socios.obtenerTodos()])

@socios_bp.route('/socios/<int:DNI>', methods=['GET'])
def obtener_socio(DNI):
    socio_encontrado = repo_socios.obtenerSociosPorDNI(DNI)
    if isinstance(socio_encontrado, Socio):
        return jsonify(socio_encontrado.toDiccionario())
    else:
        return jsonify({'error': 'No se encontró el socio'}), 404
    
@socios_bp.route('/socios', methods=['POST'])
def agregar_socio():
    if request.is_json:
        datos = request.get_json()
        try:
            socio = Socio.fromDiccionario(datos)
            if repo_socios.existeSocioConDNI(socio.obtenerISBN()):
                return jsonify({'error': 'El socio con ese DNI ya existe'}), 409
            repo_socios.agregar(socio)
            return jsonify(socio.toDiccionario()), 201
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'El contenido debe ser JSON'}), 400


@socios_bp.route('/socios/<int:DNI>', methods=['PUT'])
def modificar_socio(DNI):
    if request.is_json:
        datos = request.get_json()
        if "nombre" in datos and "apellido" in datos and "mail" in datos:
            nombre = datos['nombre']
            apellido = datos['apellido']
            mail = datos['mail']
            fechaDeNacimiento = datos['fechaDeNacimiento']
            
            if repo_socios.modificarPorDNI(DNI, nombre, apellido, mail, fechaDeNacimiento):
                return jsonify({'mensaje': 'Socios modificado'}), 200
            else:
                return jsonify({'error': 'No se encontró el socios'}), 404
        else:
            return jsonify({'error': 'Faltan datos'}), 400
    else:
        return jsonify({'error': 'El contenido debe ser JSON'}), 400
    
    
@socios_bp.route('/socios/<int:DNI>', methods=['DELETE'])
def eliminar_socio(DNI):
    if repo_socios.eliminarPorDNI(DNI):
        return jsonify({'mensaje': 'Libro eliminado'}), 200
    else:
        return jsonify({'error': 'No se encontró el libro'}), 404    