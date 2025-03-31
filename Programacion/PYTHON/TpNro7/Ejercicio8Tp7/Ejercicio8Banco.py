"""
    8. Un banco ofrece a sus clientes dos tipos de cuentas bancarias: cuenta corriente y
    caja de ahorros. 
    * Las cuentas tienen un saldo, y se mantiene la cantidad de extracciones y depósitos que realiza en el mes, 
    también tienen una tasa de interés anual y un valor de comisión mensual. 
"""

from abc import ABC, abstractmethod

class Cuenta(ABC):
    
    def __init__(self, saldo:float, cantExtracciones:int, cantDepositos:int, tazaInteresAnual:float, valorComisionMensual:float):
        
        if not isinstance(saldo, (int, float)):
           raise ValueError("El saldo debe ser un numero")
        else:
            self._saldo=saldo
         
        if not isinstance(cantExtracciones, int) or cantExtracciones<0:
            raise ValueError("La cantidad de extracciones debe ser un entero positivo")
        else:
            self._cantExtracciones=cantExtracciones
            
        if not isinstance(cantDepositos, int) or cantDepositos<0:
            raise ValueError("La cantidad de depositos debe ser un entero positivo")
        else:
            self._cantDepositos=cantDepositos
            
        if not isinstance(tazaInteresAnual, (int, float)) or tazaInteresAnual<0:
            raise ValueError("La taza de interes anual debe ser un numero positivo")
        else:
            self._tazaInteresAnual=tazaInteresAnual
            
        if not isinstance(valorComisionMensual, (int,float)) or valorComisionMensual<0:
            raise ValueError("El valor de la comision mensual debe ser un numero positivo")
        else:
            self._valorComisionMensual=valorComisionMensual
            
    """
    * En las cuentas se puede depositar y extraer dinero, en éste último caso siempre verificando que se pueda. Mensualmente se
    genera un extracto que actualiza el saldo de la cuenta restándole el valor de la comisión y actualiza el saldo de la 
    cuenta calculando el interés ganado, retornando un string con la información de la cuenta.
    """
    
    #Consultas y comandos abstractos
    
    @abstractmethod
    def Depositar(self, depositar:float):
        pass
    
    @abstractmethod
    def Extraer(self, extraer:float):
        pass
    
    @abstractmethod
    def ActMensual(self)->str:
        pass
    
"""
-> Cuenta de ahorros: posee un atributo para determinar si la cuenta de ahorros está
    activa (tipo boolean). Si el saldo es menor a $0 la cuenta está inactiva, en caso
    contrario se considera activa. 
"""
    
class CuentaAhorros(Cuenta):
    
    __COMISION_EXTRA=1000
    
    def __init__(self, saldo:float, cantExtracciones:int, cantDepositos:int, tazaInteresAnual:float, valorComisionMensual:float, activa:bool):
        super().__init__(saldo, cantExtracciones, cantDepositos, tazaInteresAnual, valorComisionMensual)
        if not isinstance(activa, bool):
            raise ValueError("El estado de la cuenta debe de ser booleano")
        else:
            if (self._saldo<0 and activa==False):
                self.__activa=False
                
            if (self._saldo>0 or activa==True):
                self.__activa=True    
    
    """            
        La cuenta de ahorros se comporta de la siguiente
        forma:
        
            • Depositar: se puede depositar dinero si la cuenta está activa.
            • Retirar: es posible retirar dinero si la cuenta está activa.         
    """ 
    
    def Depositar(self, depositar:float):
        if not isinstance(depositar, (int, float)) or depositar<0:
            raise ValueError("El deposito debe ser un numero positivo")
        else:
            if self.__activa==True:
                print(f"Depositaste {depositar}$")
                self._saldo+=depositar
            else:
                print("Tu cuenta esta inactiva")    
    
    def Extraer(self, extraer:float):
        if not isinstance(extraer, (int,float)) or extraer<0:
            raise ValueError("El dinero a extraer debe ser un numero positivo")
        else:
            if self.__activa==True and extraer < self._saldo:
                print(f"Se extrajo {extraer}$")
                self._saldo-=extraer
            else:
                print("Tu cuenta esta inactiva o no te da el saldo")
                
    def __str__(self) -> str:
        return (f"Cuenta:\n"
                f"Saldo: {self._saldo}\n"
                f"Cantidad de Extracciones: {self._cantExtracciones}\n"
                f"Cantidad de Depósitos: {self._cantDepositos}\n"
                f"Tasa de Interés Anual: {self._tazaInteresAnual}%\n"
                f"Valor Comisión Mensual: {self._valorComisionMensual}\n"
                f"Estado: {self.__activa}")                
        
    """
        • Extracto mensual: si el número de retiros es mayor que 4, por cada retiro adicional, se cobra $1000 
            como comisión mensual. Al generar el extracto, se determina si la cuenta queda activa o no con el saldo 
            (la comisión puede dejarla en saldo negativo).  
    """
    
    def ActMensual(self)->str:
        # Calcular interés ganado
        interes_ganado = (self.tazaInteresAnual / 100) * self._saldo / 12
        self._saldo += interes_ganado
        
        # Restar la comisión
        if self._cantExtracciones <= 4:
            self._saldo -= self._cantExtracciones * self._valorComisionMensual
        else:
            self._saldo -= (self._cantExtracciones * self._valorComisionMensual)+((self._cantExtracciones-4)*1000)
            
        if self._saldo < 0 and self.__activa==True:
            self.__activa==False
        
        self.__str__()
        
