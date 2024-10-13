'''5) Una organización dedicada a la preservación del medio ambiente mantiene 
información referida a cada especie animal de la que se realiza seguimiento. Cada 
especie está caracterizada por su nombre científico, la cantidad de hembras y la 
cantidad de machos que se registran en la actualidad y el ritmo de crecimiento anual 
de la población de acuerdo a lo ocurrido en los últimos 10 años. La cantidad de 
hembras y machos tiene que ser siempre un valor no negativo, el ritmo puede ser 
cualquier valor real.  

Los tres valores numéricos se inicializan en 0 y luego pueden establecerse o 
actualizarse con un valor dado. Los comandos establecerMachos y 
establecerHembras controlan que el parámetro sea positivo, en caso contrario no 
modifican el valor del atributo. Los comandos actualizarMachos y actualizarHembras 
suman el valor del parámetro al atributo de instancia. Pueden recibir un parámetro 
negativo, pero el valor del atributo nunca debe ser menor a 0.  

La consulta clonar retorna una especie con el mismo estado interno que la especie 
que recibe el mensaje. Observe que luego de crear una especie debe establecer los 
valores de modo que el estado interno de la especie que retorna sea el mismo que el 
de la especie que recibe el mensaje.  

La organización está interesada en calcular para una especie particular: la población 
total, el nivel de riesgo de extinción (“verde” si el ritmo de crecimiento es positivo, 
“amarillo” si es nulo y “rojo” si es negativo), la población estimada para dentro de una 
cantidad dada de años, cuántos años serán necesarios estimativamente para que la 
población alcance un valor dado. Se desea determinar también si en una especie 
dada es mayor el número de hembras o de machos y entre dos especies diferentes 
cuál tiene mayor ritmo de crecimiento.  

a) A partir del diagrama y la especificación implemente la clase Especie en 
Python encapsulando atributos y comportamiento para modelar la situación 
planteada. Incluya todos los métodos auxiliares que considere oportunos, 
como así también los métodos triviales que no estén incluidos en el 
diagrama. 
 
b) Escriba una clase tester que verifique los servicios provistos por Especie con 
valores ingresados por el usuario para nombre y ritmo y generados al azar 
para machos y hembras dentro de un rango establecido '''

class Especie:
    def __init__(self,nombre:str,machos:int,hembras:int,ritmo:float):
        self.__nombre = nombre
        self.__machos = machos
        self.__hembras = hembras
        self.__ritmo = ritmo

    #comandos
    def establecerHembras(self,cantHembras:int):
        if cantHembras >= 0:
            self.__hembras = cantHembras
        
    def establecerMachos(self,cantMachos:int):
        if cantMachos >= 0:
            self.__machos = cantMachos
    
    def establecerRitmo(self,ritmo:float):
        self.__ritmo = ritmo
    
    def actualizarHembras(self,cantHembras:int):
        self.__hembras += cantHembras
        if self.__hembras < 0:
            self.__hembras = 0
    
    def actualizarMachos(self, cantMachos:int):
        self.__machos += cantMachos
        if self.__machos < 0:
            self.__machos = 0
    
    def actualizarRitmo(self,ritmo:float):
        self.__ritmo += ritmo
        if self.__ritmo < 0:
            self.__ritmo = 0
    
    #consultas
    def obtenerHembras(self)->int:
        return self.__hembras
    
    def obtenerMachos(self)->int:
        return self.__machos
    
    def obtenerRitmo(self)->float:
        return self.__ritmo
    
    def obtenerNombre(self)->str:
        return self.__nombre
    
    def poblacionActual(self)->int:
        poblacionActual = self.__machos + self.__hembras 
        return poblacionActual
    
    def poblacionEstimada(self,anios:int)->int:
        poblacionEstimada = self.__machos + self.__hembras + (self.__ritmo * anios)
        return poblacionEstimada
    
    def aniosParaPoblacion(self,poblacion:int)->int:
        aniosParaPoblacion = (poblacion - self.poblacionActual()) / (self.__machos + self.__hembras)
        return aniosParaPoblacion
    
    def riesgo(self)->str:
        if self.__ritmo > 0:
            return "verde"
        elif self.__ritmo == 0:
            return "amarillo"
        else:
            return "rojo"
    
    def masHembras(self)->bool:
        masHembras = False
        if self.__hembras > self.__machos:
            masHembras = True
        else:
            masHembras = False
        
        return masHembras
    
    def mayorRitmo(self,otraEspecie:'especie')->bool:
        mayorRitmo = False
        if self.__ritmo > otraEspecie.obtenerRitmo():
            mayorRitmo = True
            return mayorRitmo
        else:
            mayorRitmo = False
            return mayorRitmo
    
    def clonar(self)->'Especie':
        clon = Especie(self.__nombre, self.__machos, self.__hembras, self.__ritmo)
        return clon
    
    def toStrintg(self)->str:
        return f"Nombre: {self.__nombre}, Machos: {self.__machos}, Hembras: {self.__hembras}, Ritmo: {self.__ritmo}"
    




