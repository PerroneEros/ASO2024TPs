class Automovil:
    def __init__(self,marca:str,modelo:str,anio:int,VelocidadMaxima:float,VelocidadActual:float):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__VelocidadMaxima = VelocidadMaxima
        self.__VelocidadActual = VelocidadActual
    
    def establecerMarca(self,marca:str):
        self.__marca = marca
    
    def establecerModelo(self,modelo:str):
        self.__modelo = modelo
    
    def  establecerAnio(self,anio:int):
        self.__anio = anio

    def establecerVelocidadMaxima(self,VelocidadMaima:float):
        self.__VelocidadMaxima = VelocidadMaima

    def establecerVelocidadActual(self,VelocidadActual:float):
        self.__VelocidadActual = VelocidadActual

    def acelerar(self,incrementoVelocidad:int):
        if ((self.__VelocidadActual + incrementoVelocidad) > self.__VelocidadMaxima):
            print("FLAQUITO BAJALE QUE VAS MUY RAPIDO")
        else:
            self.__VelocidadActual = self.__VelocidadActual + incrementoVelocidad
            print(f"estas yendo a {self.__VelocidadActual} km/h ")
    
    def desacelerar(self,decrementoVelocidad:int):
        if ((self.__VelocidadActual - decrementoVelocidad) <= 0):
            print("se te paro el auto")
            self.__VelocidadActual = 0
        else:
            self.__VelocidadActual = self.__VelocidadActual - decrementoVelocidad
            print(f"se bajo la velocidad hasta {self.__VelocidadActual}")
    
    def frenarPorCompleto(self):
        self.__VelocidadActual = 0
        return self.__VelocidadActual
    
    def obtenerMarca(self)->str:
        return self.__marca

    def obtenerModelo(self)->str:
        return self.__modelo   
    
    def obtenerAnio(self)->int:
        return self.__anio
    
    def obtenerVelocidadMaxima(self)->float:
        return self.__VelocidadMaxima
    
    def obtenerVelocidadActual(self)->float:
        return self.__VelocidadActual
    
    def calcularMinutosParaLlegar(self,distanciaKM:float)->int:
        timpoParaLlegar = 0
        if self.__VelocidadActual <= 0:
            print("El auto esta detenido y no se puede calcular el timpo para llrgar")
        else:
            timpoParaLlegar = int((distanciaKM/ self.__VelocidadActual)*60) 
        
        return timpoParaLlegar
    