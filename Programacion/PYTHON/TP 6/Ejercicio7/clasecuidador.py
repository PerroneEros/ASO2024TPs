'''7) Un refugio de animales nos pide diseñar un sistema simple para gestionar las 
mascotas en el refugio. El sistema permitirá registrar mascotas y sus cuidadores, así 
como asignar y gestionar el cuidado de las mascotas. 
 
Mascota: Cada mascota tiene un nombre, una especie (por ejemplo, perro, gato), 
una edad y una descripción. Las mascotas pueden ser asignadas a un cuidador. 

Cuidador: Cada cuidador tiene un nombre, una dirección y un número de teléfono. 
Los cuidadores pueden ser asignados a una o más mascotas. 
 
A. Crea un diagrama de clases que incluya dos clases principales: Mascota y 
Cuidador. 
La clase Mascota debe tener los atributos: nombre, especie, edad, 
descripción. 
La clase Cuidador debe tener los atributos: nombre, dirección, teléfono y un 
método para asignar mascotas. 
B. Implementar las clases con python '''

from clasemascota import Mascota
class Cuidador():
    def __init__(self,nombre:str,direccion:str,telefono:str):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__mascota = None
    
    #comandos
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
    
    def agregarMascota(self, mascota:'Mascota'):
            if not isinstance(mascota, Mascota):
                raise ValueError("El objeto que quieres ingresar no es una mascota")
            else:
                if self.__mascota == None:
                    self.__mascota=[]
                    self.__mascota.append(mascota) 
                elif mascota not in self.__mascota:
                    self.__mascota.append(mascota)
                else:
                    print(f"{mascota.obtenerNombre()} ya está asignada a este cuidador.")

    #consultas
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerDireccion(self)->str:
        return self.__direccion
    
    def obtenerTelefono(self)->str:
        return self.__telefono
    
    def obtenerMascotas(self)->Mascota:
        return [mascota.obtenerNombre() for mascota in self.__mascota]
    
    def __str__(self)->str:
        return f"Nombre: {self.__nombre}, Dirección: {self.__direccion}, Teléfono: {self.__telefono}, Mascotas: {self.__mascota}"