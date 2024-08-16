cantidad = int(input("cuantos numeros va a ingresar:"))

suma = 0

for i in range(1,cantidad+1,1):
    suma = int(input("ingresa un numero:")) + suma 

promedio = suma/cantidad

print(f"el promedio es: {promedio}")