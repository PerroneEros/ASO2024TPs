class Vinoteca:

    CAPCIDADMAXIMA=5000

    #atributos de la instacia

    def __init__(self, cantJugos: int = 5000, __cantBlancos: int = 5000, cantTitosJovenes: int = 5000, cantTintosAnejados: int = 5000):
        self.__cantJugos = cantJugos
        self.__cantBlancos = __cantBlancos
        self.__cantTitosJovenes = cantTitosJovenes
        self.__cantTintosAnejados = cantTintosAnejados

    def reponerJugos(self):
        self.__cantJugos=5000

    def reponerVinosBlancos(self):
        self.__cantBlancos=5000

    def reponerVinosTintosJoven(self):
        self.__cantTitosJovenes=5000

    def reponerVinosTintosAnejado(self):
        self.__cantTintosAnejados=5000

    def venderJugos(self, unidades:int):
        if (unidades <= self.__cantJugos):
            self.__cantJugos -= unidades
            print(f"Venta realizada: {unidades} jugos vendidos. Stock restante: {self.__cantJugos}.")
        else:
            StockActual = self.__cantJugos
            self.__cantJugos = 0
            print(f"Venta parcial realizada: {StockActual} jugos vendidos. Stock agotado.")

    def venderVinosBlancos(self, unidades:int):
        if (unidades <= self.__cantBlancos):
            self.__cantBlancos -= unidades
            print(f"Venta realizada: {unidades} jugos vendidos. Stock restante: {self.__cantBlancos}.")
        else:
            StockActual = self.__cantBlancos
            self.__cantBlancos = 0
            print(f"Venta parcial realizada: {StockActual} jugos vendidos. Stock agotado.")

    def venderVinosTintosJoven(self, unidades:int):
        if (unidades <= self.__cantTitosJovenes):
            self.__cantTitosJovenes -= unidades
            print(f"Venta realizada: {unidades} jugos vendidos. Stock restante: {self.__cantTitosJovenes}.")
        else:
            StockActual = self.__cantTitosJovenes
            self.__cantTitosJovenes = 0
            print(f"Venta parcial realizada: {StockActual} jugos vendidos. Stock agotado.")

    def venderVinosTintosAnejado(self, unidades:int):
        if (unidades <= self.__cantTintosAnejados):
            self.__cantTintosAnejados -= unidades
            print(f"Venta realizada: {unidades} jugos vendidos. Stock restante: {self.__cantTintosAnejados}.")
        else:
            StockActual = self.__cantTintosAnejados
            self.__cantTintosAnejados = 0
            print(f"Venta parcial realizada: {StockActual} jugos vendidos. Stock agotado.")    

    def ObtenerCantidadJugos(self)->int:
        return self.__cantJugos

    def ObtenerCantidadVinosBlancos(self)->int:
        return self.__cantBlancos

    def ObtenerCantidadVinosTintoJovenes(self)->int:
        return self.__cantTitosJovenes

    def ObtenerCantidadVinosTintoAnejado(self)->int:
        return self.__cantTintosAnejados       