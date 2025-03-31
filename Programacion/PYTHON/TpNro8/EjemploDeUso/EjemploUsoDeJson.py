import json

class Direccion:
    #metodos de clase -------------------------------------------------------------------------------------------------
    @classmethod
    def fromDiccionario(cls, data: dict)->"Direccion":
        if not isinstance(data, dict):
            raise ValueError("El parametro data debe ser un diccionario.")
        return cls(data["calle"], data["numero"])
    
    #constructor y metodos de instancia -------------------------------------------------------------------------------
    def __init__(self, calle, numero):
        if not isinstance(calle, str) or calle == "" or calle.isspace():
            raise ValueError("La calle debe ser un string valido.")
        if not isinstance(numero, int) or numero < 0:
            raise ValueError("El numero debe ser un entero positivo.")
        self.__calle = calle
        self.__numero = numero
        
    def obtenerCalle(self)->str:
        return self.__calle
    
    def obtenerNumero(self)->int:
        return self.__numero
    
    def esIgualProf(self, otra:"Direccion")->bool:
        return self.__calle == otra.obtenerCalle() and self.__numero == otra.obtenerNumero()
    
    def toDiccionario(self):
        return {"calle":self.__calle,"numero":self.__numero}   

class Persona:
    #metodos de clase-----------------------------------------------------------------------
    @classmethod
    def fromDiccionario(cls, data:dict)->"Persona":
        if not isinstance(data, dict):
            raise ValueError("El parametro data deber ser un diccionario.")
        return cls(data["nombre"], data["apellido"], Direccion.fromDiccionario(data["direccion"]))
    
    #constructor y metodos de instancia-----------------------------------------------------
    def __init__(self, nombre:str, apellido:str, direccion:Direccion):
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError("El nombre debe ser un string valido.")
        if not isinstance(apellido, str) or apellido == "" or apellido.isspace():
            raise ValueError("El apellido debe ser un string valido.")
        if not isinstance(direccion, Direccion):
            raise ValueError("La direccion debe ser una instancia de la clase direccion.")
        self.__nombre = nombre
        self.__apellido = apellido
        self.__direccion = direccion
        
    def obtenerNombre(self) -> str:
        return self.__nombre

    def obtenerApellido(self) -> str:
        return self.__apellido

    def obtenerDireccion(self) -> Direccion:
        return self.__direccion

    def esIgualProf(self, otra: "Persona") -> bool:
        return (self.__nombre == otra.obtenerNombre() and
                self.__apellido == otra.obtenerApellido() and
                self.__direccion.esIgualProf(otra.obtenerDireccion()))

    def toDiccionario(self):
        return {
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "direccion": self.__direccion.toDiccionario()
        }

        
class Equipo:
    #metodos de clase -------------------------------------------------------------------------------------------
    @classmethod
    def fromDiccionario(cls, data:dict)->"Equipo":
        if not isinstance(data, dict):
            raise ValueError("El parametro data debe ser un diccionario.")
        return cls(data["nombre"], Persona.fromDiccionario(data["lider"]))
    
    #constructor y metodo de instancia --------------------------------------------------------------------------
    def __init__(self, nombre:str, lider:Persona):
        if not isinstance(nombre, str) or nombre == "" or nombre.isspace():
            raise ValueError("El nombre debe ser un string valido.")
        if not isinstance(lider, Persona):
            raise ValueError("El lider debe ser una instancia de la clase Persona.")
        self.__nombre = nombre
        self.__lider = lider
        
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerLider(self)->Persona:
        return self.__lider
    
    def toDiccionario(self):
        return {"nombre":self.__nombre, "lider":self.__lider.toDiccionario()}
    
    def esIgualProf(self, otro:"Equipo")->bool:
        return self.__nombre == otro.obtenerNombre() and self.__lider.esIgualProf(otro.obtenerLider())
    
class Tester:
    @staticmethod
    def test():
        lista_direcciones = []
        lista_personas = []
        lista_equipos = []
        
        # Crear instancias de Direccion, Persona y Equipo
        dir1 = Direccion("Av. Siempre Viva", 742)
        dir2 = Direccion("Av. Siempre Viva", 730)
        homero = Persona("Homero", "Simpson", dir1)
        ned = Persona("Ned", "Flanders", dir2)
        equipo_homero = Equipo("Los Simpsons", homero)
        equipo_ned = Equipo("Los Flanders", ned)
        
        # Agregar instancias a las listas correspondientes
        lista_direcciones.extend([dir1, dir2])
        lista_personas.extend([homero, ned])
        lista_equipos.extend([equipo_homero, equipo_ned])
        
        # Imprimir la representación de los objetos en formato diccionario
        print("print de objeto.toDiccionario()")
        print(dir1.toDiccionario())
        print(homero.toDiccionario())
        print(equipo_homero.toDiccionario())
        print("------------------------------------------------\n")
        
        # Convertir a JSON y mostrar el JSON generado
        print("Convierto equipo.toDiccionario() a JSON con json.dumps(obj.toDiccionario(), indent=4)")
        str_equipo_homero = json.dumps(equipo_homero.toDiccionario(), indent=4)
        print("print de JSON str_equipo_homero")
        print(str_equipo_homero)
        print("print de type(str_equipo_homero)")
        print(type(str_equipo_homero))
        print("------------------------------------------------\n")
        
        # Convertir de JSON a objeto y mostrar el objeto recreado
        print("Convierto JSON a objeto con json.loads(str_equipo_homero)")
        eq_recreado = Equipo.fromDiccionario(json.loads(str_equipo_homero))
        print("print de obj.toDiccionario() de un objeto creado a partir de un JSON")
        print(eq_recreado.toDiccionario())
        print("------------------------------------------------\n")
        
        # Guardar los equipos en un archivo JSON
        print("Guardo los equipos en un archivo JSON")
        with open("equipos.json", "w") as file:
            diccionarios_equipos = [equipo.toDiccionario() for equipo in lista_equipos]
            json.dump(diccionarios_equipos, file, ensure_ascii=False, indent=4)

# Ejecutar la prueba
Tester.test()
    
    
                
         
    