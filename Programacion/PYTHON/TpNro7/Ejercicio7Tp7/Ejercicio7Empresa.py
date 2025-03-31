from datetime import date
from abc import ABC, abstractmethod

class Fecha:
    def __init__(self, dia: int, mes: int , anio:int):
        """inicializa una fecha si los valores son correctos, sino lanza una excepción"""
        
        if mes < 1 or mes > 12:
            raise ValueError("El mes debe estar entre 1 y 12")
        elif mes == 2 and dia > 28 and not self.__EsAnioBisiesto(anio):
            raise ValueError("Febrero no puede tener más de 28 días")
        elif mes == 2 and dia > 29 and self.__EsAnioBisiesto():
            raise ValueError("Febrero no puede tener más de 29 días en año bisiesto")
        elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
            raise ValueError("El mes no puede tener más de 30 días")
        elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia > 31:
            raise ValueError("El mes no puede tener más de 31 días")
        else:
            self.__dia = dia
            self.__mes = mes
            self.__anio = anio
    
    def establecerDia(self, dia: int):
        self.__dia = dia

    def establecerMes(self, mes: int):
        self.__mes = mes
    
    def establecerAnio(self, anio: int):
        self.__anio = anio
    
    def obtenerDia(self)->int:
        return self.__dia
    
    def obtenerMes(self)->int:
        return self.__mes
    
    def obtenerAnio(self)->int:
        return self.__anio
    
    def esAnterior(self, otraFecha: "Fecha")->bool:
        """Indica si la fecha actual es anterior a otra fecha recibida por parametro.
        Parámetros:
        - otraFecha: La fecha a comparar.
        
        Retorna:
        - True si la fecha actual es anterior a otraFecha, False en caso contrario."""
        if self.__anio < otraFecha.obtenerAnio():
            return True
        elif self.__anio == otraFecha.obtenerAnio():
            if self.__mes < otraFecha.obtenerMes():
                return True
            elif self.__mes == otraFecha.obtenerMes():
                if self.__dia < otraFecha.obtenerDia():
                    return True
        return False
    
    def sumaDias(self, dias: int)->"Fecha":
        """Suma una cantidad de días a la fecha actual y devuelve la nueva fecha
        Parámetros:
        - dias: La cantidad de días a sumar.
        Retorna:
        - La nueva fecha."""
        dia = self.__dia + dias
        mes = self.__mes
        anio = self.__anio
        while dia > self.__diasDelMes(mes):
            dia -= self.__diasDelMes(mes)
            mes += 1
            if mes > 12:
                mes = 1
                anio += 1
        return Fecha(dia, mes, anio)

    def diaSiguiente(self)->"Fecha":
        return self.sumaDias(1)
    
    def esIgual(self, otraFecha: "Fecha")->bool:
        return self.__dia == otraFecha.obtenerDia() and self.__mes == otraFecha.obtenerMes() and self.__anio == otraFecha.obtenerAnio()
    
    def __str__(self) -> str:
        return f"{self.__dia}/{self.__mes}/{self.__anio}"
    
    def diferenciaEnAnios(self, otraFecha:"Fecha")->float:
        """Calcula la diferencia en días, mes y años entre la fecha que recibe el mensaje y la fecha recibida por parámetro.
        Parámetros:
        - otraFecha: Fecha a comparar.
        Si no recibe un objeto de tipo Fecha lanza un ValueError.
        Retorna:
        - Un valor real con los años de la diferencia."""
        if not isinstance(otraFecha, Fecha):
            raise ValueError("El objeto a comparar debe ser de tipo Fecha.")
        dias = 0
        if self.esAnterior(otraFecha):
            primeraFecha = self.clonar()
            segundaFecha = otraFecha
        else:
            primeraFecha = otraFecha.clonar()
            segundaFecha = self   
        while not primeraFecha.esIgual(segundaFecha):
            primeraFecha = primeraFecha.diaSiguiente()
            dias += 1
        anios = dias / 365
        return anios
    
    def diferenciaHoy(self)->float:
        """Calcula la diferencia en años entre la fecha que recibe el mensaje y la fecha actual."""
        hoy = Fecha(date.today().day, date.today().month, date.today().year)
        return self.diferenciaEnAnios(hoy)
    
    def clonar(self)->"Fecha":
        return Fecha(self.__dia, self.__mes, self.__anio)
    #métodos auxiliares        
    def __EsAnioBisiesto(self, anio:int)->bool:
        return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)
    
    def __diasDelMes(self, mes: int)->int:
        if mes == 2:
            if self.__EsAnioBisiesto(self.__anio):
                return 29
            else:
                return 28
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            return 30
        else:
            return 31
        
    """
    Clase empleado
    """        
    
class Empleado(ABC):
    
    def __init__(self, dni:str, nombre:str, apellido:str, fechaIngreso:'Fecha'):
        self._dni=dni
        self._nombre=nombre
        self._apellido=apellido
        self._fechaIngreso=fechaIngreso
    
    #Consultas abstractas
    @abstractmethod
    def obtenerSalario(self):
        pass
        
    #Comandos    
    def establecerDni(self, dni:str):
        pass
    
    def establecerNombre(self, nombre:str):
        pass
    
    def establecerApellido(self, apellido:str):
        pass
    
    def establecerFechaIngreso(self, fecha:'Fecha'):
        pass 
    
    #Consultas
    def obtenerDni(self)->str:
        return self._dni
    
    def obtenerNombreCompleto(self)->str:
        return self._nombre + " " + self._apellido
    
    def obtenerFechaIngreso(self)->Fecha:
        return self._fechaIngreso
       
    """
    Class empleado salario fijo
    """
    
