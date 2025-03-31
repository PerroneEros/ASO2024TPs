"""
La clase Cuidador debe tener los atributos: nombre, dirección, teléfono y un
método para asignar mascotas.
"""

from classMascota import Mascota

class Cuidador():
    #Constructor
    
    def __init__ (self, nombre:str, direccion:str, telefono:str):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__mascota = None
        
    #Comandos
    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str):
            ValueError("El nombre debe ser un string")
        else:
            self.__nombre=nombre
            
    def establecerDireccion(self, direccion:str):
        if not isinstance(direccion, str):
            ValueError("La especie debe ser un string")
        else:
            self.__direccion=direccion
            
    def establecerTelefono(self, telefono:str):
        if not isinstance(telefono, str):
            ValueError("La telefono debe ser un string")
        else:
            self.__telefono=telefono
            
    def asignarMascota(self, mascota: 'Mascota'):
        if not isinstance(mascota, Mascota):
            raise ValueError("El objeto que quieres ingresar no es una mascota")
        else:
            if self.__mascota==None:
                self.__mascota=[]
                self.__mascota.append(mascota) 
            elif mascota not in self.__mascota:
                self.__mascota.append(mascota)
            else:
                print(f"{mascota.obtenerNombre()} ya está asignada a este cuidador.")

    #Consultas
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerDireccion(self)->str:
        return self.__direccion
    
    def obtenerTelefono(self)->str:
        return self.__telefono
    
    def obtenerMascotas(self)->Mascota:
        return [mascota.obtenerNombre() for mascota in self.__mascota]
                                  