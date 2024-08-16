#!/usr/bin/env python

lado1=int(input("cuanto es el valor del primer lado:"))
lado2=int(input("cuanto es el valor del segundo lado:"))
lado3=int(input("cuanto es el valor del tercer lado:"))

if (lado1 == lado2 == lado3):
    print("el triangulo es equilatero")
elif ((lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3)):
    print("el triangulo es isoceles")
else:
    print("el triangulo es escaleno")       