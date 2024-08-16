oracion = input("ingrese una oracion:")
contador = 0

for letra in oracion:
    if letra == 'a' or letra == 'e' or letra == 'i' or  letra == 'o' or  letra == 'u':
        contador += 1

if contador == 0:
    print("la oracion no tiene vocales")
else:
    print(f"la oracion tiene {contador} vocales")    