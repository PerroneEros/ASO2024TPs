class Persona():
    
    def __init__(self, nombre:str, apellido:str, dni:str, nroLegajo:int):
        self._nombre=nombre
        self._apellido=apellido
        self._dni=dni
        self._nroLegajo=nroLegajo
        
    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str):
            raise ValueError("El nombre debe ser un string")
        else:
            self._nombre=nombre
            
    def establecerApellido(self, apellido:str):
        if not isinstance(apellido, str):
            raise ValueError("El nombre debe ser un string")
        else:
            self._apellido=apellido
            
    def establecerDni(self, dni:str):
        if not isinstance(dni, str):
            raise ValueError("El dni debe ser un string")
        else:
            self._dni=dni
            
    def establecerNroLegajo(self, nroLegajo:int):
        if not isinstance(nroLegajo, int) or nroLegajo < 0:
            raise ValueError("El nroLegajo debe ser un entero positivo")
        
    def obtenerNombre(self)->str:
        return self._nombre
    
    def obtenerApellido(self)->str:
        return self._apellido
    
    def obtenerDni(self)->str:
        return self._dni
    
    def obtenerNroLegajo(self)->str:
        return self._nroLegajo                                