funcionamiento = True
suma = 0
contador = 0
promedio = 0

while funcionamiento :
    numero = int(input("ingrese un numero:"))
    if (numero > 0):
        suma = suma + numero
        contador += 1
    else:
        promedio = suma/contador
        print(f"el promedio es {promedio} con un total de {suma} ingresos")
        funcionamiento = False