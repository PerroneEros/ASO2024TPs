from datetime import date
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
    
class TestFecha:
    @staticmethod
    def run():
        fecha1 = Fecha(11, 3, 2021)
        fecha2 = Fecha(16, 3, 2021)
        print(f"fecha1: {fecha1} es anterior a fecha2 {fecha2}: {fecha1.esAnterior(fecha2)}")
        fecha1.establecerDia(16)
        print(f"fecha1 {fecha1} es anterior a fecha2 {fecha2}: {fecha1.esAnterior(fecha2)}")
        fecha1.establecerMes(9)
        fecha1.establecerAnio(2022)
        print(f"fecha1 {fecha1} es anterior a fecha2 {fecha2}: {fecha1.esAnterior(fecha2)}")
        print(f"Fecha 1: {fecha1}")
        fecha1 = fecha1.diaSiguiente()
        print(f"Fecha 1: {fecha1}")
        fecha1=fecha1.sumaDias(19)
        print(f"Fecha 1: {fecha1}")
        fecha1=fecha1.sumaDias(30)
        print(f"Fecha 1: {fecha1}")
        fecha1=fecha1.sumaDias(62)
        print(f"Fecha 1: {fecha1}")
        fecha2 = Fecha(30, 9, 2024)
        fecha1 = Fecha(9, 3, 2020)
        print(f"Diferencia '{fecha1}' con '{fecha2}': {fecha1.diferenciaEnAnios(fecha2)}")
        print(f"Diferencia en años cast INT: {int(fecha1.diferenciaEnAnios(fecha2))}")

        print(f"Diferencia en años con hoy: {fecha1.diferenciaHoy()}")
        print(f"Diferencia en años con hoy cast INT: {int(fecha1.diferenciaHoy())}")


if __name__ == "__main__":
    TestFecha.run()