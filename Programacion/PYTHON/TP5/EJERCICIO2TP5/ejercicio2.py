'''2) A partir del siguiente diagrama que modela la clase Fecha implemente y verifique la 
clase en python encapsulando atributos y comportamiento. Considerando que: 
a) esAnterior retorna verdadero si la fecha que recibe el mensaje es anterior a 
la fecha pasada por parámetro, y falso en caso contrario. 
b) sumaDias retorna la fecha que resulta de sumar la cantidad de días recibida 
por parámetro a la fecha que recibe el mensaje 
c) diaSiguiente retorna una nueva fecha con los valores del día siguiente a la 
fecha que recibe el mensaje 
d) esIgualQue retorna true si otraFecha es equivalente a la fecha que recibe el 
mensaje  
'''
class Fecha:
    
    def _init_(self,dia:int,mes:int,anio:int):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
    '''COMANDOS'''
    def establecerDia(self,dia:int):
        self.__dia = dia
    
    def establecerMes(self,mes:int):
        self.__mes = mes 
    
    def establecerAnio(self,anio:int):
        self.__anio = anio
    

    def obtenerDia(self)->int:
     return self.__dia
    
    def obtenerMes(self)->int:
     return self.__mes

    def obtenerAnio(self)->int:
       return self.__anio
        
    def esAnterior(self,otraFecha:'Fecha')->bool:
        if self.__anio < otraFecha.obtenerAnio():
            return True
        elif self.__anio == otraFecha.obtenerAnio():
            if self.__mes < otraFecha.obtenerMes():
                return True
            elif self.__mes == otraFecha.obtenerMes():
                if self.__dia < otraFecha.obtenerDia():
                    return True
        return False
    
    def sumaDias(self,cantDias:int)->'Fecha':
        diaSiguiente = self.__dia + cantDias
        mesSiguiente = self.__mes
        anioSiguiente = self.__anio
        while diaSiguiente > 31:
            diaSiguiente -= 31
            mesSiguiente += 1
            if mesSiguiente > 12:
                mesSiguiente -= 12
                anioSiguiente += 1

        return Fecha(diaSiguiente, mesSiguiente, anioSiguiente)
    
    def diaSiguiente(self)->'Fecha':
        Dia=self.__dia
        Mes=self.__mes
        Anio=self.__anio

        DiasMeses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if self.__anio % 4 == 0 and (self.__anio % 100 != 0 or self.__anio % 400 == 0):
            DiasMeses[1] = 29  # Ajuste de febrero en años bisiestos

        Dia += 1

        if Dia > DiasMeses[self.__mes - 1]:  # Si el día excede el límite del mes
            Dia = 1
            Mes += 1

            if Mes > 12:  # Si pasa de diciembre
                Mes = 1
                Anio += 1
        
        return Fecha(Dia, Mes, Anio) 
            
    def esIgualQue(self, otraFecha:'Fecha')->bool:
        Igual=False
        if self.__anio == otraFecha.obtenerAnio():
            Igual=True
            if self.__mes == otraFecha.obtenerMes():
                Igual=True
                if self.__dia == otraFecha.obtenerDia():
                    Igual=True
                else:
                    Igual=False
            else:
                Igual=False    
        else:
            Igual=False    

        return Igual




