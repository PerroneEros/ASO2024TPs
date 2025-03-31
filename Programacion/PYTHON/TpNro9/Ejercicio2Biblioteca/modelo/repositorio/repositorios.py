from modelo.repositorio.RepositorioSocio import RepositorioSocios

# defino un repositorio para cada entidad que tuviera en el proyecto
# lo declaro como variable global para que sea accesible desde cualquier
# parte del proyecto

# Inicializa el repositorio de libros solo una vez
repo_socio = None

def obtenerRepositorioSocio() -> RepositorioSocios:
    """Obtiene una única instancia del RepositorioLibro."""
    global repo_socio
    if repo_socio is None:
        repo_socio = RepositorioSocios()  # Instancia solo si aún no se ha creado
    return repo_socio