'''7. Implemente un programa que le pida una palabra al usuario y cuenta la cantidad de 
vocales en ella. El programa deberá pedirle palabras al usuario hasta que éste 
introduzca la palabra “salir”. '''

palabra = input("ingrese una palabra y te digo cuantas vocales tiene, si quiere salir introduzca la palabra salir: ").lower()

contador_de_vocales = 0
while palabra != "salir":
    for i in palabra:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            contador_de_vocales += 1
    palabra = input(f"la palabra tiene {contador_de_vocales} vocal , ingrese otra palabra o escriba salir: ")
    contador_de_vocales = 0
