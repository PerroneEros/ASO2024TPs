'''3) El sistema de colores RGB (Red, Green, Blue) es un modelo de colores aditivos que 
combina estos tres colores primarios para crear una amplia gama de colores. Cada 
color en el modelo RGB se representa con tres componentes: 
a) Rojo (R): Intensidad de la luz roja (de 0 a 255). 
b) Verde (G): Intensidad de la luz verde (de 0 a 255). 
c) Azul (B): Intensidad de la luz azul (de 0 a 255). 

Cuando se combinan diferentes intensidades de estos colores, se puede formar 
cualquier color visible. Por ejemplo: 
d) Blanco se forma con R=255, G=255, B=255. 
e) Negro se forma con R=0, G=0, B=0. 
f) Gris tiene valores iguales para R, G, y B (por ejemplo, R=50, G=50, B=50). 
La combinación y variación de estos valores permite definir colores precisos para 
una variedad de aplicaciones, como pantallas y gráficos.

variar(val:entero), modifica cada componente de color sumándole si es 
posible, un valor dado. Si sumándole el valor dado a una o varias 
componentes se supera el valor 255, dicha componente queda en 255. Si el 
argumento es negativo la operación es la misma pero en ese caso el mínimo 
valor que puede tomar una componente, es 0. 
● variarRojo(val:entero), modifica la componente de rojo sumándole un valor 
dado. Ídem para azul (variarAzul(val:entero)) y verde 
(variarVerde(val:entero)). 
● esRojo() retorna el valor verdadero si el objeto que recibe el mensaje 
representa el color rojo. Ídem para gris (esGris()) y para negro (esNegro()) 
● complemento() retorna un nuevo objeto con el color complemento del color 
del objeto que recibe el mensaje para alcanzar el color blanco. 
● esIgualQue(otroColor:Color): retorna el valor verdadero si ambos objetos 
son equivalentes. 
● clonar(): devuelve un nuevo color con el mismo estado interno que el color 
que recibe el mensaje. 
A partir del diagrama presentado y la especificación, implemente y verifique la clase 
Color en Python encapsulando atributos y comportamiento para modelar la situación 
planteada. Incluya todos los métodos auxiliares que considere oportunos.
'''
class Color:
    def __init__(self,rojo = 255,verde = 255,azul = 255):
        self.__rojo = rojo
        self.__verde = verde
        self.__azul = azul
    #consultas
    def obtenerRojo(self)->int:
        return self.__rojo
    
    def obtenerVerde(self)->int:
        return self.__verde
    
    def obtenerAzul(self)->int:
        return self.__azul
    
    def esRojo(self)->bool:
        esRojoBool = False
        if self.__rojo > 0 and (self.__verde == 0 and self.__azul == 0):
            esRojoBool = True
            return esRojoBool
        else:
            return esRojoBool
    
    def esGris(self)->bool:
        esGrisBool = False
        if self.__rojo == self.__verde and self.__verde == self.__azul:
            esGrisBool = True
            return esGrisBool
        else:
            return esGrisBool
    
    def esNegro(self)->bool:
        esNegroBool = False
        if self.__rojo == 0 and self.__verde == 0 and self.__azul == 0:
            esNegroBool = True
            return esNegroBool
        else:
            return esNegroBool
    
    def complemento(self)->'color':
        complementoRojo = 255 - self.__rojo
        complementoVerde = 255 - self.__verde
        complementoAzul = 255 - self.__azul

        return Color(complementoRojo, complementoVerde, complementoAzul)
    
    def esIgualQue(self,otroColor ='color')->bool:
        esIgualBool = False
        if self.__rojo == otroColor.obtenerRojo() and self.__verde == otroColor.obtenerVerde() and self.__azul == otroColor.obtenerAzul():
            esIgualBool = True
            return esIgualBool
        else:
            return esIgualBool
    
    def clonar(self)->'color':
        Rojo = self.__rojo
        Verde = self.__verde
        Azul = self.__azul
        
        clonado = Color(Rojo, Verde, Azul)
        
        return clonado

    #COMANDOS
    def variar(self,valor:int):
        
        if self.__rojo + valor > 255:
            self.__rojo = 255
        elif self.__rojo + valor < 0:
            self.__rojo = 0
        else:
            self.__rojo += valor
        
        if self.__verde + valor > 255:
            self.__verde = 255
        elif self.__verde + valor < 0:
            self.__verde = 0
        else:
            self.__verde += valor
        
        if self.__azul + valor > 255:
            self.__azul = 255
        elif self.__azul + valor < 0:
            self.__azul = 0
        else:
            self.__azul += valor

    def variarRojo(self, valor:int):
        if self.__rojo + valor > 255:
            self.__rojo = 255
        elif self.__rojo + valor < 0:
            self.__rojo = 0
        else:
            self.__rojo += valor

    def variarAzul(self,valor:int):
        if self.__azul + valor > 255:
            self.__azul = 255
        elif self.__azul + valor < 0:
            self.__azul = 0
        else:
            self.__azul += valor

    def variarVerde(self, valor:int):
        if self.__verde + valor > 255:
            self.__verde = 255
        elif self.__verde + valor < 0:
            self.__verde = 0
        else:
            self.__verde += valor

    def establecerRojo(self,valor:int):
        if valor > 255:
            self.__rojo = 255
        elif valor < 0:
            self.__rojo = 0
        else:
            self.__rojo = valor
        
    def establecerAzul(self, valor:int):
        if valor > 255:
            self.__azul = 255
        elif valor < 0:
            self.__azul = 0
        else:
            self.__azul = valor

    def establecerVerde(self, valor:int):
        if valor > 255:
            self.__verde = 255
        elif valor < 0:
            self.__verde = 0
        else:
            self.__verde = valor        
    
    def copiar(self,otroColor:'color'):
        copiaRojo = otroColor.obtenerRojo()
        copiaVerde = otroColor.obtenerVerde()
        copiaAzul = otroColor.obtenerAzul()

        copia = Color(copiaRojo, copiaVerde, copiaAzul)
        
        return copia
    