"""    
  -> Cuenta corriente: posee un atributo “límite descubierto”, el cual se inicializa en cero y el banco lo 
      modifica cuando desea. También contiene la acumulacion de “penalizaciones” cobradas en el mes por utilizar 
      la cuenta sin saldo, este valor figura en el extracto. El comportamiento de la cuenta es el siguiente:
"""

class CuentaCorriente(Cuenta):
    
    __SALDO_QUITADO_POR_PENALIZACION=0
    
    def __init__(self, saldo:float, cantExtracciones:int, cantDepositos:int, tazaInteresAnual:float, valorComisionMensual:float):
        super().__init__(saldo, cantExtracciones, cantDepositos, tazaInteresAnual, valorComisionMensual)
        self.__limiteDescubierto=0
        self.__contPenalizaciones=0
        
    def establecerLimiteDescubierto(self, limiteDescubierto:float):
        if not isinstance(limiteDescubierto, (int, float)):
            raise ValueError("El limite debe ser un numero")
        else:
            self.__limiteDescubierto=limiteDescubierto    
        
    """
       • Retirar: se retira dinero de la cuenta actualizando su saldo. Se puede
        retirar dinero superior al saldo siempre considerando el límite en
        descubierto que tiene asignado la cuenta. En este caso el saldo
        queda con valor negativo.
        • Depositar: cuando el saldo es negativo, la cantidad depositada reduce
        la deuda pero primero se le cobra una penalización del 2% del valor
        adeudado (si tiene saldo negativo y deposita plata, primero se calcula
        la penalización y se le resta al depósito, luego se suma el valor
        resultante en el saldo).
    """
     
    def Depositar(self, depositar:float):
        if not isinstance(depositar, (int, float)) or depositar<0:
            raise ValueError("El deposito debe ser un numero positivo")
        else:
            if self._saldo < 0:
                self._saldo+=depositar
                self._saldo-=depositar*0.02
                self.__SALDO_QUITADO_POR_PENALIZACION+=depositar*0.02
                self.__contPenalizaciones+=1
            else:
                self._saldo+=depositar    
        
    
    def Extraer(self, extraer:float):
        if not isinstance(extraer, (int,float)) or extraer<0:
            raise ValueError("El dinero a extraer debe ser un numero positivo")
        else:
            if extraer < (self._saldo+self.__limiteDescubierto):
                print(f"Se extrajo {extraer}$")
                self._saldo-=extraer
            else:
                print("Ni con el limite descubierto puedes retirar")
                
    """
        • Extracto mensual: Muestra la información del estado de la cuenta y
            agrega información sobre el saldo cobrado por penalizaciones.
    """
    
    def __str__(self) -> str:
        return (f"Cuenta:\n"
                f"Saldo: {self._saldo}\n"
                f"Cantidad de Extracciones: {self._cantExtracciones}\n"
                f"Cantidad de Depósitos: {self._cantDepositos}\n"
                f"Tasa de Interés Anual: {self._tazaInteresAnual}%\n"
                f"Valor Comisión Mensual: {self._valorComisionMensual}\n"
                f"Saldo quitado por penalizacion: {self.__SALDO_QUITADO_POR_PENALIZACION}") 
    
    def ActMensual(self)->str:
        self.__str__()
        
                            