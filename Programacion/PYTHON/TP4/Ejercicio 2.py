#2)a)
class Empleado:
                                  #atributos de instancia
                                  #constructores
    def __init__(self, legajo:int, horasTrabajadasMes:int, valorHora:float):
        self.__legajo = legajo
        #comandos
        self.__horasTrabajadasMes = horasTrabajadasMes
        self.__valorHora = valorHora
    
    def calcular_sueldo(self):
        return self.__horasTrabajadasMes * self.__valorHora
       
   #consultas
    def obtenerLegajo(self)->int:
        return self.__legajo
    def obtenerHorasTrabajadas(self)->int:
        return self.__horasTrabajadasMes
    def obtenerValorHora(self)->float:
        return self.__valorHora
    def obtenerSueldo(self)->float:
        return self.calcular_sueldo

#2)b)
def tester_empleado():
    legajo = int(input("ingrese el legajo del empleado: "))
    horasTrabajadasMes = int(input("ingrese la cantidad de horas trabajada por mes: "))
    valorHora = float(input("ingrese el valor por hora: "))

    empleado = Empleado(legajo,horasTrabajadasMes,valorHora)
    sueldo = empleado.obtenerSueldo
    
    print(f"el legajo es: {empleado.obtenerLegajo} y el sueldo es: {sueldo}")

tester_empleado()

#2)c)
def tester_empleado_verificacion():
    legajo = int(input("ingrese el legajo del empleado:"))
    
    empleado = Empleado(legajo,0,0)
    
    empleado.__horasTrabajadasMes = int(input("ingrese la cantidad de horas trabajadas:"))
    empleado.__valorHora = float(input("ingrese la cantidad de horas:"))

    sueldo = empleado.calcular_sueldo()

    print(f"el legajo es: {empleado.obtenerLegajo} y el sueldo es {sueldo}")

tester_empleado_verificacion()