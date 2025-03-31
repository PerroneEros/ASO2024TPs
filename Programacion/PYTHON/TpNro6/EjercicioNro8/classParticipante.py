"""
Participante: Cada participante tiene un nombre, una dirección de correo electrónico
y un número de teléfono. Los participantes pueden registrarse en uno o más
eventos.
"""

class Participante:
    def __init__ (self, nombre:str, telefono:str, correo:str):
        self.__nombre=nombre
        self.__telefono=telefono
        self.__correo=correo
        
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerTelefono(self)->str:
        return self.__telefono
    
    def obtenerCorreo(self)->str:
        return self.__correo
    
    #def eventosIncriptos(self)->Evento:
    #    return [Evento.obtenerNombre() for Evento in self.__eventos]
    
    #Comandos

    def establecerNombre(self, nombre:str):
        if not isinstance(nombre, str):
            ValueError("El nombre debe ser un string")
        else:
            self.__nombre=nombre           
            
    def establecerCorreo(self, correo:str):
        if not isinstance(correo, str):
            ValueError("El correo debe ser un string")
        else:
            self.__correo=correo
            
    def establecerTelefono(self, telefono:str):
        if not isinstance(telefono, str):
            ValueError("El telefono debe ser string")
        else:
            self.__telefono=telefono         
            
    #def inscribirAEventos(self, evento: 'Evento'):
    #    if not isinstance(evento, Evento):
    #        raise ValueError("El objeto que quieres ingresar no es un evento")
    #    else:
    #        if self.__eventos==None:
    #            self.__eventos=[]
    #            self.__eventos.append(evento) 
    #        elif evento not in self.__eventosACargo:
    #            self.__eventos.append(evento)
    #        else:
    #            print(f"{evento.obtenerNombre()} ya está asignada a este cuidador.")

