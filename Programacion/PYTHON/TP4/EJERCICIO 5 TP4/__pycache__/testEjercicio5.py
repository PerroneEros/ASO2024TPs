from Ejercicio5 import MascotaVirtual

class TestHombreConGorra:
    @staticmethod

    def test():
        nombre=input("Dame el nombre de tu personaje ")
        Hombre = MascotaVirtual(nombre, 100, 100, 100, False, 100)  # Valores de ejemplo

        print(Hombre.estaVivo())

        while Hombre.estaVivo():
            print("   Este es tu Tamagotchi")
            print("       ____ ")
            print("      /    \\")
            print("     /      \\")
            print("    |  ^  ^  |")
            print("    |   --   |")
            print("     \\  \\_/  /")
            print("       ||")
            print("      /||\\")
            print("     / || \\")
            print("       ||")
            print("      /  \\")
            print("     /    \\")
            print("¿Que queres hacer?")
            print("1- Comer")
            print("2- Beber")
            print("3- Dormir")
            print("4- Desperar")
            print("5- Jugar")
            print("6- Caminar")
            print("7- Saltar")
            print("8- Bañarse")
            print("9- Obtener humor")
            opcion=int(input("¿Que va a hacer el muchacho? "))

            if opcion==1:
                Hombre.comer()
            elif opcion==2:
                Hombre.beber()
            elif opcion==3:
                Hombre.dormir()
            elif opcion==4:
                Hombre.despertar()
            elif opcion==5:
                Hombre.jugar()
            elif opcion==6:
                Hombre.caminar()
            elif opcion==7:
                Hombre.saltar()
            elif opcion==8:
                Hombre.banarse()
            elif opcion==9:
                print(Hombre.obtenerHumor())    

            print("Actualidad del personaje...")  
            print(f"Nombre:{Hombre.obtenerNombre()}, Energia:{Hombre.obtenerEnergia()}, Higiene:{Hombre.obtenerHigiene()}, Esta vivo?:{Hombre.estaVivo()}")    
            opcion=0                          


if __name__ == "__main__":
    TestHombreConGorra.test()