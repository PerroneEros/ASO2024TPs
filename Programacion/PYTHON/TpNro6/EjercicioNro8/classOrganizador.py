"""
Organizador: Cada organizador tiene un nombre, una dirección de correo electrónico
y una especialidad (por ejemplo, planificación de eventos, catering, músico, DJ, etc.).
Cada organizador puede estar a cargo de uno o más eventos.
"""

class Organizador:
    
    def __init__ (self, nombre:str, correo:str, especialidad:str):
        self.__nombre=nombre
        self.__correo=correo
        self.__especialidad=especialidad
        
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerCorreo(self)->str:
        return self.__correo    
    
    def obtenerEspecialidad(self)->str:
        return self.__especialidad
    
    #def eventosACargo(self)->Evento:
    #    return [Evento.obtenerNombre() for Evento in self.__eventosACargo]
    
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
            
    def establecerEspecialidad(self, especialidad:str):
        if not isinstance(especialidad, str):
            ValueError("El especialidad debe ser string")
        else:
            self.__especialidad=especialidad        
            
    #def establecerEventosACargo(self, evento: 'Evento'):
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