class EmpleadoSalarioFijo(Empleado):
    
    __AUMENTO_MENOR_DE_DOS_ANIOS=0
    __AUMENTO_MAYOR_A_DOS_MENOR_CINCO_ANIOS=0.05
    __AUMENTO_MAYOR_A_CINCO_ANIOS=0.1
    
    def __init__(self, dni:str, nombre:str, apellido:str, fechaIngreso:'Fecha', salarioMinimo:float):
        super().__init__(dni, nombre, apellido, fechaIngreso)
        self.__salarioMinimo=salarioMinimo
        
    def establecerSalarioMinimo(self, minimo:float):
        if isinstance(minimo, float) or minimo<0:
            raise ValueError("Minimo debe ser un float mayor a 0")
        else:
            self.__salarioMinimo=minimo
            
    def obtenerSalarioMinimo(self)->float:
        return self.__salarioMinimo
    
    """
        Los empleados con salario fijo tienen un sueldo básico y un porcentaje adicional en
        función del número de años que llevan la empresa:
            ● Menos de 2 años: Nada.
            ● De 2 a 5 años: 5% más.
            ● Más de 5 años: 10% más.
    """
    
    def calcularAumento(self)->float:
        #Se tomara hoy por 15/10/2024
        Hoy = Fecha(15,10,2024)
        cantAnios = Hoy.diferenciaEnAnios(self._fechaIngreso)
        aumento=0
        
        if cantAnios > 5:
            self.__salarioMinimo * self.__AUMENTO_MAYOR_A_CINCO_ANIOS = aumento
        elif cantAnios <= 5 and cantAnios > 2:
            self.__salarioMinimo * self.__AUMENTO_MAYOR_A_DOS_MENOR_CINCO_ANIOS = aumento
        else:
            self.__salarioMinimo * self.__AUMENTO_MENOR_DE_DOS_ANIOS= aumento         
        
        return aumento
    
    def obtenerSalario(self):
        return self.__salarioMinimo + self.calcularAumento()
    
    """
    Clase Empleado Salario a comision
    """
    
class EmpleadoSalarioComision(Empleado):
    
    def __init__(self, dni:str, nombre:str, apellido:str, fechaIngreso:str, salarioMinimo:float, clientesCaptados:int, monto:float):
        super().__init__(dni, nombre, apellido, fechaIngreso)
        self.__salarioMinimo=salarioMinimo
        self.__clientesCaptados=clientesCaptados
        self.__monto=monto
    
    """
         Los empleados a comisión tienen un salario mínimo, un número de clientes captados
        y un monto a cobrar por cada cliente captado. El salario se obtiene multiplicando los
        clientes captados por el monto por cliente.
         Si el salario obtenido por los clientes
        captados no llega a cubrir el salario mínimo, cobrará el salario mínimo.
    """
    
    def obtenerSalario(self)->float:
        SalarioEspeculado=self.__clientesCaptados*self.__monto
        
        if SalarioEspeculado > self.__salarioMinimo:
            return SalarioEspeculado
        else:
            return self.__salarioMinimo
        
    #Comandos      
    def establecerSalariosMinimo(self, salarioMin:float):
        pass
    
    def establecerClientesCaptados(self, clientesCaptados:int):
        pass
    
    def establecerMonto(self, monto:float):
        pass
    
    #Consultas
    def obtenerSalariosMinimo(self)->float:
        return self.__salarioMinimo
    
    def obtenerClientesCaptados(self)->int:
        return self.__clientesCaptados
    
    def obtenerMonto(self)->float:
        return self.__monto
    
    """
    Clase Empresa
    """
    
class Empresa():
    
    def __init__(self):
        self.__empleados=[]
        
    def agregarEmpleado(self, empleado:'Empleado'):
        if not isinstance(empleado, Empleado):
            raise ValueError("La empleado debe ser de tipo Empleado")
        else:
            if empleado not in self.__empleados:
                self.__empleados.append(empleado)
            else:
                print(f"La póliza {empleado.obtenerNombre()} ya está asignada a esta aseguradora.")

    def eliminarEmpleado(self, empleado:'Empleado'):
        if not isinstance(empleado, Empleado):
            raise ValueError("La empleado debe ser de tipo Empleado")
        
        if empleado in self.__empleados:
            self.__empleados.remove(empleado)
            print(f"La póliza {empleado.obtenerNombre()} fue eliminada.")
        else:
            print("La póliza no existe en la aseguradora.")
            
    def masClientesCaptados(self)->'EmpleadoSalarioComision':
        """Devuelve el empleado a comisión con más clientes captados usando obtenerClientesCaptados."""
        empleados_comision = [emp for emp in self.__empleadosempleados if isinstance(emp, EmpleadoSalarioComision)]
        
        if not empleados_comision:
            return None  # No hay empleados a comisión
        
        # Inicializar con None y hacer la comparación desde el inicio
        empleado_max_clientes = None
        max_clientes = -1  # Inicializamos con un valor menor a cualquier número de clientes
        
        # Recorrer todos los empleados a comisión
        for empleado in empleados_comision:
            if empleado.obtenerClientesCaptados() > max_clientes:
                max_clientes = empleado.obtenerClientesCaptados()
                empleado_max_clientes = empleado
        
        return empleado_max_clientes
          