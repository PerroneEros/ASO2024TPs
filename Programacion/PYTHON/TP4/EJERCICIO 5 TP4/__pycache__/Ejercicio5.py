class MascotaVirtual:

    MAX_VALOR = 100
    MIN_VALOR = 0
    
    def __init__(self,nombre:str,energia:int=MAX_VALOR,diversion:int=MAX_VALOR,higiene:int=MAX_VALOR,dormido:bool=False,cantActividadesDesgaste:int=MAX_VALOR):
        self.__nombre = nombre
        self.__energia = energia
        self.__diversion = diversion
        self.__higiene = higiene
        self.__dormido = dormido
        self.__cantActividadesDesgaste = cantActividadesDesgaste
    
    def comer(self):
        if self.__dormido:
            print("No puede hacer esto,esta durmiendo")
        elif self.__energia + 20 <= self.MAX_VALOR:
            self.__energia += 20
        else:
            self.__energia = self.MAX_VALOR
        return self.__energia
    
    def beber(self):
        if self.__dormido:
            print("No puede hacer esto,esta durmiendo")
        elif self.__energia + 10 <= self.MAX_VALOR:
            self.__energia += 10
        else:
            self.__energia = self.MAX_VALOR
        return self.__energia
    
    def dormir(self):
        if self.__dormido:
            print("ya esta dormido")
        else:
            self.__dormido = True
            self.__energia += 20
            self.__diversion -= 10
            if self.__energia > self.MAX_VALOR:
                self.__energia = self.MAX_VALOR
            if self.__diversion < 0:
                self.__diversion = self.MIN_VALOR
        return self.__dormido,self.__energia,self.__diversion
    
    def despertar(self):
        self.__dormido = False
        return self.__dormido

    def jugar(self):
        if self.__dormido:
            print("No puede hacer esto,esta durmiendo")
        else:
            if(self.__diversion+40>self.MAX_VALOR):
                self.__diversion=self.MAX_VALOR
            else:
                self.__diversion += 40
            if self.__energia - 20 < self.MIN_VALOR:
                self.__energia = self.MIN_VALOR
            else:
                self.__energia = self.__energia - 20
            if self.__higiene - 15 < self.MIN_VALOR:
                self.__higiene = self.MIN_VALOR
            else:
                self.__higiene = self.__higiene - 15
        return self.__dormido,self.__diversion,self.__energia,self.__higiene
    
    def caminar(self):
        if self.__dormido:
            print("No puede hacer esto,esta durmiendo")
        else:
            if self.__diversion + 20 > self.MAX_VALOR:
                self.__diversion = self.MAX_VALOR
            else:
                self.__diversion += 20
            if self.__energia - 10 < self.MIN_VALOR:
                self.__energia = self.MIN_VALOR
            else:
                self.__energia -= 10
            if self.__higiene - 8 < self.MIN_VALOR:
                self.__higiene = self.MIN_VALOR
            else:
                self.__higiene -= 8
        return self.__dormido,self.__diversion,self.__energia,self.__higiene
    
    def saltar(self):
        if self.__dormido:
            print("No puede hacer esto,esta durmiendo")
        else:
            if self.__diversion + 10 > self.MAX_VALOR:
                self.__diversion = self.MAX_VALOR
            else:
                self.__diversion += 10
            if self.__energia - 15 < self.MIN_VALOR:
                self.__energia = self.MIN_VALOR
            else:
                self.__energia -= 15
            if self.__higiene - 10 < self.MIN_VALOR:
                self.__higiene = self.MIN_VALOR
            else:
                self.__higiene -= 10
        return self.__dormido,self.__diversion,self.__energia,self.__higiene

    def banarse(self): 
        if self.__diversion - 10 < self.MIN_VALOR:
            self.__diversion = self.MIN_VALOR
        else:
            self.__diversion -= 10
        if (self.__higiene + 40 >self.MAX_VALOR):
            self.__higiene=self.MAX_VALOR
        else:
            self.__higiene += 40
        return self.__higiene, self.__diversion 

    def obtenerNombre(self)->str:
        return self.__nombre
    
    def obtenerEnergia(self)->int:
        return self.__energia
    
    def obtenerDiversion(self)->int:
        return self.__diversion
    
    def obtenerHigiene(self)->int:
        return self.__higiene

    def estaDormido(self)->bool:
        return self.__dormido
    
    def obtenerHumor(self)->str:
        humor = ""
        if self.__energia > 70 and self.__diversion > 70 and self.__higiene > 70:
            humor = "Estoy Muy Feliz"
        elif ((self.__energia > 50 and self.__diversion > 50 ) or (self.__energia > 50 and self.__higiene > 50) or (self.__diversion > 50 and self.__higiene > 50)):
            humor = "Estoy Alegre"
        elif ((self.__energia > 30 and self.__diversion > 30 ) or (self.__energia > 30 and self.__higiene > 30) or (self.__diversion > 30 and self.__higiene > 30)):
            humor = "Estoy neutral"
        elif ((self.__energia > 10 and self.__diversion > 10 ) or (self.__energia > 10 and self.__higiene > 10) or (self.__diversion > 10 and self.__higiene > 10)):
            humor = "Estoy Triste :( )"
        elif ((self.__energia < 10 and self.__diversion < 10 ) or (self.__energia < 10 and self.__higiene < 10) or (self.__diversion < 10 and self.__higiene < 10)):
            humor = "Estoy Muy Triste ;( )"
        else:
            humor = "Estoy cansado de esta vida chau *se pega un tiro*"
        return humor
    
    def estaVivo(self)->bool:
        if self.__energia == self.MIN_VALOR:
            return False
        else:
            return True
        