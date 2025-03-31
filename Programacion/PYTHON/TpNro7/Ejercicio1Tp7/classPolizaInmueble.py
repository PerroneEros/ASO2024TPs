class PolizaInmueble():
    
    def __init__ (self, numero:int, incendio:float, explosion:float , robo:float):
        self._numero=numero
        self._incendio=incendio
        self._explosion=explosion
        self._robo=robo

    #Consultas

    def costoPoliza(self) -> float:
        """
        Calcula el costo total de la póliza sumando los valores de los riesgos de incendio, explosión y robo.
        """
        return self._incendio + self._explosion + self._robo

    def toString(self) -> str:
        """
        Devuelve una representación en forma de string de la póliza.
        """
        return (f"Póliza {self._numero}: "
                f"Incendio = {self._incendio}, "
                f"Explosión = {self._explosion}, "
                f"Robo = {self._robo}")

    # Métodos para obtener los valores de los atributos privados
     
    def obtenerNumero(self)->int:
        return self._numero

    def obtenetIncendio(self)->float:
        return self._incendio

    def obtenerExplosion(self)->float:
        return self._explosion

    def obtenerRobo(self)->float:
        return self._robo
        
    def establecerNumero(self, numero:int):
        if not isinstance(numero, int) or numero<0:
            raise ValueError("El numero debe ser un entero positivo")
        else:
            self._numero=numero

    def establecerIncendio(self, incendio:float):
        if not isinstance(incendio, float) or numero<0:
            raise ValueError("El numero debe ser un real positivo")
        else:
            self._incendio=incendio

    def establecerExplosion(self, explosion:float):
        if not isinstance(explosion, float) or explosion<0:
            raise ValueError("El numero debe ser un entero positivo")
        else:
            self._numero=numero

    def establecerRobo(self, robo:float):
        if not isinstance(robo, float) or robo<0:
            raise ValueError("El numero debe ser un entero positivo")
        else:
            self._robo=robo                                           