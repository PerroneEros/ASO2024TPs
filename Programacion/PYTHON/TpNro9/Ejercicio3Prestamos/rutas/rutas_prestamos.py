from flask import Blueprint, request, jsonify
from modelo.repositorio.repositorios import obtenerRepositorioPrestamo
from modelo.entidades.Prestamo import Prestamo

repo_prestamos = obtenerRepositorioPrestamo()
bp_prestamos = Blueprint("bp_prestamos", __name__)

@bp_prestamos.route("/prestamos", methods=["POST"])
def agregar_prestamo():
    if not request.is_json:
        return jsonify({"mensaje": "Error, los datos deben estar en formato JSON."}), 400

    datos = request.json
    try:
        prestamo = Prestamo.fromDiccionario(datos)
    except Exception as e:
        return jsonify({"error": "No se pudo crear el préstamo con los datos recibidos.", "detalle": str(e)}), 400

    if repo_prestamos.existePrestamoConID(prestamo.obtenerID()):
        return jsonify({"mensaje": "El préstamo con el ID especificado ya existe."}), 400

    # Validar lógica de negocio aquí (e.g., ejemplares disponibles)
    if repo_prestamos.agregar(prestamo):
        return jsonify({"mensaje": "Préstamo agregado con éxito.", "prestamo": datos}), 201
    else:
        return jsonify({"mensaje": "Error al agregar el préstamo."}), 500

@bp_prestamos.route("/prestamos", methods=["GET"])
def obtener_todos_los_prestamos():
    prestamos = [prestamo.toDiccionario() for prestamo in repo_prestamos.obtenerTodos()]
    return jsonify(prestamos), 200

@bp_prestamos.route("/prestamos/<int:id>", methods=["GET"])
def obtener_prestamo_por_id(id):
    prestamo = repo_prestamos.obtenerPrestamoPorID(id)
    if prestamo:
        return jsonify(prestamo.toDiccionario()), 200
    return jsonify({"mensaje": f"No se encontró un préstamo con ID {id}."}), 404

@bp_prestamos.route("/prestamos/<int:id>", methods=["DELETE"])
def eliminar_prestamo(id):
    if repo_prestamos.existePrestamoConID(id):
        if repo_prestamos.eliminarID(id):
            return jsonify({"mensaje": "Préstamo eliminado con éxito."}), 200
        return jsonify({"mensaje": "Error al eliminar el préstamo."}), 500
    return jsonify({"mensaje": f"El préstamo con ID {id} no existe."}), 404
