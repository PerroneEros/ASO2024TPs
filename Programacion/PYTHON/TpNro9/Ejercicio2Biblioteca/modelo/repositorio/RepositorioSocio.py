from modelo.entidades.Socio import Socio
import json
from typing import Optional

class RepositorioSocios:
    __ruta_archivo = "datos/socios.json"

    def __init__(self):
        self.__socios = self.__cargarTodos()

    def __cargarTodos(self):
        lista = []
        try:
            with open(RepositorioSocios.__ruta_archivo, 'r') as file:
                socios = json.load(file)
                for s in socios:
                    lista.append(Socio.fromDiccionario(s))
        except FileNotFoundError:
            print("No se encontró el archivo con datos de socios.")
        except json.JSONDecodeError:
            print("Error en el formato del archivo JSON.")
        return lista

    def __guardarTodos(self):
        try:
            lista = [socio.toDiccionario() for socio in self.__socios]
            with open(RepositorioSocios.__ruta_archivo, 'w') as file:
                json.dump(lista, file, indent=4)
        except IOError:
            print("Error al guardar los datos de los socios.")
    
    def obtenerTodos(self) -> list:
        return self.__socios

    def existeSocioConDNI(self, DNI: int) -> bool:
        return any(socio.obtenerDNI() == DNI for socio in self.__socios)

    def agregar(self, socio: Socio) -> bool:
        if not self.existeSocioConDNI(socio.obtenerDNI()):
            self.__socios.append(socio)
            self.__guardarTodos()
            return True
        return False

    def obtenerSociosPorDNI(self, DNI: int) -> Optional[Socio]:
        for socio in self.__socios:
            if DNI == socio.obtenerDNI():
                return socio
        return None

    def eliminarPorDNI(self, DNI: int) -> bool:
        for socio in self.__socios:
            if DNI == socio.obtenerDNI():
                self.__socios.remove(socio)
                self.__guardarTodos()
                return True
        return False

    def modificarPorDNI(self, DNI: int, nombre: str, apellido: str, mail: str, fechaDeNacimiento: str) -> bool:
        for socio in self.__socios:
            if socio.obtenerDNI() == DNI:
                socio.establecerNombre(nombre)
                socio.establecerApellido(apellido)
                socio.establecerMail(mail)
                socio.establecerFechaDeNacimiento(fechaDeNacimiento)
                self.__guardarTodos()
                return True
        return False

    def actualizarSocios(self):
        self.__socios = self.__cargarTodos()
