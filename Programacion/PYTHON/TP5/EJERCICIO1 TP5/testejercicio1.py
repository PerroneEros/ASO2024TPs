from ejercicio1 import Atleta 

class testAtleta:

    @staticmethod

    def test():
        Atleta_1= Atleta("Marcos")
        Atleta_2= Atleta("Santiago")

        print(f"Destreza del atleta uno:{Atleta_1.obtenerDestreza()}")   
        print(f"Destreza del atleta dos:{Atleta_2.obtenerDestreza()}")  

        for i in range(10):
            Atleta_1.Entrenar()

        for i in range(5):
            Atleta_2.Entrenar()

        print(f"Destreza del atleta uno:{Atleta_1.obtenerDestreza()}")   
        print(f"Destreza del atleta dos:{Atleta_2.obtenerDestreza()}")  

        print(f"Energia del atleta uno:{Atleta_1.obtenerEnergia()}")
        print(f"Energia del atleta dos:{Atleta_2.obtenerEnergia()}")   

        Atleta_1.Descansar()
        Atleta_2.Descansar()

        print(f"Energia del atleta uno:{Atleta_1.obtenerEnergia()}")
        print(f"Energia del atleta dos:{Atleta_2.obtenerEnergia()}")  

        if Atleta_1.mayorDestrezaQue(Atleta_2):
            print("El atleta nro 1 es el master mister")
        elif Atleta_1.mismaDestrezaQue(Atleta_2):
            print("Estos dos son los master mister")
        else:
            print("El atleta nro 2 es el master mister")


if __name__ == "__main__":
    testAtleta.test()