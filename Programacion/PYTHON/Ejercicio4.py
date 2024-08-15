
numero1 = int(input("ingrese el primer numero:"))
numero2 = int(input("ingrese el segundo numero:"))
numero3 = int(input("ingrese el tercer numero:"))

mayor = numero1
menor = numero1

if (numero2 > mayor):
    mayor = numero2
elif (numero2 < menor):
    menor = numero2

if (numero3 > mayor):
    mayor = numero3
elif (numero3 < menor):
    menor = numero3

print(f"el mayor es {mayor} y el menor es {menor}")