
cadena = input("ingresa una oracion:")
espacio = ' '
contador = 0

for i in cadena:
    if (i == espacio):
        contador += 1

print(f"hay {contador} espacios en la oracion")