"""
2. Crea una clase Contacto que permita gestionar la información de los contactos (nombre,
apellido, teléfono, correo electrónico y dirección, todo en formato string). En la clase
implementa los métodos para serializar/deserializar el objeto utilizando los métodos
toDiccionario() y fromDiccionario(dic: dict) vistos en clase.
En la clase tester:
    a. Crea objetos de la clase Contacto y almacenarlos en una lista
"""

import json

class Contacto:
    @classmethod
    def fromDiccionario(cls, data: dict) -> "Contacto":
        if not isinstance(data, dict):
            raise ValueError("El parámetro data debe ser un diccionario.")
        return cls(data["nombre"], data["apellido"], data["telefono"], data["correo"], data["direccion"])
    
    def __init__(self, nombre: str, apellido: str, telefono: str, correo: str, direccion: str):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser un string válido.")
        if not isinstance(apellido, str) or not apellido.strip():
            raise ValueError("El apellido debe ser un string válido.")
        if not isinstance(telefono, str) or not telefono.strip():
            raise ValueError("El teléfono debe ser un string válido.")
        if not isinstance(correo, str) or not correo.strip():
            raise ValueError("El correo debe ser un string válido.")
        if not isinstance(direccion, str) or not direccion.strip():
            raise ValueError("La dirección debe ser un string válido.")
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono
        self.__correo = correo
        self.__direccion = direccion
        
    def obtenerApellido(self) -> str:
        return self.__apellido    
        
    def toDiccionario(self) -> dict:
        return {
            "nombre": self.__nombre,
            "apellido": self.__apellido, 
            "telefono": self.__telefono, 
            "correo": self.__correo, 
            "direccion": self.__direccion
        }
        

"""
    b. Guarda esa lista completa en un archivo JSON “contactos.json”.
    c. En una nueva lista vacía almacena los objetos reconstruidos a partir del archivo JSON.
    d. Pedile al usuario una letra para buscar los contactos cuyo apellido comienza con esa
        letra, y mostrá el resultado de la búsqueda por pantalla. 
"""        
class Tester:
    
    @staticmethod
    def guardar_contactos(contactos: list, archivo: str):
        """Guarda la lista de contactos en un archivo JSON."""
        with open(archivo, 'w', encoding='utf-8') as file:
            json.dump([contacto.toDiccionario() for contacto in contactos], file, ensure_ascii=False, indent=4)
    
    @staticmethod
    def cargar_contactos(desde_archivo: str) -> list:
        """Carga los contactos desde un archivo JSON y crea instancias de Contacto."""
        try:
            with open(desde_archivo, 'r', encoding='utf-8') as file:
                datos_contactos = json.load(file)
                contactos = [Contacto.fromDiccionario(data) for data in datos_contactos]
                return contactos
        except FileNotFoundError:
            print(f"Error: El archivo '{desde_archivo}' no existe.")
            return []
        except json.JSONDecodeError:
            print("Error: El archivo JSON tiene un formato incorrecto.")
            return []
    
    @staticmethod
    def mostrar_contactos(contactos: list):
        """Muestra la información de cada contacto en la lista."""
        if not contactos:
            print("No hay contactos para mostrar.")
            return
        for contacto in contactos:
            print(contacto.toDiccionario())
    
    @staticmethod
    def buscar_contactos_por_inicial_apellido(contactos: list, letra: str):
        """Busca y muestra contactos cuyo apellido empieza con la letra especificada."""
        contactos_encontrados = [contacto for contacto in contactos if contacto.obtenerApellido().startswith(letra)]
        
        if contactos_encontrados:
            print(f"Contactos con apellido que comienza con '{letra}':")
            for contacto in contactos_encontrados:
                print(contacto.toDiccionario())
        else:
            print(f"No se encontraron contactos con apellido que comience con '{letra}'.")

# Ejecución de pruebas
if __name__ == "__main__":
    # Crear y guardar contactos de prueba
    contactos = [
        Contacto("Juan", "Pérez", "123456789", "juan.perez@example.com", "Calle Falsa 123"),
        Contacto("Ana", "Gómez", "987654321", "ana.gomez@example.com", "Avenida Siempre Viva 456"),
        Contacto("Luis", "Martínez", "555123456", "luis.martinez@example.com", "Boulevard Central 789")
    ]
    
    # Guardar contactos en archivo JSON
    Tester.guardar_contactos(contactos, "contactos.json")
    
    # Cargar contactos desde el archivo JSON
    contactos_cargados = Tester.cargar_contactos("contactos.json")
    
    # Mostrar todos los contactos cargados
    print("Contactos cargados:")
    Tester.mostrar_contactos(contactos_cargados)
    
    # Buscar contactos por la letra inicial del apellido
    letra_busqueda = input("Ingrese la letra inicial del apellido para buscar: ").strip().upper()
    Tester.buscar_contactos_por_inicial_apellido(contactos_cargados, letra_busqueda)     
    
      
        
                     