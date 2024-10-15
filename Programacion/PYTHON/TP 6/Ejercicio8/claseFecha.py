class Fecha:

    #Atributos de la instancia

    #Constructor
    def __init__(self, dia:int,mes:int,anio:int):
        self.__dia=dia
        self.__mes=mes
        self.__anio=anio

    #Comandos

    def establecerDia(self,dia:int):
        self.__dia=dia

    def establecerMes(self,mes:int):
        self.__mes=mes

    def establecerAnio(self,anio:int):
        self.__anio=anio

    #Consultas
     
    def obtenerDia(self)->int:
        return self.__dia

    def obtenerMes(self)->int:
        return self.__mes

    def obtenerAnio(self)->int: 
        return self.__anio

    # a) esAnterior retorna verdadero si la fecha que recibe el mensaje es anterior a
    # la fecha pasada por parámetro, y falso en caso contrario.  
     
    def esAnterior(self,otraFecha:'Fecha')->bool:
        Anterior=False
        if (self.__anio > otraFecha.obtenerAnio()):
            Anterior=True
        elif (self.__anio==otraFecha.obtenerAnio()):
            if (self.__mes>otraFecha.obtenerMes()):
                Anterior=True
            elif (self.__mes==otraFecha.obtenerMes()):
                if(self.__dia<otraFecha.obtenerDia()):
                    Anterior=True
                else:
                    Anterior=False
            else:
                Anterior=False
        else:
            Anterior=False
        return Anterior

        # b) sumaDias retorna la fecha que resulta de sumar la cantidad de días recibida
        # por parámetro a la fecha que recibe el mensaje

    def sumaDias(self, diaUsuario: int) -> None:
        DiasMeses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if (self.__anio % 4 == 0 and (self.__anio % 100 != 0 or self.__anio % 400 == 0)):
            DiasMeses[1] = 29 

        while diaUsuario > 0:
            diasRestantesMes = DiasMeses[self.__mes - 1] - self.__dia
        
            if diaUsuario > diasRestantesMes:  
                diaUsuario -= (diasRestantesMes + 1)  
                self.__dia = 1
                self.__mes += 1

                if self.__mes > 12:  
                    self.__mes = 1
                    self.__anio += 1
            else:
                self.__dia += diaUsuario
                diaUsuario = 0

        return self.__dia, self.__mes, self.__anio    


    # c) diaSiguiente retorna una nueva fecha con los valores del día siguiente a la
    # fecha que recibe el mensaje     

    def diaSiguiente(self) -> int:
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

        return Dia, Mes, Anio                       

    # d) esIgualQue retorna true si otraFecha es equivalente a la fecha que recibe el
    # mensaje

    def esIgualQue(self,otraFecha:'Fecha')->bool:
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
    
    def __str__(self)->'str':
        return f" Dia:{self.__dia}, Mes:{self.__mes}, Anio:{self.__anio}"