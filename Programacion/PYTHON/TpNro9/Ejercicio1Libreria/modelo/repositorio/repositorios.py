from modelo.repositorio.RepositorioLibro import RepositorioLibro

# defino un repositorio para cada entidad que tuviera en el proyecto
# lo declaro como variable global para que sea accesible desde cualquier
# parte del proyecto

# Inicializa el repositorio de libros solo una vez
repo_libro = None

def obtenerRepositorioLibro() -> RepositorioLibro:
    """Obtiene una única instancia del RepositorioLibro."""
    global repo_libro
    if repo_libro is None:
        repo_libro = RepositorioLibro()  # Instancia solo si aún no se ha creado
    return repo_libro

