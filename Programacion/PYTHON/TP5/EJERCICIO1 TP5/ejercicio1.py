class Atleta:
    MAX_VALOR = 100
    MIN_VALOR = 0

    def __init__(self,nombre:str,energia:int= MAX_VALOR,destreza:int=MIN_VALOR):
        self.__nombre = nombre
        self.__energia = energia
        self.__destreza = destreza
        self.__entrenamiento = 0
    
    def Entrenar(self):
        if self.__energia - 5 > Atleta.MIN_VALOR: 
            self.__energia -= 5
            self.__entrenamiento += 1
            if self.__entrenamiento == 5:
                self.__destreza += 1
                self.__entrenamiento = 0
        else:
            print("el atleta esta cansado, no puede entrenar")
            self.__energia = Atleta.MIN_VALOR
        
        return self.__energia,self.__entrenamiento,self.__destreza   
        
    def Descansar(self):
        if self.__energia + 20 > Atleta.MAX_VALOR:
            self.__energia = Atleta.MAX_VALOR
        else:
            self.__energia += 20

        return self.__energia

    def obtenerNombre(self)->str:
        return self.__nombre

    def obtenerEnergia(self)->int:
        return self.__energia
    
    def obtenerDestreza(self)->int:
        return self.__destreza

    def mismaDestrezaQue(self,otroAtleta:'Atleta')->bool:
        if self.__destreza == otroAtleta.obtenerDestreza():
            return True
        else:
            return False
     
    def mayorDestrezaQue(self,otroAtleta:'Atleta')->bool:
        if self.__destreza > otroAtleta.obtenerDestreza():
            return True
        else:
            return False
        