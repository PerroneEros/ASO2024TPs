"""

3) El sistema de colores RGB (Red, Green, Blue) es un modelo de colores aditivos que
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

"""    

class color():

    #Atributos de la instacia rojo, azul, verde

    #Constructores...

    def __init__(self, rojo:int=255, azul:int=255, verde:int=255):
        self.__rojo=rojo
        self.__azul=azul
        self.__verde=verde

    # variar(val:entero), modifica cada componente de color sumándole si es
    # posible, un valor dado. Si sumándole el valor dado a una o varias
    # componentes se supera el valor 255, dicha componente queda en 255. Si el
    # argumento es negativo la operación es la misma pero en ese caso el mínimo
    # valor que puede tomar una componente, es 0. 
     
    def obtenerRojo(self):
        return self.__rojo

    def obtenerAzul(self):
        return self.__azul

    def obtenerVerde(self):
        return self.__verde           

    def variar(self,valor:int):
        
        if self.__rojo+valor>255:
            self.__rojo=255
        elif self.__rojo+valor<0:
            self.__rojo=0
        else:        
            self.__rojo+=valor

        if self.__azul+valor>255:
            self.__azul=255
        elif self.__azul+valor<0:
            self.__azul=0            
        else:
            self.__azul+=valor

        if self.__verde+valor>255:
            self.__verde=255
        elif self.__verde+valor<0:
            self.__verde=0            
        else:
            self.__verde+=valor   

    # ● variarRojo(val:entero), modifica la componente de rojo sumándole un valor
    # dado. Ídem para azul (variarAzul(val:entero)) y verde
    # (variarVerde(val:entero))

    def variarRojo(self,valor:int):

        if self.__rojo+valor>255:
            self.__rojo=255
        elif self.__rojo+valor<0:
            self.__rojo=0
        else:
            self.__rojo+=valor

    def variarAzul(self,valor:int):

        if self.__azul+valor>255:
            self.__azul=255
        elif self.__azul+valor<0:
            self.__azul=0
        else:
            self.__azul+=valor

    def variarVerde(self,valor:int):

        if self.__verde+valor>255:
            self.__verde=255
        elif self.__verde+valor<0:
            self.__verde=0
        else:
            self.__verde+=valor

    # ● esRojo() retorna el valor verdadero si el objeto que recibe el mensaje
    # representa el color rojo. Ídem para gris (esGris()) y para negro (esNegro())
     
    def esRojo(self)->bool:
        esRojoBool=False
        if self.__rojo > 0 and self.__azul==0 and self.__verde==0:
            esRojoBool=True
        else:
            esRojoBool=False

        return esRojoBool

    def esGris(self)->bool:
        esGrisBool=False
        if self.__rojo==200 and self.__verde==200 and self.__azul==200:
            esGrisBool=True
        elif self.__rojo==128 and self.__verde==128 and self.__azul==128:
            esGrisBool=True
        elif self.__rojo==50 and self.__azul==50 and self.__verde==50:
            esGrisBool=True
        else:
            esGrisBool=False

        return esGrisBool


    def esNegro(self)->bool:
        esNegroBool=False
        if self.__rojo==0 and self.__azul==0 and self.__verde==0:
            esNegroBool=True
        else:
            esNegroBool=False

        return esNegroBool

    # ● complemento() retorna un nuevo objeto con el color complemento del color
    # del objeto que recibe el mensaje para alcanzar el color blanco.

    def complemento(self)->'color':
        Rojo=255-self.__rojo
        Azul=255-self.__azul
        Verde=255-self.__verde

        colorComplemento=color(Rojo,Azul,Verde)

        return colorComplemento

   # ● esIgualQue(otroColor:Color): retorna el valor verdadero si ambos objetos
   # son equivalentes

    def esIgualQue(self,otroColor='color')->bool:
        esIgual=False
        if self.__rojo==otroColor.obtenerRojo() and self.__azul==otroColor.obtenerAzul() and self.__verde==otroColor.obtenerVerde():
            esIgual=True
        else:
            esIgual=False

        return esIgual

    # ● clonar(): devuelve un nuevo color con el mismo estado interno que el color
    # que recibe el mensaje.

    def clonar(self)->'color':
        Rojo=self.__rojo
        Azul=self.__azul
        Verde=self.__verde

        Clonado=color(Rojo,Azul,Verde)

        return Clonado

            
              

