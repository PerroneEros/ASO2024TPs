from modelo.repositorio.RepositorioPrestamo import RepositorioPrestamo

# defino un repositorio para cada entidad que tuviera en el proyecto
# lo declaro como variable global para que sea accesible desde cualquier
# parte del proyecto

# Inicializa el repositorio de libros solo una vez
repo_prestamo = None

def obtenerRepositorioPrestamo() -> RepositorioPrestamo:
    """Obtiene una única instancia del RepositorioLibro."""
    global repo_prestamo
    if repo_prestamo is None:
        repo_prestamo = RepositorioPrestamo()  # Instancia solo si aún no se ha creado
    return repo_prestamo